import whisper

model = whisper.load_model("medium")
audio = "top2010.wav"

# Transcribe with segments
result = model.transcribe(audio, language="es", verbose=True)

with open("top2010.txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        text = segment["text"].strip()
        print(text)      # Shows in terminal live
        f.write(text + "\n")  # Writes to file progressively
