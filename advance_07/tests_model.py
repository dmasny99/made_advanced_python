import unittest
from unittest.mock import patch, call
from predict_mood import predict_message_mood


class TestSomeModel(unittest.TestCase):

    def setUp(self):
        print("Imitates that model is loaded")

    def test_model_pred(self):
        with patch("predict_mood.SomeModel") as mocked_model:
            texts = [
                "threat death",
                "python python python",
                "good love kind",
                "hate kill pain",
                "  ",
                "friend friendship",
                "Чапаев и пустота",
                ]
            scores = [0.28, 0.5, 1, 0.1, 0.32, 0.84, 0.81]
            results = ["неуд", "норм", "отл", "неуд", "норм", "отл", "отл"]
            mocked_model.predict.side_effect = scores
            for idx, text in enumerate(texts):
                self.assertEqual(
                    predict_message_mood(text, mocked_model),
                    results[idx])

    def test_model_calls(self):
        with patch("predict_mood.SomeModel") as mocked_model:
            texts = [
                "threat death",
                "python python python",
                "good love kind",
                "hate kill pain",
                "  ",
                "friend friendship",
                "Чапаев и пустота",
                ]
            scores = [0.28, 0.5, 1, 0.1, 0.32, 0.84, 0.81]
            mocked_model.predict.side_effect = scores
            for _, text in enumerate(texts):
                predict_message_mood(text, mocked_model)
                self.assertEqual(
                    mocked_model.predict.call_args,
                    call(text))

    def test_border_scores(self):
        eps = 0.001
        with patch("predict_mood.SomeModel") as mocked_model:
            texts = [
                "txt 1",
                "txt 2",
                "txt 3",
                "txt 4",
                "txt 5",
                "txt 6",
                ]
            scores = [0.3 + eps, 0.3 - eps, 0.8 - eps, 0.8, 0.8 + eps, 1]
            results = ["норм", "неуд", "норм", "норм", "отл", "отл"]
            mocked_model.predict.side_effect = scores
            for idx, text in enumerate(texts):
                self.assertEqual(
                    predict_message_mood(text, mocked_model),
                    results[idx])


if __name__ == "__main__":
    unittest.main()
