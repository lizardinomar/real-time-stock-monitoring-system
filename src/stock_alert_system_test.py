import RPi.GPIO as GPIO
import time
import random

LED_GREEN = 16
LED_RED = 18
BUZZER = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.output(LED_GREEN, GPIO.HIGH)
GPIO.output(LED_RED, GPIO.HIGH)
GPIO.output(BUZZER, GPIO.LOW)

try:
    while True:
        price = random.uniform(150, 200)
        print(f"Mock stock price: {price:.2f}")

        if price >= 190:
            # Green blink + long beep
            GPIO.output(LED_GREEN, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_GREEN, GPIO.HIGH)
            GPIO.output(BUZZER, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(BUZZER, GPIO.LOW)
            time.sleep(1)
        elif price <= 180:
            # Red blink + short beeps
            GPIO.output(LED_RED, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(LED_RED, GPIO.HIGH)
            for _ in range(100):
                GPIO.output(BUZZER, GPIO.HIGH)
                time.sleep(0.15)
                GPIO.output(BUZZER, GPIO.LOW)
                time.sleep(0.15)
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
