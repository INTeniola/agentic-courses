import os
import json
import subprocess
import urllib.request

def get_access_token():
    try:
        token = subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode().strip()
        return token
    except Exception as e:
        print(f"Error fetching gcloud token: {e}")
        return None

def synthesize_text(text, voice_name="en-US-Chirp2-HD-F", output_file="day_1/Day_1_Narration.mp3"):
    token = get_access_token()
    if not token:
        print("Failed to get authorization token.")
        return False

    url = "https://texttospeech.googleapis.com/v1/text:synthesize"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8",
        "x-goog-user-project": "quizant"
    }

    payload = {
        "input": {"text": text},
        "voice": {
            "languageCode": "en-US",
            "name": voice_name
        },
        "audioConfig": {
            "audioEncoding": "MP3",
            "speakingRate": 1.0,
            "pitch": 0.0
        }
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            import base64
            audio_bytes = base64.b64decode(res_data["audioContent"])
            with open(output_file, "wb") as f:
                f.write(audio_bytes)
            print(f"✅ Successfully synthesized expressive Chirp v2 audio to {output_file}")
            return True
    except Exception as e:
        print(f"API Error during synthesis: {e}")
        if hasattr(e, 'read'):
            print(e.read().decode('utf-8'))
        return False

def main():
    print("Preparing text from Day 1 Video Script...")
    script_path = "day_1/Day_1_Video_Script.md"
    if not os.path.exists(script_path):
        print(f"Error: {script_path} does not exist.")
        return

    with open(script_path, "r") as f:
        lines = f.readlines()

    clean_text_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("[VISUAL CUE") or stripped.startswith("#"):
            continue
        if stripped:
            clean_text_lines.append(stripped)

    full_narration = " ".join(clean_text_lines)
    sample_narration = full_narration[:4000]

    print(f"Synthesizing {len(sample_narration)} characters using Google Cloud Chirp v2 Expressive Voice...")
    
    # Try Chirp2-HD first, fallback to Journey or Neural2 if project doesn't have Chirp enabled
    success = synthesize_text(sample_narration, voice_name="en-US-Chirp2-HD-F", output_file="day_1/Day_1_Narration.mp3")
    if not success:
        print("Falling back to Google Journey Expressive Voice (en-US-Journey-F)...")
        success = synthesize_text(sample_narration, voice_name="en-US-Journey-F", output_file="day_1/Day_1_Narration.mp3")
    if not success:
        print("Falling back to Neural2 HD Voice (en-US-Neural2-D)...")
        synthesize_text(sample_narration, voice_name="en-US-Neural2-D", output_file="day_1/Day_1_Narration.mp3")

if __name__ == "__main__":
    main()
