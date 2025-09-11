import whisper
import sounddevice as sd
import numpy as np

# Load Whisper model (small is faster, medium/large are more accurate)
model = whisper.load_model("small")

def record_and_transcribe(duration=30, samplerate=16000):
    """
    Records audio from microphone for given duration and transcribes it to English.
    """
    print("🎙️ Recording... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.float32)
    sd.wait()
    print("✅ Recording complete, transcribing...")

    # Convert to numpy array Whisper expects
    audio = np.squeeze(audio)

    # Transcribe and translate to English
    result = model.transcribe(audio, task="translate")

    detected_lang = result.get("language", "unknown")
    text = result["text"]

    print(f"🌍 Detected language: {detected_lang}")
    print(f"📝 English text: {text}\n")

if __name__ == "__main__":
    while True:
        record_and_transcribe(duration=30)  # listen every 5 seconds