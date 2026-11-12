# 나만의 4지선다 퀴즈 게임 (Quiz-Game)

> **AI 올인원 교육 과정 · 미션: 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기**

## 한눈에 보는 프로젝트

이 프로그램은 Python을 처음 배우는 **비전공 학습자**가 기초 문법을 직접 사용해 만든 **터미널(명령어 입력 화면)용 4지선다 퀴즈 게임**입니다. 저는 배운 명령어를 문제로 다시 풀어 보고, Git으로 작업 과정을 기록하기 위해 이 주제를 선택했습니다.

- **퀴즈 주제:** Python 기초 문법과 Git 명령어
- **할 수 있는 일:** 퀴즈 풀기, 새 문제 추가, 문제 목록 보기, 최고 점수 확인, 종료 후 데이터 유지
- **코드 구성:** `Quiz`와 `QuizGame`, 두 개의 클래스로 역할을 분리
- **저장 파일:** `state.json`(문제와 최고 점수)
- **검증:** 직접 실행 확인 및 자동 테스트 11개 통과
- **Git 실습:** 10개 이상 커밋, 브랜치 생성·병합, 기본 명령어 7종 실행
- **실행 증빙:** [evidence 폴더의 18장](evidence/)

**확인 상태(2026-11-12):** 프로그램 실행, 기존 GitHub 업로드 및 증빙 17장 등록, 성능 측정의 학습자 PC 실행까지 확인했습니다. **교육 플랫폼에 실제 제출하거나 최종 평가를 통과했는지는 아직 확인하지 않았습니다.**

---

## 1. 프로그램은 어떻게 사용하나요?

`python3 main.py`로 실행하면 아래 메뉴가 나타납니다.

| 번호 | 기능 | 사용자가 하는 일 |
| :---: | --- | --- |
| 1 | 퀴즈 풀기 | 문제마다 보기 네 개 중 정답 번호(1~4)를 입력합니다. |
| 2 | 퀴즈 추가 | 질문·보기 네 개·정답 번호를 입력하면 파일에 저장됩니다. |
| 3 | 퀴즈 목록 | 저장된 문제와 정답을 확인합니다. |
| 4 | 최고 점수 확인 | 가장 많이 맞힌 문제 수와 등록 문제 수를 확인합니다. |
| 5 | 종료 | 게임을 끝냅니다. 기록은 다음 실행에도 남습니다. |

**정상 실행을 확인하는 방법:** 1~5번 메뉴가 나오고, 5번을 입력했을 때 `게임을 종료합니다.`가 표시되면 됩니다. 실습 당시 기본 문제 6개에 Git 문제 1개를 추가했고, 재실행 후에도 **문제 7개와 최고 점수 6점**이 유지되었습니다. 숫자는 사용에 따라 달라질 수 있습니다.

**입력 오류 안내 예시:** 메뉴에서 `abc`를 입력하면 `숫자를 입력하세요 (1~5).`가 나타납니다. `9`를 입력하면 `1~5 사이의 숫자를 입력하세요.`가 나타나고, 아무것도 입력하지 않으면 `입력값이 비어 있습니다. 다시 입력하세요.`라고 알려 줍니다. 잘못 입력해도 메뉴에서 다시 선택할 수 있습니다. [실제 화면](evidence/10-invalid-input-and-interrupt.png)

## 2. 처음 실행하는 방법

### 필요한 환경

- **Python 3.10 이상:** 프로그램 코드를 실행하는 도구. 실습 PC에서 **Python 3.14.4** 확인
- **Git:** 변경 이력을 관리하는 도구. 실습 PC에서 **Git 2.53.0** 확인
- **Ubuntu(WSL) 터미널** 또는 Python이 설치된 Windows 터미널
- 외부 패키지 설치는 필요하지 않음(Python 기본 제공 기능만 사용)

환경 확인 증빙: [09-environment.png](evidence/09-environment.png)

**실행 위치: Ubuntu(WSL) 터미널.** 프로젝트를 내려받을 *상위 폴더*에서 실행합니다.

