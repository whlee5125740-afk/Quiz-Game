"""퀴즈 게임 흐름과 JSON 파일 저장을 담당한다 (표준 라이브러리만 사용)."""

import json
from pathlib import Path
from shutil import copy2
from datetime import datetime

from quiz import Quiz


DEFAULT_QUIZZES = [
    Quiz("파이썬에서 화면에 글자를 출력하는 함수는?", ["print()", "input()", "len()", "type()"], 1),
    Quiz("파이썬에서 사용자 입력을 받는 함수는?", ["range()", "input()", "sum()", "str()"], 2),
    Quiz("여러 항목을 순서대로 저장하는 자료형은?", ["bool", "int", "list", "float"], 3),
    Quiz("조건에 따라 실행할 코드를 결정하는 키워드는?", ["for", "def", "import", "if"], 4),
    Quiz("같은 명령을 조건이 참인 동안 반복하는 문장은?", ["while", "return", "class", "break"], 1),
    Quiz("JSON 파일을 다루는 표준 라이브러리의 이름은?", ["math", "json", "random", "pathlib"], 2),
]


class QuizGame:
    def __init__(self, data_path: Path | str | None = None):
        self.data_path = Path(data_path) if data_path is not None else Path(__file__).resolve().parent / "state.json"
        self.quizzes = []
        self.best_score = 0
        self.load()

    def load(self) -> None:
        if not self.data_path.exists():
            print("안내: 저장 파일이 없어 기본 퀴즈로 시작합니다.")
            self._use_defaults()
            self.save()
            return
        try:
            with self.data_path.open("r", encoding="utf-8") as f:
                saved = json.load(f)
            if not isinstance(saved, dict) or not isinstance(saved.get("quizzes"), list):
                raise ValueError("JSON에 quizzes 목록이 없습니다.")
            scores = saved.get("best_score")
            if type(scores) is not int or scores < 0:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")
            items = [Quiz.from_dict(item) for item in saved["quizzes"]]
            self.quizzes = items
            self.best_score = scores
            print(f"저장된 데이터 로드: 퀴즈 {len(items)}개, 최고 점수 {scores}점")
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError, TypeError) as exc:
            print(f"안내: 저장 파일을 읽을 수 없습니다 ({exc}). 기본 퀴즈로 복구합니다.")
            self._backup_bad_file()
            self._use_defaults()
            self.save()

    def _backup_bad_file(self) -> None:
        if not self.data_path.exists():
            return
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        backup = self.data_path.with_name(f"{self.data_path.stem}.corrupt-{stamp}.bak")
        try:
            copy2(self.data_path, backup)
            print(f"손상된 원본은 {backup.name}에 보관했습니다.")
        except OSError as exc:
            print(f"주의: 손상 파일 백업에 실패했습니다 ({exc}). 원본을 덮어쓰지 않습니다.")
            self._allow_save = False

    def _use_defaults(self) -> None:
        self.quizzes = [Quiz.from_dict(q.to_dict()) for q in DEFAULT_QUIZZES]
        self.best_score = 0

    def save(self) -> bool:
        if getattr(self, "_allow_save", True) is False:
            return False
        payload = {"quizzes": [q.to_dict() for q in self.quizzes], "best_score": self.best_score}
        try:
            self.data_path.parent.mkdir(parents=True, exist_ok=True)
            temporary = self.data_path.with_name(self.data_path.name + ".tmp")
            with temporary.open("w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
                f.write("\n")
            temporary.replace(self.data_path)
            return True
        except OSError as exc:
            print(f"저장 실패: {exc}")
            return False

    @staticmethod
    def read_number(prompt: str, low: int, high: int) -> int:
        while True:
            raw = input(prompt).strip()
            if not raw:
                print("입력값이 비어 있습니다. 다시 입력하세요.")
                continue
            try:
                value = int(raw)
            except ValueError:
                print(f"숫자를 입력하세요 ({low}~{high}).")
                continue
            if low <= value <= high:
                return value
            print(f"{low}~{high} 사이의 숫자를 입력하세요.")

    @staticmethod
    def read_text(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("내용을 비워 둘 수 없습니다. 다시 입력하세요.")

    def play(self) -> None:
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return
        score = 0
        print(f"\n퀴즈 시작! 총 {len(self.quizzes)}문제 (정답은 1~4 입력)")
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.show(i)
            answer = self.read_number("정답 번호 (1~4): ", 1, 4)
            if quiz.is_correct(answer):
                score += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답: {quiz.answer}번 ({quiz.choices[quiz.answer - 1]})")
        print(f"\n게임 결과: {len(self.quizzes)}문제 중 {score}문제 정답")
        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
            self.save()
        print(f"최고 점수: {self.best_score}점")

    def add_quiz(self) -> None:
        print("\n새 퀴즈 등록")
        question = self.read_text("문제: ")
        if any(q.question.casefold() == question.casefold() for q in self.quizzes):
            print("이미 등록된 문제입니다.")
            return
        choices = [self.read_text(f"선택지 {i}: ") for i in range(1, 5)]
        answer = self.read_number("정답 번호 (1~4): ", 1, 4)
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        if self.save():
            print("새 퀴즈를 저장했습니다.")
        else:
            print("퀴즈가 메모리에만 추가되었습니다. 저장 오류를 확인하세요.")

    def list_quizzes(self) -> None:
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n등록된 퀴즈 목록: {len(self.quizzes)}개")
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.show(i)
            print(f"  정답: {quiz.answer}번")

    def show_best_score(self) -> None:
        print(f"최고 점수: {self.best_score}점 (등록 문제 {len(self.quizzes)}개)")

    def run(self) -> None:
        try:
            while True:
                print("\n===== 나만의 4지선다 퀴즈 게임 =====")
                print("1. 퀴즈 풀기")
                print("2. 퀴즈 추가")
                print("3. 퀴즈 목록")
                print("4. 최고 점수 확인")
                print("5. 종료")
                selected = self.read_number("메뉴 선택 (1~5): ", 1, 5)
                if selected == 1:
                    self.play()
                elif selected == 2:
                    self.add_quiz()
                elif selected == 3:
                    self.list_quizzes()
                elif selected == 4:
                    self.show_best_score()
                else:
                    print("게임을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 안전하게 종료합니다.")
        finally:
            self.save()
