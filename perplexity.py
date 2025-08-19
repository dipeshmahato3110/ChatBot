import pyautogui
import pyperclip
import time
import requests

# Perplexity API details — replace with actual key and endpoint
api_key = "API KEY"
endpoint = "https://api.perplexity.ai/chat/completions"

# Step 1: Click the WhatsApp icon
pyautogui.moveTo(1065, 1052, duration=0.3)
pyautogui.click()

time.sleep(2)

# Step 2: Drag to select text
pyautogui.moveTo(672, 197, duration=0.3)
pyautogui.mouseDown()
pyautogui.moveTo(1885, 940, duration=1)
pyautogui.mouseUp()

# pyautogui.click()

# Step 3: Copy
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'c')


# Step 4: Read from clipboard
time.sleep(0.3)
copied_text = pyperclip.paste()

# Step 5: Send to Perplexity AI if copied
if copied_text.strip():
    print("✅ Copied Text:\n", copied_text)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar-pro",  # or whatever model is allowed (like pplx-70b-online)
        "messages": [
            {"role": "system", "content": "You are a person named dipesh who speaks hindi as well as english. He is from India and is a student. First you analyze chat history conversation and respond like dipesh. Reply in few words and make it simple. Do not say the name of the person to whom you are replying."},
            {"role": "user", "content": copied_text}
        ]
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        print("\n Perplexity Reply:\n", reply)
    else:
        print("API Error:", response.status_code, response.text)

else:
    print("Nothing copied! Check if selection worked.")

