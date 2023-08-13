from pvrecorder import PvRecorder
import whisper
import keyboard



# Initialize recording state
global audio
for index, device in enumerate(PvRecorder.get_audio_devices()):
    print(f"[{index}] {device}")


recorder = PvRecorder(device_index=3, frame_length=512)
audio = []

def on_press_space(event=None):
    recorder.start()

def on_release_space(event=None):
    recorder.stop()
    frame = recorder.read()

    
    model = whisper.load_model("base")
    text = model.transcribe(frame)
    #text = whisper.transcribe(audio.frames)
    print(text)

keyboard.on_press_key("space", on_press_space, suppress=True)
keyboard.on_release_key("space", on_release_space, suppress=True)
keyboard.wait()