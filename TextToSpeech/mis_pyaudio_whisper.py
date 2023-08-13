import pyaudio
import wave
import whisper




# Set parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio object
audio = pyaudio.PyAudio()

# Open audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording started...")

# Record audio
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording stopped...")

# Stop audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save audio to file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()






import whisper
from pathlib import Path
import wave
import numpy as np



model = whisper.load_model("medium")
# audio_file = Path('audio.mp3')
with wave.open("output.wav", "rb") as wav_file:
    audio_data = wav_file.readframes(wav_file.getnframes())
# audio_array = np.frombuffer(audio_data, dtype=np.int16)
audio_array = np.frombuffer(audio_data, np.int16).flatten().astype(np.float32) / 32768.0 
result = model.transcribe(audio_array)
print(result["text"])
print(result)



print(f"Recorded {len(frames)} frames.")