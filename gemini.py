import pyautogui
import pyperclip
import time
import textwrap
import google.generativeai as genai

# Disable PyAutoGUI failsafe
pyautogui.FAILSAFE = False 

# Set your API key
genai.configure(api_key="AIzaSyAeWxMW_fRlmYZ4g8ybsivGw--PTpf28Bs")
# Initialize the GenAI model
model = genai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat()  # Start once, reuse

# Track last seen message
last_message = ""
last_sender_message = ""  # <-- Add this line
last_reply_preview = ""   # (if not already declared)

print(" Waiting for new sender message...\n")

# Click the WhatsApp icon
pyautogui.moveTo(1065, 1052, duration=0.3)
pyautogui.click()
time.sleep(1)

while True:
    try:
        # Drag to select text
        pyautogui.moveTo(672, 197, duration=0.2)
        pyautogui.mouseDown()
        pyautogui.moveTo(1885, 940, duration=0.5)
        pyautogui.mouseUp()

        # Copy
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.click(1397,222)

        # Read from clipboard
        time.sleep(0.3)
        copied_text = pyperclip.paste().strip()

        if not copied_text:
            time.sleep(1.5)
            continue  # Nothing copied, skip

        # Get the last line of the chat
        chat_lines = copied_text.splitlines()
        last_line = chat_lines[-1].strip()

        # Skip replies you sent (with your name or timestamped prefix)
        if last_line.startswith("[") and "] DM:" in last_line:
            print("Skipping own sent message.")
            time.sleep(2)
            continue

        # If the last message is same as before, skip
        if last_line == last_sender_message:
            time.sleep(1.5)
            continue

        # Update last seen sender message
        last_sender_message = last_line
        print("New message detected:", last_line)
       
        # Send to Google GenAI (Gemini)
        prompt = (
                "You're Dipesh, a 22-year-old student from India who speaks Hindi, English, and Bengali. "
                "Based on the chat below, detect its tone and language style (Hinglish, Bengali mix, or English) "
                "and reply naturally in the same language style without saying what the language is.\n\n"
                + last_line
            )
            
       
        response = chat.send_message(prompt)
        
        # Clean reply
        reply = response.text.strip()  

        print("Reply:", reply)

     
        pyperclip.copy(reply)  # Copy AI response to clipboard
        pyautogui.click(795, 985)      # Click on message input box
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')  # Paste the response
        time.sleep(0.2)
        pyautogui.press('enter')       # Press Enter to send

        # Wait before checking again
        time.sleep(3)
    
    except KeyboardInterrupt:
        print("\n Script stopped by user.")
        break

    except Exception as e:
        print("⚠️ Error:", e)
        time.sleep(3)


