from some_model import SomeModel


def predict_message_mood(
    message,
    model,
    bad_thresholds=0.3,
    good_thresholds=0.8,
):
    logit = model.predict(message)
    if logit <= bad_thresholds:
        return "неуд"
    if logit > good_thresholds:
        return "отл"
    return "норм"


if __name__ == "__main__":
    model = SomeModel()
    assert predict_message_mood("Чапаев и пустота", model) == "норм"
