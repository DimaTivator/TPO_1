class Pause:
    def __init__(self, duration):
        self.duration = duration

class Intonation:
    def __init__(self, level):
        self.level = level

class Timbre:
    def __init__(self, quality):
        if not (0 <= quality <= 3):
            raise ValueError("Характеристика тембра должна быть от 0 до 3!")
        self.quality = quality

class Speech:
    def __init__(self, pause, intonation, timbre):
        self.pause = pause
        self.intonation = intonation
        self.timbre = timbre

    def modify_pause(self, new_pause):
        self.pause = new_pause

    def modify_intonation(self, new_intonation):
        self.intonation = new_intonation

    def modify_timbre(self, new_timbre):
        self.timbre = new_timbre

class Emotion:
    def __init__(self, name, intensity):
        if not (0 <= intensity <= 10):
            raise ValueError("Интенсивность должна быть от 0 до 10!")
        self.name = name
        self.intensity = intensity

    def modify_intensity(self, new_intensity):
        self.intensity = new_intensity

class Human:
    def __init__(self, name):
        self.name = name
        self.speech = None
        self.emotions = []

    def set_speech(self, speech):
        self.speech = speech

    def add_emotion(self, emotion):
        self.emotions.append(emotion)

    def get_emotion_intensity(self, emotion_name):
        for emotion in self.emotions:
            if emotion.name == emotion_name:
                return emotion.intensity
        return 0

    def express_contempt(self):
        contempt = Emotion("презрение", 10)
        self.add_emotion(contempt)
        if self.speech:
            self.speech.modify_pause(Pause(1.0))
            self.speech.modify_intonation(Intonation(2))
            self.speech.modify_timbre(Timbre(3))

    def express_terror(self):
        terror = Emotion("ужас", 10)
        self.add_emotion(terror)
        if self.speech:
            self.speech.modify_pause(Pause(0.1))
            self.speech.modify_intonation(Intonation(8))
            self.speech.modify_timbre(Timbre(1))
