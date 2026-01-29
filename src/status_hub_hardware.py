import RPi.GPIO as GPIO
import time

# ================= PIN CONFIG (PHYSICAL) =================
GREEN_LED = 16
RED_LED = 18
BUZZER = 22

# ================= GPIO SETUP =================
GPIO.setmode(GPIO.BOARD)

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

# ================= STATES =================
def idle_state():
    """Both LEDs ON, buzzer OFF"""
    GPIO.output(GREEN_LED, GPIO.HIGH)
    GPIO.output(RED_LED, GPIO.HIGH)
    GPIO.output(BUZZER, GPIO.LOW)

def green_alert():
    """Green LED blink + long buzzer beeps"""
    print("GREEN ALERT")
    end_time = time.time() + 15

    while time.time() < end_time:
        GPIO.output(GREEN_LED, GPIO.HIGH)
        GPIO.output(RED_LED, GPIO.HIGH)

        GPIO.output(BUZZER, GPIO.HIGH)
        time.sleep(3)

        GPIO.output(BUZZER, GPIO.LOW)
        time.sleep(1)

    idle_state()

def red_alert():
    """Red LED blink + rapid buzzer beeps"""
    print("RED ALERT")
    end_time = time.time() + 15

    while time.time() < end_time:
        GPIO.output(RED_LED, GPIO.HIGH)
        GPIO.output(BUZZER, GPIO.HIGH)
        time.sleep(0.15)

        GPIO.output(RED_LED, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.LOW)
        time.sleep(0.15)

    idle_state()

# ================= MAIN LOOP =================
if __name__ == "__main__":
    try:
        print("Status Hub Hardware Initialized")
        idle_state()

        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Shutting down...")
        GPIO.cleanup()