```bash
git clone https://github.com/whlee5125740-afk/Quiz-Game.git
cd Quiz-Game
python3 main.py
```

- `git clone`: GitHub의 프로젝트를 내 PC로 복사합니다.
- `cd Quiz-Game`: 복사된 폴더로 들어갑니다.
- `python3 main.py`: 프로그램을 시작합니다.

**이미 `Quiz-Game` 폴더가 있으면 다시 복제하지 마세요.** 해당 폴더로 이동한 다음 `python3 main.py`만 실행합니다. Windows PowerShell에서는 설치 환경에 따라 `python main.py`를 사용합니다.

> 게임에서 문제를 추가하거나 최고 점수를 갱신하면 `state.json`이 바뀔 수 있습니다. 제출 파일을 유지하려면 실행 전후 `git status`로 변경 여부를 확인합니다.

## 3. 파일과 코드의 역할

```text
Quiz-Game/
├── main.py                  # 게임 시작
├── quiz.py                  # Quiz: 문제 한 개를 관리
├── game.py                  # QuizGame: 메뉴·점수·파일 저장 관리
├── state.json               # 문제 목록과 최고 점수
├── tests/
│   ├── test_quiz.py         # 기존 자동 테스트 11개
│   └── benchmark_scale.py   # 문제 1,000·10,000개 성능 측정(추가 개선 파일)
├── evidence/                # 이미 검증한 실행 화면 17장
├── README.md                # 이 안내 문서
└── .gitignore               # 임시 파일을 Git에 올리지 않도록 설정
```

> `tests/benchmark_scale.py`는 **이번 추가 개선으로 제공하는 파일**입니다. 이 파일을 PC에 복사하고 GitHub에 커밋하기 전에는 기존 GitHub 저장소에 아직 없습니다.

**클래스(Class)**는 관련 데이터와 기능을 묶어 두는 코드의 구성 단위입니다. **메서드(Method)**는 그 안에서 실행하는 기능(함수)입니다.

| 파일 / 클래스 | 쉬운 설명 | 핵심 메서드와 역할 |
| --- | --- | --- |
| `main.py` | 실행 버튼 역할 | `main()` → `QuizGame().run()` |
| `quiz.py` / `Quiz` | **퀴즈 한 문제**를 담당 | `__init__()` 질문·보기·정답 준비, `show()` 출력, `is_correct()` 정답 확인, `to_dict()`/`from_dict()` 데이터 변환 |
| `game.py` / `QuizGame` | **게임 전체 진행**을 담당 | `run()` 메뉴, `read_number()` 입력 점검, `play()` 풀이·점수 계산, `add_quiz()` 등록, `list_quizzes()` 목록, `show_best_score()` 조회, `save()`/`load()` 파일 저장·불러오기 |

**역할을 나눈 이유:** 문제 하나를 검증하는 코드와 전체 게임을 진행하는 코드를 분리하면, 나중에 특정 기능만 수정하거나 시험하기가 쉽습니다. 예를 들어 `Quiz("문제", ["가", "나", "다", "라"], 2)`처럼 같은 `Quiz` 클래스를 여러 문제에 재사용합니다.

기본 문법은 다음처럼 사용합니다. `if / elif / else`는 메뉴를 선택하고, `while`은 메뉴를 반복하며, `for`는 퀴즈를 순서대로 처리합니다. `str`은 글자, `int`는 정수, `list`는 목록, `dict`는 이름과 값의 묶음입니다. `self`는 현재 객체 자신의 정보를 뜻하고, `__init__`은 객체 생성 시 초기값을 정합니다.

## 4. 문제와 점수는 어떻게 저장하나요?

**JSON**은 이름과 값을 글자 형식으로 저장하는 방법입니다. `state.json`은 프로젝트 최상위 폴더에 **UTF-8**로 저장됩니다.

```json
{
  "quizzes": [
    {
      "question": "파이썬에서 화면에 글자를 출력하는 함수는?",
      "choices": ["print()", "input()", "len()", "type()"],
      "answer": 1
    }
  ],
  "best_score": 6
}
```

