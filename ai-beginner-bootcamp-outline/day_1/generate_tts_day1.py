import os
from google.cloud import texttospeech

def synthesize_audio():
    print("Synthesizing Day 1 voiceover narration with Google Cloud Text-to-Speech...")
    
    if not os.path.exists("Day_1_Video_Script.md"):
        print("Error: Day_1_Video_Script.md not found.")
        return

    with open("Day_1_Video_Script.md", "r") as f:
        lines = f.readlines()

    # Extract spoken narration (filter out visual cues and headers)
    narration_text = []
    for line in lines:
        cleaned = line.strip()
        if cleaned.startswith("[VISUAL CUE") or cleaned.startswith("#"):
            continue
        if cleaned:
            narration_text.append(cleaned)

    full_narration = " ".join(narration_text)

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=full_narration[:4000]) # GCP TTS limit per call

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-D", # Natural, professional male voice
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.0,
        pitch=0.0
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open("Day_1_Narration.mp3", "wb") as out:
        out.write(response.audio_content)
        print("✅ Saved day_1/Day_1_Narration.mp3 successfully!")

if __name__ == "__main__":
    synthesize_audio()
