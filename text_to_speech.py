from gtts import gTTS

text_to_say = "How are you doing?."

language = "en"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save("/content/gtts.wav")

from IPython.display import Audio

Audio("/content/gtts.wav")