**위 코드는 실제 파일 전체가 아니라 형식을 이해하기 위한 축약 예시입니다.** `quizzes`는 문제 목록, `question`은 질문, `choices`는 네 가지 선택지, `answer`는 1~4 중 정답 번호, `best_score`는 지금까지 가장 많이 맞힌 문제 수입니다.

1. 파일이 있으면 `load()`로 기존 데이터를 읽습니다.
2. 파일이 없다면 `game.py`의 `DEFAULT_QUIZZES`에서 **기본 6문제**를 가져와 새 파일을 만듭니다.
3. 문제 추가·최고 점수 갱신·종료 시 `save()`로 저장합니다.
4. 저장할 때 먼저 임시 파일 `state.json.tmp`을 작성한 뒤 원래 파일을 **교체(`replace`)**합니다. 이는 작성 중인 내용을 바로 원본 파일에 쓰지 않기 위한 방법입니다.
5. 파일이 손상되면 가능한 경우 `state.corrupt-날짜.bak` 형태로 원본을 보관한 후 기본 문제로 복구합니다. 손상 원본 보관에 실패하면 덮어쓰지 않도록 저장을 막습니다.

**JSON을 선택한 이유:** 문제 수가 적고 한 사람이 PC에서 실행하는 이 과제에서는 파일 하나로 저장·확인하기 쉽습니다. 별도의 데이터베이스(DB, 대량 데이터 관리 도구)가 필요하지 않습니다. 단, 문제 수가 매우 많거나 여러 사람이 동시에 수정하는 환경에는 검색 속도와 동시 수정 문제가 생길 수 있습니다.

**주의:** 현재 구현은 여러 사용자의 **동시 저장을 조정하는 기능이 없습니다.** 한 파일을 여러 프로그램에서 동시에 수정하지 않는 것이 좋습니다. `.bak` 파일은 자동 삭제하지 않으므로 원인과 복구를 확인한 뒤 보관·정리 여부를 결정합니다. 쓰기 권한 오류가 나면 저장 폴더의 권한과 사용 가능한 공간을 먼저 확인하세요.

## 5. 테스트와 실제 실행 증거

### 자동 테스트 (11개)

**실행 위치: `Quiz-Game` 폴더의 Ubuntu(WSL) 터미널**

```bash
python3 -m unittest discover -s tests -v
```

`unittest`는 Python 기본 자동 검사 도구이며, `discover`는 `tests` 폴더에서 테스트를 찾아 실행한다는 의미입니다.

**2026-11-11 학습자 PC에서 실제 확인된 출력:**

```text
Ran 11 tests in 0.003s

OK
```

문제 데이터 형식, 기본 파일 생성, 저장·재불러오기, 손상 JSON 복구, 중복 차단, 잘못된 메뉴 입력, `Ctrl+C`/EOF 중단, 최고 점수 등을 검사했습니다. 자동 테스트는 별도의 **임시 폴더**를 사용해 실제 `state.json`을 건드리지 않습니다. [02번 증빙](evidence/02-automatic-tests.png)

### 직접 실행한 기능

| 기능 | 실제 확인 결과 | 증빙 |
| --- | --- | --- |
| 메뉴 출력·목록·종료 | 1~5번 메뉴와 기본 문제 6개 출력 | [03번](evidence/03-menu-list-score-exit.png) |
| 문제 풀이 | 6문제 전부 정답, 최고 점수 5→6점 | [04번](evidence/04-quiz-play-result.png) |
| 문제 추가 | Git 명령어 문제 1개 등록 | [05번](evidence/05-add-quiz.png) |
| 문제 목록 | 총 7개 확인 | [06번](evidence/06-seven-quiz-list.png) |
| 최고 점수 확인 | 6점 표시 | [07번](evidence/07-best-score.png) |
| 종료 후 재실행 | 7개 문제와 6점 유지 | [08번](evidence/08-reload-persistence.png) |
| 입력 오류·중단 | `abc`, `9`, 빈 입력 안내 및 `Ctrl+C` 안전 종료 | [10번](evidence/10-invalid-input-and-interrupt.png) |

