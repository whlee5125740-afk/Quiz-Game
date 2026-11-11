"""표준 라이브러리 unittest로 실행하는 자동 테스트."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from quiz import Quiz
from game import QuizGame


class QuizTests(unittest.TestCase):
    def test_four_choices_and_answer(self):
        quiz = Quiz("문제", ["가", "나", "다", "라"], 2)
        self.assertTrue(quiz.is_correct(2))
        self.assertFalse(quiz.is_correct(1))
        self.assertEqual(quiz.to_dict()["answer"], 2)

    def test_reject_bad_question_data(self):
        with self.assertRaises(ValueError):
            Quiz("", ["가", "나", "다", "라"], 2)
        with self.assertRaises(ValueError):
            Quiz("문제", ["가", "나"], 2)
        with self.assertRaises(ValueError):
            Quiz("문제", ["가", "나", "다", "라"], 5)


class GameTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.path = Path(self.tempdir.name) / "state.json"
        with contextlib.redirect_stdout(io.StringIO()):
            self.game = QuizGame(self.path)

    def test_missing_file_creates_six_quizzes(self):
        self.assertEqual(len(self.game.quizzes), 6)
        self.assertTrue(self.path.exists())
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8"))["best_score"], 0)

    def test_save_and_reload(self):
        self.game.best_score = 3
        self.game.save()
        with contextlib.redirect_stdout(io.StringIO()):
            another = QuizGame(self.path)
        self.assertEqual(another.best_score, 3)
        self.assertEqual(len(another.quizzes), 6)

    def test_bad_json_is_preserved_then_recovered(self):
        self.path.write_text("{broken", encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            recovered = QuizGame(self.path)
        self.assertEqual(len(recovered.quizzes), 6)
        self.assertTrue(list(self.path.parent.glob("state.corrupt-*.bak")))

    def test_empty_quiz_list(self):
        self.game.quizzes = []
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.game.play()
            self.game.list_quizzes()
        self.assertIn("등록된 퀴즈가 없습니다", out.getvalue())

    def test_menu_invalid_then_exit(self):
        with patch("builtins.input", side_effect=["", "abc", "9", "5"]):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.game.run()
        self.assertIn("숫자를 입력하세요", out.getvalue())
        self.assertIn("게임을 종료합니다", out.getvalue())

    def test_ctrl_c_and_eof_stop_safely(self):
        for error in (KeyboardInterrupt, EOFError):
            with self.subTest(error=error):
                with patch("builtins.input", side_effect=error):
                    out = io.StringIO()
                    with contextlib.redirect_stdout(out):
                        self.game.run()
                self.assertIn("안전하게 종료", out.getvalue())

    def test_add_quiz_then_reload(self):
        answers = ["새 문제", "가", "나", "다", "라", "4"]
        with patch("builtins.input", side_effect=answers):
            with contextlib.redirect_stdout(io.StringIO()):
                self.game.add_quiz()
        with contextlib.redirect_stdout(io.StringIO()):
            another = QuizGame(self.path)
        self.assertEqual(len(another.quizzes), 7)
        self.assertEqual(another.quizzes[-1].answer, 4)

    def test_duplicate_question_not_added(self):
        with patch("builtins.input", return_value=self.game.quizzes[0].question):
            with contextlib.redirect_stdout(io.StringIO()):
                self.game.add_quiz()
        self.assertEqual(len(self.game.quizzes), 6)

    def test_play_all_correct_updates_high_score(self):
        answers = [str(q.answer) for q in self.game.quizzes]
        with patch("builtins.input", side_effect=answers):
            with contextlib.redirect_stdout(io.StringIO()):
                self.game.play()
        self.assertEqual(self.game.best_score, 6)
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8"))["best_score"], 6)


if __name__ == "__main__":
    unittest.main()
