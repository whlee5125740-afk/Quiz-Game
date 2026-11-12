# 나만의 4지선다 퀴즈 게임 (Quiz-Game)

> **AI 올인원 교육 과정 | 미션: 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기**

## 한눈에 보는 프로젝트

이 프로젝트는 **Python을 처음 배우는 비전공자**가 직접 만든 **터미널(명령어 입력 화면)용 4지선다 퀴즈 게임**입니다. 배운 내용을 실제 프로그램에 적용하고, Git으로 작업 과정을 기록하는 것이 목표입니다.

- **퀴즈 주제:** Python 기초 문법과 Git 명령어
- **주제를 선택한 이유:** 새로 배우는 `print()`, `input()`, 조건문, 반복문, Git 명령어를 문제로 풀면서 복습하기 위해서입니다.
- **주요 기능:** 퀴즈 풀기, 문제 추가, 문제 목록, 최고 점수 조회, 종료 후 데이터 유지
- **프로그램 구성:** `Quiz`와 `QuizGame`, 총 **2개의 클래스**
- **저장 방식:** `state.json` 파일에 문제와 최고 점수를 보관
- **검증 결과:** 자동 테스트 11건 통과, 실제 퀴즈 풀이 및 재실행 확인
- **Git 작업:** 커밋 **10개 이상** 조건 충족(2026-11-12 GitHub에서 13개 확인), 브랜치 생성·병합 및 필수 명령어 7종 실습
- **증빙자료:** [`evidence/` 폴더의 실행 화면 17장](evidence/)

**현재 상태(2026-11-12):** 프로그램·Git 실습·GitHub 자료 업로드까지 확인했습니다. **교육 플랫폼에 실제로 제출했는지는 아직 확인하지 않았습니다.**

---

## 1. 무엇을 할 수 있는 프로그램인가요?

게임을 실행하면 아래 5개 메뉴가 나옵니다.

| 메뉴 번호 | 기능 | 사용자가 하는 일 |
| :---: | --- | --- |
| 1 | 퀴즈 풀기 | 각 문제의 보기 4개 중 정답 번호(1~4)를 선택합니다. |
| 2 | 퀴즈 추가 | 문제와 보기 4개, 정답 번호를 입력해 새 문제를 저장합니다. |
| 3 | 퀴즈 목록 | 지금까지 등록된 문제와 정답을 확인합니다. |
| 4 | 최고 점수 확인 | 가장 많이 맞혔을 때의 점수와 문제 수를 확인합니다. |
| 5 | 종료 | 프로그램을 종료합니다. 저장한 데이터는 다음 실행에도 유지됩니다. |

실제로 기본 문제 6개로 시작해 새로운 문제 1개를 추가했고, 이후 **7개 문제와 최고 점수 6점**이 유지되는 것을 확인했습니다. 이는 실습 당시의 결과이며 사용 후에는 값이 달라질 수 있습니다.

## 2. 어떻게 실행하나요?

### 필요한 환경

- **Python 3.10 이상:** 코드를 실행하는 프로그램입니다. 실제 실습 PC에서는 **Python 3.14.4**를 확인했습니다.
- **Git:** 파일 변경 이력을 기록하고 GitHub와 연결하는 도구입니다. 실제 확인 버전은 **Git 2.53.0**입니다.
- **터미널:** Ubuntu(WSL) 또는 Python이 설치된 Windows 터미널을 사용할 수 있습니다.
- **추가 설치 패키지:** 없음. Python에 기본 포함된 기능만 사용합니다.

실습 환경 확인 화면: [09-environment.png](evidence/09-environment.png)

### 처음 GitHub에서 내려받는 경우

**실행 위치: Ubuntu(WSL) 터미널**, 프로젝트를 저장하려는 상위 폴더에서 실행합니다.

```bash
git clone https://github.com/whlee5125740-afk/Quiz-Game.git
cd Quiz-Game
python3 main.py
```

명령어의 뜻은 다음과 같습니다.

1. `git clone`: GitHub에 있는 프로젝트를 내 PC로 복사합니다.
2. `cd Quiz-Game`: 복사된 프로젝트 폴더로 이동합니다.
3. `python3 main.py`: 퀴즈 게임을 시작합니다.

이미 PC에 `Quiz-Game` 폴더가 있다면 **다시 복제하지 말고 그 폴더에서** 다음 명령만 실행합니다.

```bash
python3 main.py
```

