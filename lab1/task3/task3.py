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
        return next((emotion.intensity for emotion in self.emotions if emotion.name == emotion_name), 0)

    def express_emotion(self, emotion_name):
        emotions_params = {
            "презрение": (1.0, 2, 3),
            "ужас": (0.1, 8, 1)
        }

        if emotion_name not in emotions_params:
            raise ValueError("Неизвестная эмоция")

        pause_duration, intonation_level, timbre_quality = emotions_params[emotion_name]

        self.add_emotion(Emotion(emotion_name, 10))
        if self.speech:
            self.speech.modify_pause(Pause(pause_duration))
            self.speech.modify_intonation(Intonation(intonation_level))
            self.speech.modify_timbre(Timbre(timbre_quality))