**증거 구분:** 손상 JSON과 EOF는 자동 테스트로 검증했습니다. 실제로 사람이 직접 실행한 것처럼 기록하지 않습니다.

## 6. Git으로 작업한 과정

Git은 **PC에서 파일 변경 이력을 남기는 도구**, GitHub는 그 이력을 인터넷 저장소에 올려 공유하는 서비스입니다. **PC에 저장 → Git 커밋 → GitHub 업로드는 서로 다른 단계**입니다.

| 명령어 | 쉬운 뜻 | 이번 미션에서 수행한 일 |
| --- | --- | --- |
| `git init` | 새 Git 저장소를 시작 | 별도 `Quiz-Game-init-practice` 폴더에서 실행 |
| `git add` | 다음 커밋에 넣을 파일 선택 | 코드와 증빙 등록 |
| `git commit` | 변경한 작업을 PC 이력에 기록 | 기능·테스트·README를 별도 커밋으로 작성 |
| `git checkout` | 다른 브랜치로 이동 | `feature/quiz-game` → `main` |
| `git push` | GitHub로 커밋 업로드 | 완성된 프로그램과 증빙 전송 |
| `git clone` | GitHub 프로젝트를 복제 | `Quiz-Game-pull-practice` 폴더에 복제 |
| `git pull` | GitHub 변경을 PC에 내려받기 | 복제 폴더에서 수정·업로드한 README를 원본 폴더로 가져오기 |

**브랜치(Branch)**는 같은 프로젝트의 작업 이력을 나누는 줄기입니다. `feature/quiz-game`에서 만든 기능을 `main`으로 병합(`merge --no-ff`)하여 어떤 기능이 합쳐졌는지 기록했습니다. [병합 증빙](evidence/11-merge-execution.png) · [이력 그래프](evidence/12-final-git-history.png)

2026-11-12 GitHub `main`에서 **14개 커밋**을 확인했습니다(이번 개선 전 기준). 교육기관의 **최소 10개 이상** 조건을 충족합니다. 현재 값은 GitHub의 커밋 기록에서 확인하면 됩니다.

```bash
git log --oneline --graph -20
git status --short --branch
```

### 6-1. 커밋을 어떻게 나누고 메시지를 쓰나요? — 평가 보완 #12

**커밋 단위 원칙:** 하나의 기능이나 문서 작업을 마칠 때 한 번씩 기록합니다. 코드와 관련 없는 파일을 한 번에 모두 넣는 `git add .` 방식보다는 변경 대상을 확인해 필요한 파일만 선택합니다.

**커밋 메시지 규칙(앞부분 + 설명):**

```text
종류: 어떤 변경을 했는지 짧은 문장

Why: 변경한 이유 (필요할 때)
What: 바뀐 파일이나 기능 (필요할 때)
```

- `Feat:` 새 기능, `Fix:` 오류 수정, `Test:` 테스트 추가, `Docs:` README·증빙 수정, `Data:` 퀴즈 데이터 변경, `Merge:` 브랜치 병합을 뜻합니다.
- 첫 줄은 변경 내용을 구체적으로 쓰고, 이유가 더 필요할 때만 빈 줄 아래에 `Why:`·`What:`을 덧붙입니다. 모든 커밋에 긴 설명을 넣을 필요는 없습니다.
- **실제 Git 기록에 있는 예:** `Feat: implement four-choice Quiz class`, `Test: add quiz game automated tests`, `Docs: add final Git workflow evidence`, `Merge: integrate four-choice quiz game`.
- **앞으로 사용할 수 있는 형식 예시(실행 기록 아님):** `Fix: handle empty question input`.

이 방식은 평가자뿐 아니라 나중에 다시 프로젝트를 열었을 때 **무엇을 왜 수정했는지** 쉽게 파악하기 위한 규칙입니다.

### 6-2. 다른 폴더에서 변경 내용을 가져올 때

별도 복제 폴더에서 README를 수정해 `commit`·`push`한 다음, 원본 폴더에서 `git pull --ff-only origin main`을 실행하여 최신 내용을 가져왔습니다. `--ff-only`는 불필요한 새 병합 커밋을 만들지 않고 이어 붙일 수 있을 때만 갱신하는 옵션입니다.