Windows PowerShell에서는 설치 환경에 따라 `python main.py`를 사용할 수도 있습니다.

**정상 실행 확인:** 메뉴 1~5번이 화면에 나타나면 시작된 것입니다. `5`를 입력하고 Enter를 누르면 종료됩니다.

> **주의:** 게임에서 퀴즈를 추가하거나 최고 점수를 갱신하면 `state.json`이 수정될 수 있습니다. 제출 파일을 유지하려면 실행 전후 `git status`로 변경 여부를 확인하세요.

## 3. 어떤 파일이 어떤 일을 하나요?

```text
Quiz-Game/
├── main.py             # 프로그램 시작
├── quiz.py             # Quiz 클래스: 문제 하나를 관리
├── game.py             # QuizGame 클래스: 메뉴·게임·점수·저장 관리
├── state.json          # 문제 목록과 최고 점수 저장
├── tests/
│   └── test_quiz.py    # 자동 테스트 11개
├── evidence/           # 실제 실습 화면 17장
├── README.md           # 프로젝트 설명 및 실행 안내
└── .gitignore          # Git에 올리지 않을 임시 파일 안내
```

**클래스(Class)**는 관련 데이터와 기능을 묶어 놓는 코드의 구성 단위입니다. **메서드(Method)**는 클래스 안에 정의된 기능입니다.

| 파일 | 쉬운 설명 | 실제 코드의 주요 기능 |
| --- | --- | --- |
| `main.py` | 프로그램을 시작하는 곳 | `main()`에서 `QuizGame` 실행 |
| `quiz.py` | 문제 한 개를 관리하는 곳 | `Quiz`: 질문·보기·정답 저장, 문제 출력, 정답 확인 |
| `game.py` | 게임 전체를 진행하는 곳 | `QuizGame`: 메뉴 표시, 문제 풀기·추가, 점수 계산, 파일 저장·불러오기 |
| `state.json` | 실행이 끝나도 남는 데이터 파일 | 퀴즈 목록 `quizzes`와 최고 점수 `best_score` 보관 |
| `tests/test_quiz.py` | 프로그램이 제대로 작동하는지 자동 확인 | 문제 검증, 저장·불러오기, 잘못된 입력, 안전한 종료 등 11개 테스트 |

코드에서 사용한 기본 문법도 실제 용도와 연결했습니다.

- **변수:** 문제 목록과 최고 점수처럼 실행 중 필요한 값을 기억합니다.
- **자료형:** `str`(글자), `int`(정수), `bool`(참·거짓), `list`(목록), `dict`(이름과 값의 묶음)를 사용합니다.
- **`if / elif / else`:** 선택한 메뉴 번호에 따라 다른 기능을 실행합니다.
- **`while`:** 사용자가 종료할 때까지 메뉴를 반복해서 보여 줍니다.
- **`for`:** 저장된 문제를 하나씩 순서대로 출력하거나 풉니다.
- **`__init__`, `self`:** 객체를 만들 때 초기 값을 준비하고 그 객체의 데이터를 가리키는 데 사용합니다.
- **`try / except`:** 잘못된 파일이나 중단 입력 등 오류 상황에서 프로그램이 갑자기 끝나지 않게 처리합니다.

## 4. 문제와 점수는 어떻게 보관하나요?

**JSON**은 데이터를 글자 형태로 저장하는 방식입니다. `state.json`은 프로젝트 최상위 폴더에 있으며 UTF-8 형식으로 읽고 씁니다.

아래는 **구조를 이해하기 위한 축약 예시**입니다. 실제 파일 전체를 그대로 옮긴 것은 아닙니다.

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

- `quizzes`: 문제 전체 목록
- `question`: 문제 내용
- `choices`: 4개의 선택지
- `answer`: 정답 번호(1~4)
- `best_score`: 지금까지 가장 많이 맞힌 **문제 개수**

**저장과 복구 흐름:**

1. `state.json`이 있으면 저장된 문제와 점수를 불러옵니다.
2. 파일이 처음부터 없으면 기본 문제 6개로 시작해 새 파일을 만듭니다.
3. 문제를 추가하거나 최고 점수가 올라가면 변경된 데이터를 저장합니다.
4. 파일 형식이 손상됐다면 가능한 경우 손상된 원본을 `.bak` 파일로 보관한 뒤 기본 문제로 복구합니다.

