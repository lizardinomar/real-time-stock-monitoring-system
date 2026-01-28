import RPi.GPIO as GPIO
import time

# -----------------------------
# GPIO setup
# -----------------------------
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbers
GPIO.setwarnings(False)

# Pin assignments (physical pins)
LED_GREEN = 16   # Green LED
LED_RED   = 18   # Red LED
BUZZER    = 22   # Buzzer

# Setup pins as outputs
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

# Initialize all OFF
GPIO.output(LED_GREEN, GPIO.LOW)
GPIO.output(LED_RED, GPIO.LOW)
GPIO.output(BUZZER, GPIO.LOW)

# -----------------------------
# Test loop
# -----------------------------
try:
    while True:
        # GREEN ON, RED OFF, buzzer OFF
        GPIO.output(LED_GREEN, GPIO.HIGH)
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(BUZZER, GPIO.LOW)
        time.sleep(0.2)

        # RED ON, GREEN OFF, buzzer short beep
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_RED, GPIO.HIGH)

        # Short beep: 0.05 sec ON, 0.15 sec OFF
        GPIO.output(BUZZER, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(BUZZER, GPIO.LOW)
        time.sleep(0.15)

except KeyboardInterrupt:
    GPIO.cleanup()