**만약 pull이 거부된다면:** 먼저 `git status`로 PC에 수정된 파일이 있는지 확인하고, 파일을 보존한 상태에서 어떤 변경과 충돌하는지 살펴봅니다. 임의로 `reset --hard`를 실행하거나 파일을 지우지 않습니다.

## 7. 문제 1,000개 이상일 때는 어떨까요? — 평가 보완 #16

현재 실제 저장된 퀴즈는 **7개**입니다. 문제를 훨씬 많이 등록하는 상황을 가정하여, 원래 데이터를 건드리지 않는 **성능 측정 도구** `tests/benchmark_scale.py`를 별도로 준비했습니다.

**실행 위치: `Quiz-Game` 폴더의 Ubuntu(WSL) 터미널**

```bash
python3 tests/benchmark_scale.py
```

이 도구는 1,000개와 10,000개의 **시험용 문제**를 임시 폴더에 만든 뒤, 문제 생성, 마지막 문제 찾기(중복 검사와 같은 방식), JSON 저장·재불러오기 속도, 파일 크기, Python 메모리 사용량을 측정합니다. 실습용 `state.json`은 변경하지 않습니다.

### 실제 측정 결과 — 학습자 PC (2026-11-12)

**학습자 PC의 Ubuntu(WSL), Python 3.14.4 환경**에서 `python3 tests/benchmark_scale.py`를 실행했습니다. 아래 숫자는 **실제 터미널 출력**을 그대로 기록한 것으로, 다른 컴퓨터에서의 결과와 구분합니다. [실행 화면 확인](evidence/18-scale-benchmark.png)

| 시험 문제 수 | 문제 생성(초) | 마지막 문제 검색 1회(밀리초) | JSON 저장(초) | JSON 다시 불러오기(초) | 파일 크기(KiB) | Python 메모리 최고치(MiB) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1,000 | 0.0086 | 0.3493 | 0.0139 | 0.0038 | 254.9 | 1.83 |
| 10,000 | 0.0853 | 3.3944 | 0.1340 | 0.0414 | 2548.9 | 17.13 |

- **실제 확인:** 임시 파일에 저장하고 다시 읽었을 때 두 경우 모두 문제 수가 일치했습니다(`2/2`). 기존 제출 데이터인 `state.json`은 측정 도구에서 읽거나 수정하지 않습니다.
- **수치의 의미:** `0.3493ms`는 약 0.00035초입니다. 10,000문제에서 마지막 문제를 찾는 시간이 1,000문제보다 길어졌습니다. 검색 대상이 목록의 끝에 있기 때문입니다.
- **메모리 기준:** `tracemalloc`으로 추적한 측정 중 **Python 메모리 할당의 최고치**입니다. 컴퓨터 전체 RAM 사용량과는 다릅니다.
- **측정 한계:** 한 번의 측정값이며 저장장치·기기 성능 등에 따라 달라집니다. 사람이 퀴즈를 실제로 10,000문제 푸는 속도나 여러 사용자의 동시 사용 성능을 증명하는 시험은 아닙니다.

### 현재 프로그램의 한계와 개선 방향

| 작업 | 현재 방식 | 문제 수가 많을 때의 한계 | 필요해지면 고려할 개선 |
| --- | --- | --- | --- |
| 중복 질문 확인 | `add_quiz()`에서 목록을 하나씩 비교 | 문제 수에 비례해 검사량이 증가 | 정규화된 질문을 `set`으로 관리해 검색 속도 개선 |
| 저장·불러오기 | `save()`·`load()`에서 JSON 전체 처리 | 문제 수가 늘면 파일 크기와 처리 시간이 증가 | 변경 부분만 저장하는 DB 방식 검토 |
| 전체 목록·퀴즈 풀이 | `list_quizzes()`·`play()`에서 전부 순회 | 문제 수가 많으면 터미널 출력·풀이 시간이 너무 길어짐 | 페이지별 목록, 문제 수 선택·무작위 출제 기능 검토 |
| 여러 PC·사람의 동시 사용 | 하나의 JSON 파일 사용 | 동시에 수정하면 마지막 저장이 이전 변경을 덮을 수 있음 | 다중 사용자용 DB·동시 수정 제어 검토 |