손상 파일 복구 기능은 **자동 테스트로 검증**했습니다. 실제 저장 파일을 임의로 손상시키는 수동 실습을 했다고 기록하지는 않습니다.

## 5. 제대로 작동하는지 어떻게 확인했나요?

### ① 자동 테스트

**실행 위치:** `Quiz-Game` 폴더의 Ubuntu(WSL) 터미널

```bash
python3 -m unittest discover -s tests -v
```

- `python3 -m unittest`: Python에 기본 포함된 자동 테스트 기능 실행
- `discover -s tests`: `tests` 폴더에서 테스트 코드를 찾기
- `-v`: 테스트별 결과를 자세히 출력하기

**실제 실행 결과(2026-11-11):**

```text
Ran 11 tests in 0.003s

OK
```

11개 테스트에는 문제 데이터 검증, JSON 파일 생성·저장·복구, 문제 추가와 중복 차단, 빈 문제 목록, 잘못된 메뉴 입력, `Ctrl+C` 및 입력 종료(EOF), 최고 점수 갱신 등이 포함됩니다. 자동 테스트는 **임시 폴더**를 사용하므로 실제 `state.json`을 직접 바꾸지 않습니다.

증빙: [02-automatic-tests.png](evidence/02-automatic-tests.png)

### ② 사람이 직접 실행한 확인

| 직접 해본 작업 | 확인 결과 | 증빙 |
| --- | --- | --- |
| 메뉴와 문제 목록 보기 | 메뉴 1~5, 기본 문제 6개와 보기 확인 | [03번](evidence/03-menu-list-score-exit.png) |
| 퀴즈 풀기 | 6문제 모두 맞혀 6점 기록 | [04번](evidence/04-quiz-play-result.png) |
| 퀴즈 추가하기 | Git 관련 문제 1개 추가 | [05번](evidence/05-add-quiz.png) |
| 문제 목록 다시 확인 | 총 7문제로 증가 | [06번](evidence/06-seven-quiz-list.png) |
| 최고 점수 확인 | 최고 점수 6점 | [07번](evidence/07-best-score.png) |
| 종료 후 다시 실행 | 문제 7개와 최고 점수 6점 유지 | [08번](evidence/08-reload-persistence.png) |
| 문자 `abc`, 숫자 `9`, 빈 입력 | 오류 안내 후 다시 입력받음 | [10번](evidence/10-invalid-input-and-interrupt.png) |
| `Ctrl+C`로 입력 중단 | 안내 메시지를 출력하고 안전하게 종료 | [10번](evidence/10-invalid-input-and-interrupt.png) |

**결과를 구분해 기록했습니다:** 직접 실행한 화면은 수동 실습 증거이고, 자동으로 검사한 기능은 자동 테스트 증거입니다. 둘을 동일한 실습 기록으로 취급하지 않았습니다.

## 6. Git으로 작업한 과정

Git은 **PC의 파일 변경 이력을 기록하는 도구**, GitHub는 **그 이력을 인터넷 저장소에 올리고 확인하는 서비스**입니다.

| 명령어 | 쉬운 뜻 | 이번 미션에서 한 일 |
| --- | --- | --- |
| `git init` | 새 Git 저장소 시작 | 별도의 `Quiz-Game-init-practice` 폴더에서 실습 |
| `git add` | 커밋할 파일 선택 | 작성한 코드와 증빙자료를 등록 |
| `git commit` | 변경 이력을 PC에 기록 | 클래스, 게임 진행, 테스트, 문서 등을 작업별 기록 |
| `git checkout` | 다른 브랜치로 이동 | `feature/quiz-game`에서 `main`으로 이동 |
| `git push` | PC의 커밋을 GitHub로 보내기 | 완료한 프로그램과 증빙 업로드 |
| `git clone` | GitHub 프로젝트를 복제하기 | 별도 `Quiz-Game-pull-practice` 폴더 생성 |
| `git pull` | GitHub 변경을 PC에 가져오기 | 복제 폴더에서 수정한 README를 원본 폴더에 반영 |

**브랜치(Branch)**는 같은 프로젝트 안에서 변경 작업을 구분하는 Git의 작업 줄기입니다. `feature/quiz-game`에서 기능을 만들고 `main`으로 **병합(Merge)**했습니다.

**PC 저장, 커밋, GitHub 업로드는 서로 다릅니다.** 파일을 저장했다고 커밋된 것은 아니며, 커밋했다고 GitHub에 자동으로 올라가는 것도 아닙니다.

