import pytest

from test_task3 import *


@pytest.fixture
def human():
    h = Human("Марвин")
    speech = Speech(Pause(0.5), Intonation(5), Timbre(2))
    h.set_speech(speech)
    return h

def test_express_contempt(human):
    """Проверка выражения презрения: пауза, интонация, тембр."""
    human.express_contempt()
    assert "презрение" in [e.name for e in human.emotions]
    assert human.speech.pause.duration == 1.0
    assert human.speech.intonation.level == 2
    assert human.speech.timbre.quality == 3

def test_express_terror(human):
    """Проверка выражения ужаса: пауза, интонация, тембр."""
    human.express_terror()
    assert "ужас" in [e.name for e in human.emotions]
    assert human.speech.pause.duration == 0.1
    assert human.speech.intonation.level == 8
    assert human.speech.timbre.quality == 1

def test_invalid_emotion_intensity():
    """Ошибка при недопустимой интенсивности эмоции."""
    with pytest.raises(ValueError):
        Emotion("гнев", 11)
    with pytest.raises(ValueError):
        Emotion("страх", -1)

def test_get_emotion_intensity(human):
    """Получение интенсивности эмоции."""
    human.express_contempt()
    assert human.get_emotion_intensity("презрение") == 10
    assert human.get_emotion_intensity("радость") == 0

def test_invalid_timbre_quality():
    """Проверка недопустимых значений для качества тембра."""
    with pytest.raises(ValueError):
        Timbre(4)  # Значение больше 3
    with pytest.raises(ValueError):
        Timbre(-1)  # Значение меньше 0

def test_modify_pause(human):
    """Проверка изменения паузы в речи."""
    new_pause = Pause(2.0)
    human.speech.modify_pause(new_pause)
    assert human.speech.pause.duration == 2.0

def test_modify_intonation(human):
    """Проверка изменения интонации в речи."""
    new_intonation = Intonation(6)
    human.speech.modify_intonation(new_intonation)
    assert human.speech.intonation.level == 6

def test_modify_timbre(human):
    """Проверка изменения тембра в речи."""
    new_timbre = Timbre(1)
    human.speech.modify_timbre(new_timbre)
    assert human.speech.timbre.quality == 1
