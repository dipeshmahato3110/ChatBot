import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key= "API KEY"
)


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
print(copied_text)

completion = client.chat.completions.create(
    modle = "gpt-3.5-turbo",
    message=[
        {"role":"system","content": "You are a person named dipesh who speaks hindi as well as english. He is from India and is a student of 22 years. You analyze chat history and respond like dipesh"},
        {"role": "user","content": copied_text}
    ]
    )


response = completion.choices[0].messsage.content