최종 확인 당시 GitHub `main`의 **커밋 13개(2026-11-12, 이 README 개선 작업 전)**를 확인했습니다. 최소 10개 이상 조건을 충족했습니다.

커밋 이력 확인 명령:

```bash
git log --oneline --graph -15
git status --short --branch
```

참고: GitHub 업로드 중 이메일 공개 보호 오류(GH007)가 발생했지만, 비공개용 `noreply` 이메일을 사용하여 해결했습니다. 인증 토큰·비밀번호는 코드, 문서, 증빙에 포함하지 않습니다.

## 7. 제출 증빙사진 (17장)

다음 링크를 선택하면 GitHub에서 해당 실습 화면을 열어볼 수 있습니다. 각 이미지는 **실행 당시의 화면**으로, 현재 커밋 번호와 다른 과거 기록이 보일 수 있습니다.

| 번호 | 무엇을 확인할 수 있나요? | 파일 |
| :---: | --- | --- |
| 01 | 작업 브랜치 생성 | [01-git-branch.png](evidence/01-git-branch.png) |
| 02 | 자동 테스트 11개 통과 | [02-automatic-tests.png](evidence/02-automatic-tests.png) |
| 03 | 메뉴·문제 목록·종료 | [03-menu-list-score-exit.png](evidence/03-menu-list-score-exit.png) |
| 04 | 퀴즈 풀이 및 점수 | [04-quiz-play-result.png](evidence/04-quiz-play-result.png) |
| 05 | 문제 추가 | [05-add-quiz.png](evidence/05-add-quiz.png) |
| 06 | 문제 7개 목록 | [06-seven-quiz-list.png](evidence/06-seven-quiz-list.png) |
| 07 | 최고 점수 조회 | [07-best-score.png](evidence/07-best-score.png) |
| 08 | 재실행 후 데이터 유지 | [08-reload-persistence.png](evidence/08-reload-persistence.png) |
| 09 | Python·Git 버전 확인 | [09-environment.png](evidence/09-environment.png) |
| 10 | 잘못된 입력과 `Ctrl+C` 처리 | [10-invalid-input-and-interrupt.png](evidence/10-invalid-input-and-interrupt.png) |
| 11 | 작업 브랜치 병합 | [11-merge-execution.png](evidence/11-merge-execution.png) |
| 12 | Git 커밋 이력 그래프 | [12-final-git-history.png](evidence/12-final-git-history.png) |
| 13 | GitHub 업로드 성공 | [13-github-push-success.png](evidence/13-github-push-success.png) |
| 14 | GitHub 저장소 복제 | [14-clone-practice.png](evidence/14-clone-practice.png) |
| 15 | 변경 사항 `pull` 성공 | [15-pull-success.png](evidence/15-pull-success.png) |
| 16 | 별도 폴더의 `git init` 실행 | [16-git-init-execution.png](evidence/16-git-init-execution.png) |
| 17 | 새 Git 저장소의 상태 확인 | [17-git-init-status.png](evidence/17-git-init-status.png) |

모든 사진 파일이 GitHub의 [`evidence/` 폴더](evidence/)에 등록된 것을 확인했습니다.

## 8. 최종 제출 점검표

- [x] Python으로 동작하는 4지선다 퀴즈 프로그램 완성
- [x] 기본 퀴즈 5개 이상 작성 및 새 문제 추가 기능 확인
- [x] 2개 클래스(`Quiz`, `QuizGame`)와 기능별 메서드 구현
- [x] `state.json` 저장·불러오기 및 데이터 유지 검증
- [x] 잘못된 입력·안전한 종료·손상 파일 복구 처리 확인(자동/수동 구분)
- [x] Python 3.10 이상 환경 및 자동 테스트 11개 통과
- [x] Git 커밋 10개 이상, 작업 브랜치 생성·병합
- [x] Git 기본 명령어 7종 실습
- [x] GitHub에 프로그램 코드·README·증빙 17장 업로드
- [ ] **교육 플랫폼에 GitHub 저장소 주소 및 요구 제출물을 실제 제출하고 접수 여부 확인**

**제출용 GitHub 주소:** https://github.com/whlee5125740-afk/Quiz-Game

> **최종 상태:** 프로그램과 Git 실습 및 GitHub 자료 준비까지 확인했습니다. **교육 플랫폼 제출 완료 및 평가 통과는 아직 확인되지 않았습니다.**
