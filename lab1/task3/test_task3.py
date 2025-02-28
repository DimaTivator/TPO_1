import pytest
from task3_fixture import human
from task3 import *


@pytest.mark.parametrize(
    "expected_name, expected_speech, expected_pause, expected_intonation, expected_timbre",
    [
        ("Марвин", Speech(Pause(0.5), Intonation(5), Timbre(2)), 0.5, 5, 2)
    ]
)
def test_human_creation(human, expected_name, expected_speech, expected_pause, expected_intonation, expected_timbre):
    assert human.name == expected_name
    assert isinstance(human.speech, Speech)
    assert human.speech.pause.duration == expected_pause
    assert human.speech.intonation.level == expected_intonation
    assert human.speech.timbre.quality == expected_timbre


@pytest.mark.parametrize(
    "emotion_name, expected_pause, expected_intonation, expected_timbre",
    [
        ("презрение", 1.0, 2, 3),
        ("ужас", 0.1, 8, 1)
    ]
)
def test_express_emotion(human, emotion_name, expected_pause, expected_intonation, expected_timbre):
    human.express_emotion(emotion_name)
    assert emotion_name in [e.name for e in human.emotions]

    assert human.speech.pause.duration == expected_pause
    assert human.speech.intonation.level == expected_intonation
    assert human.speech.timbre.quality == expected_timbre

@pytest.mark.parametrize(
    "emotion_name",
    [
        ("счастье"),
        ("грусть")
    ]
)
def test_express_invalid_emotion(human, emotion_name):
    with pytest.raises(ValueError, match="Неизвестная эмоция"):
        human.express_emotion(emotion_name)

@pytest.mark.parametrize(
    "emotion_name, intensity",
    [
        ("гнев", 11),
        ("страх", -1)
    ]
)
def test_invalid_emotion_intensity(emotion_name, intensity):
    with pytest.raises(ValueError):
        Emotion(emotion_name, intensity)

@pytest.mark.parametrize(
    "emotion_name, expected_intensity",
    [
        ("презрение", 10),
        ("ужас", 10)
    ]
)
def test_get_emotion_intensity(human, emotion_name, expected_intensity):
    human.express_emotion(emotion_name)
    assert human.get_emotion_intensity(emotion_name) == expected_intensity


@pytest.mark.parametrize(
    "quality",
    [
        4,
        -1
    ]
)
def test_invalid_timbre_quality(quality):
    with pytest.raises(ValueError):
        Timbre(quality)

@pytest.mark.parametrize(
    "new_pause, expected_duration",
    [
        (Pause(2.0), 2.0)
    ]
)
def test_modify_pause(human, new_pause, expected_duration):
    human.speech.modify_pause(new_pause)
    assert human.speech.pause.duration == expected_duration


@pytest.mark.parametrize(
    "new_intonation, expected_level",
    [
        (Intonation(6), 6)
    ]
)
def test_modify_intonation(human, new_intonation, expected_level):
    human.speech.modify_intonation(new_intonation)
    assert human.speech.intonation.level == expected_level


@pytest.mark.parametrize(
    "new_timbre, expected_quality",
    [
        (Timbre(1), 1)
    ]
)
def test_modify_timbre(human, new_timbre, expected_quality):
    human.speech.modify_timbre(new_timbre)
    assert human.speech.timbre.quality == expected_quality
