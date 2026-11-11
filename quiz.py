"""한 개의 4지선다 퀴즈 문제를 나타내는 클래스."""


class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 비어 있을 수 없습니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")
        if any(not isinstance(c, str) or not c.strip() for c in choices):
            raise ValueError("선택지는 비어 있을 수 없습니다.")
        if type(answer) is not int or answer not in (1, 2, 3, 4):
            raise ValueError("정답 번호는 1~4 사이의 정수여야 합니다.")
        self.question = question.strip()
        self.choices = [c.strip() for c in choices]
        self.answer = answer

    def show(self, number: int) -> None:
        print(f"\n[문제 {number}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def is_correct(self, selection: int) -> bool:
        return selection == self.answer

    def to_dict(self) -> dict:
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        if not isinstance(data, dict):
            raise ValueError("퀴즈 데이터가 객체 형식이 아닙니다.")
        return cls(data.get("question"), data.get("choices"), data.get("answer"))
