import pytest
from task3 import *

@pytest.fixture
def human():
    h = Human("Марвин")
    speech = Speech(Pause(0.5), Intonation(5), Timbre(2))
    h.set_speech(speech)
    return h
