from plyer import notification
import pyttsx3 as s
import time

initialize = s.init()
while True:
    # Voice reminder
    initialize.say("Please drink water. Drinking water is for your own safety.")
    initialize.runAndWait()
    
    # Desktop notification
    notification.notify(
        title="Drink Water",
        message="Drink water for your own safety.",
        app_name="REMINDER",
        timeout=5  # Corrected timeout syntax
    )
    
    # Wait for a period before the next reminder
    time.sleep(10)  # Adjust the sleep time as needed
