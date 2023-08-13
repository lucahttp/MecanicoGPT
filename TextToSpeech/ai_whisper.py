import whisper
from pathlib import Path
import wave
import numpy as np




model = whisper.load_model("base")


# audio_file = Path('audio.mp3')


with wave.open("output.wav", "rb") as wav_file:
    audio_data = wav_file.readframes(wav_file.getnframes())


# audio_array = np.frombuffer(audio_data, dtype=np.int16)
audio_array = np.frombuffer(audio_data, np.int16).flatten().astype(np.float32) / 32768.0 

result = model.transcribe(audio_array)
print(result["text"])
print(result)
