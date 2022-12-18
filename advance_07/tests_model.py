import pytest
from unittest import mock
from predict_mood import predict_message_mood
from some_model import SomeModel


# at fisrt test real model
@pytest.fixture
def get_model():
    model = SomeModel()
    return model


def test_model_load(get_model):
    assert isinstance(get_model, SomeModel)
    assert "predict" in dir(get_model)
    with pytest.raises(AttributeError):
        get_model.train()


@pytest.mark.parametrize(
    "message, expected",
    [
        ("python python python", "отл"),
        ("p p p p p p p p p p", "неуд"),
        (" ", "отл"),
        ("good", "норм"),
        ("bad", "норм"),
        ("neutral", "отл")
    ],
)
def test_predict_message_mood(get_model, message, expected):
    assert predict_message_mood(message, get_model) == expected


# then test model with mocks
@pytest.fixture
def get_synt_model():
    return {"Model loaded": True}


def test_synt_model_load(get_synt_model):
    assert isinstance(get_synt_model, dict)
    assert get_synt_model["Model loaded"] is True
    with pytest.raises(KeyError):
        get_synt_model.get("invalid key")


@pytest.mark.parametrize(
    "message, expected",
    [
        ("python python python", "отл"),
        ("p p p p p p p p p p", "неуд"),
        (" ", "отл"),
        ("good", "норм"),
        ("bad", "норм"),
        ("neutral", "отл")
    ],
)
def test_synt_pred(message, expected):
    with mock.patch("predict_mood.SomeModel.predict") as mpred:
        mpred.return_value = expected
        assert mpred(message) == expected
