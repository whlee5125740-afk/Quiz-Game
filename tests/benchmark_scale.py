"""확장성 확인용 측정 도구. 실제 제출 데이터(state.json)는 수정하지 않습니다.

실행: 프로젝트 폴더에서 python3 tests/benchmark_scale.py
측정: 문제 생성, 마지막 문제 중복 검색, JSON 저장/불러오기, Python 메모리 사용량.
"""
from contextlib import redirect_stdout
import io
from pathlib import Path
import platform
import sys
from tempfile import TemporaryDirectory
from time import perf_counter
import tracemalloc

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from game import QuizGame  # noqa: E402
from quiz import Quiz  # noqa: E402


def measure(count: int) -> dict:
    """가짜 문제로 별도 임시 JSON을 생성하여 측정하고, 종료 시 자동 삭제합니다."""
    with TemporaryDirectory(prefix="quiz-scale-") as temp:
        data_path = Path(temp) / "state.json"
        with redirect_stdout(io.StringIO()):
            game = QuizGame(data_path)

        tracemalloc.start()
        start = perf_counter()
        game.quizzes = [
            Quiz(
                f"성능 시험용 문제 {i:05d}",
                [f"선택지 {j} - 문제 {i:05d}" for j in range(1, 5)],
                (i % 4) + 1,
            )
            for i in range(count)
        ]
        create_sec = perf_counter() - start

        # game.py의 add_quiz()가 중복을 확인할 때 사용하는 것과 같은 순차 검색입니다.
        target = game.quizzes[-1].question
        repeats = 30
        start = perf_counter()
        for _ in range(repeats):
            found = any(q.question.casefold() == target.casefold() for q in game.quizzes)
            if not found:
                raise AssertionError("마지막 문제 검색 실패")
        search_ms = (perf_counter() - start) / repeats * 1000

        start = perf_counter()
        if not game.save():
            raise RuntimeError("임시 JSON 저장 실패")
        save_sec = perf_counter() - start
        json_kib = data_path.stat().st_size / 1024

        start = perf_counter()
        with redirect_stdout(io.StringIO()):
            loaded = QuizGame(data_path)
        load_sec = perf_counter() - start
        if len(loaded.quizzes) != count:
            raise AssertionError("저장·불러오기 후 문제 수 불일치")
        _, peak_bytes = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return {
            "count": count,
            "create_sec": create_sec,
            "search_ms": search_ms,
            "save_sec": save_sec,
            "load_sec": load_sec,
            "json_kib": json_kib,
            "peak_mib": peak_bytes / (1024 ** 2),
        }


def main() -> None:
    print(f"측정 환경: Python {platform.python_version()} / {platform.system()}")
    print("안전 확인: 프로젝트의 state.json은 읽거나 수정하지 않습니다.")
    print("※ 측정값은 컴퓨터 속도·저장장치·실행 환경에 따라 달라집니다.")
    print("※ 메모리는 tracemalloc의 Python 할당 최고치이며 PC 전체 메모리 사용량과 다릅니다.")
    print("문제수 | 생성(초) | 마지막 문제 검색(밀리초/회) | 저장(초) | 재불러오기(초) | JSON(KiB) | Python 최고 메모리(MiB)")
    for count in (1000, 10000):
        result = measure(count)
        print(
            f"{result['count']:>5} | {result['create_sec']:.4f} | "
            f"{result['search_ms']:.4f} | {result['save_sec']:.4f} | "
            f"{result['load_sec']:.4f} | {result['json_kib']:.1f} | {result['peak_mib']:.2f}"
        )
    print("검증 결과: 임시 데이터 저장·재불러오기 시 문제 수 일치 (2/2)")


if __name__ == "__main__":
    main()
