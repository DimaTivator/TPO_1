import pytest

from task3 import *

@pytest.fixture
def human():
    h = Human("Марвин")
    speech = Speech(Pause(0.5), Intonation(5), Timbre(2))
    h.set_speech(speech)
    return h

def test_express_contempt(human):
    human.express_contempt()
    assert "презрение" in [e.name for e in human.emotions]
    assert human.speech.pause.duration == 1.0
    assert human.speech.intonation.level == 2
    assert human.speech.timbre.quality == 3

def test_express_terror(human):
    human.express_terror()
    assert "ужас" in [e.name for e in human.emotions]
    assert human.speech.pause.duration == 0.1
    assert human.speech.intonation.level == 8
    assert human.speech.timbre.quality == 1

def test_invalid_emotion_intensity():
    with pytest.raises(ValueError):
        Emotion("гнев", 11)
    with pytest.raises(ValueError):
        Emotion("страх", -1)

def test_get_emotion_intensity(human):
    human.express_contempt()
    assert human.get_emotion_intensity("презрение") == 10
    assert human.get_emotion_intensity("радость") == 0

def test_invalid_timbre_quality():
    with pytest.raises(ValueError):
        Timbre(4)
    with pytest.raises(ValueError):
        Timbre(-1)

def test_modify_pause(human):
    new_pause = Pause(2.0)
    human.speech.modify_pause(new_pause)
    assert human.speech.pause.duration == 2.0

def test_modify_intonation(human):
    new_intonation = Intonation(6)
    human.speech.modify_intonation(new_intonation)
    assert human.speech.intonation.level == 6

def test_modify_timbre(human):
    new_timbre = Timbre(1)
    human.speech.modify_timbre(new_timbre)
    assert human.speech.timbre.quality == 1