**결론:** 현재 미션처럼 7개 문제를 한 사람이 사용하는 범위에는 충분하지만, 수천~수만 개 규모에서는 검색·전체 저장·화면 출력 방식의 개선을 검토해야 합니다. 이 개선 방향은 **향후 제안**이며 현재 코드에 이미 구현되었다는 뜻은 아닙니다.

**증빙 기록:** 학습자 PC에서 자동 테스트 11건 통과 및 성능 측정 결과를 같은 터미널에서 확인했습니다. 실제 화면을 `evidence/18-scale-benchmark.png`로 보관합니다. 이후 재측정 시에는 실행 환경과 측정값을 다시 확인해야 합니다.

## 8. 요구사항이 바뀌면 어디를 수정하나요? — 평가 보완 #18

어떤 기능이 바뀌었을 때 코드를 처음부터 다시 만들지 않고, **해당 파일과 메서드만 찾아 수정**하기 위한 표입니다.

| 바꾸고 싶은 기능 | 먼저 확인할 파일·위치 | 수정 후 확인할 방법 |
| --- | --- | --- |
| 시작·실행 방법 | `main.py`의 `main()` | `python3 main.py` 실행 |
| 메뉴 문구·메뉴 추가 | `game.py`의 `QuizGame.run()` | 실제 메뉴 선택 및 잘못된 번호 입력 확인 |
| 질문·보기 화면 | `quiz.py`의 `Quiz.show()` | 메뉴 1·3에서 출력 확인 |
| 정답 검증 규칙 | `quiz.py`의 `Quiz.__init__()`·`is_correct()` 및 `game.py`의 `read_number()` | `python3 -m unittest discover -s tests -v` |
| 게임 점수 계산 | `game.py`의 `play()`·`show_best_score()` | 전부 정답·오답 및 최고 점수 조회 테스트 |
| 새 문제 추가·중복 검사 | `game.py`의 `add_quiz()` | 같은 질문 입력·신규 문제 저장 후 재실행 |
| 기본 문제 수·내용 | `game.py`의 `DEFAULT_QUIZZES` | **새 임시 저장 파일로** 초기화 테스트. 기존 `state.json`에는 자동 반영되지 않음 |
| 저장 파일의 형식·저장 위치 | `game.py`의 `save()`·`load()` 및 `quiz.py`의 `to_dict()`·`from_dict()` | 임시 파일 저장·재불러오기 및 오류 복구 테스트 |
| 많은 문제의 처리 속도 | `game.py`의 `add_quiz()`·`list_quizzes()`·`save()`·`load()` | `python3 tests/benchmark_scale.py` |
| 자동 검증 항목 | `tests/test_quiz.py` | 테스트 11개를 재실행하고 결과 기록 |
| 안내문·증빙 연결 | `README.md`와 `evidence/` | GitHub에서 Markdown 링크 열기 |

**변경 순서:** (1) 무엇을 바꿀지 결정 → (2) 위 표에서 파일·함수 찾기 → (3) 필요한 부분만 수정 → (4) 자동 테스트 실행 → (5) 게임 직접 확인 → (6) `git status`로 변경 파일 확인 → (7) 기능 단위로 `commit`·`push`합니다.

**주의:** 변경 전에 기존 코드와 `state.json`을 보존하세요. 파일을 직접 삭제하거나 JSON 구조를 일방적으로 바꾸지 않습니다. 수정할 파일이 두 개 이상일 때는 데이터 저장·불러오기 쪽도 함께 점검해야 합니다.

## 9. 제출용 증빙사진 (기존 17장 + 성능 측정 1장)

각 링크를 누르면 GitHub의 실제 실행 화면을 확인할 수 있습니다. 사진은 **촬영 당시 상태**이므로 현재 커밋 개수와 다른 값이 보일 수 있습니다.

