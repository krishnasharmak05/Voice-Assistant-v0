import pyttsx3


engine = pyttsx3.init()

# RATE
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)

# VOLUME
volume = engine.getProperty("volume") 
engine.setProperty("volume", 1.0)

# VOICE
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) 