| 번호 | 증명하는 내용 | 파일 |
| :---: | --- | --- |
| 01 | 작업 브랜치 생성 | [01-git-branch.png](evidence/01-git-branch.png) |
| 02 | 자동 테스트 11개 통과 | [02-automatic-tests.png](evidence/02-automatic-tests.png) |
| 03 | 메뉴·문제 목록·종료 | [03-menu-list-score-exit.png](evidence/03-menu-list-score-exit.png) |
| 04 | 문제 풀이·점수 | [04-quiz-play-result.png](evidence/04-quiz-play-result.png) |
| 05 | 새 문제 추가 | [05-add-quiz.png](evidence/05-add-quiz.png) |
| 06 | 전체 문제 7개 확인 | [06-seven-quiz-list.png](evidence/06-seven-quiz-list.png) |
| 07 | 최고 점수 6점 확인 | [07-best-score.png](evidence/07-best-score.png) |
| 08 | 종료 후 문제·점수 유지 | [08-reload-persistence.png](evidence/08-reload-persistence.png) |
| 09 | Python 및 Git 버전 | [09-environment.png](evidence/09-environment.png) |
| 10 | 잘못된 입력·Ctrl+C 안전 종료 | [10-invalid-input-and-interrupt.png](evidence/10-invalid-input-and-interrupt.png) |
| 11 | 브랜치 병합 | [11-merge-execution.png](evidence/11-merge-execution.png) |
| 12 | 커밋 그래프 | [12-final-git-history.png](evidence/12-final-git-history.png) |
| 13 | GitHub에 push | [13-github-push-success.png](evidence/13-github-push-success.png) |
| 14 | 저장소 clone | [14-clone-practice.png](evidence/14-clone-practice.png) |
| 15 | 변경 사항 pull | [15-pull-success.png](evidence/15-pull-success.png) |
| 16 | git init 실행 | [16-git-init-execution.png](evidence/16-git-init-execution.png) |
| 17 | 초기화 상태 확인 | [17-git-init-status.png](evidence/17-git-init-status.png) |

| 18 | 학습자 PC 자동 테스트 및 1,000·10,000문제 성능 측정 | [18-scale-benchmark.png](evidence/18-scale-benchmark.png) |

**증빙 구분:** 01~17번은 이미 GitHub에 등록된 기존 자료입니다. 18번은 **이번 개선에서 추가할 사용자 PC 실행 화면**이며, GitHub 반영은 아직 확인되지 않았습니다.

## 10. 제출 전 확인표

- [x] Python으로 동작하는 4지선다 퀴즈 게임 구현
- [x] 기본 문제 6개 및 문제 추가·조회·점수·종료 기능 확인
- [x] 클래스 2개 및 역할별 메서드 분리
- [x] JSON 저장·불러오기·손상 복구·입력 오류 처리
- [x] 자동 테스트 11건 통과 및 수동 실행 증빙 확보
- [x] Git 커밋 10개 이상, 브랜치 생성·병합, 필수 명령어 7종
- [x] GitHub에 기존 코드와 증빙사진 17장 업로드
- [x] 커밋 메시지 규칙과 기능 변경 위치를 문서에 설명 (**이번 개선본에 반영**)
- [x] 학습자 PC에서 1,000·10,000문제 성능을 실제 측정하고 데이터 유지 여부 확인
- [x] 새 `tests/benchmark_scale.py`와 수정 README를 사용자 PC에 적용하고 기존 자동 테스트 11건 재확인
- [ ] 수정 README·측정 도구·18번 증빙을 GitHub에 업로드하고 확인
- [x] 학습자 PC 성능 측정 화면 확보(18번 자료로 준비)
- [ ] **교육 플랫폼에 GitHub 주소·요구 제출물을 실제로 등록하고 접수 여부 확인**

**제출할 저장소:** https://github.com/whlee5125740-afk/Quiz-Game

> **현재 상태:** 기존 프로그램과 Git 필수 실습은 검증했습니다. 이번 사전평가 보완은 개선 파일을 준비한 상태이며, **학습자 PC에서 검증은 완료했으나 GitHub 업로드·재평가 및 교육 플랫폼 제출은 아직 완료로 표시하지 않습니다.**
