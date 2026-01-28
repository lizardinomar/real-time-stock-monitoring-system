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

# Both LEDs ON by default
GPIO.output(LED_GREEN, GPIO.HIGH)
GPIO.output(LED_RED, GPIO.HIGH)
GPIO.output(BUZZER, GPIO.LOW)

BLINK_DURATION = 15      # seconds
BLINK_INTERVAL = 0.5    # on/off speed

try:
    while True:
        price = random.uniform(150, 200)
        print(f"Mock stock price: {price:.2f}")

        start_time = time.time()

        if price >= 190:
            print("GREEN ALERT")
            while time.time() - start_time < BLINK_DURATION:
                GPIO.output(LED_GREEN, GPIO.LOW)
                GPIO.output(LED_RED, GPIO.HIGH)

                GPIO.output(BUZZER, GPIO.HIGH)
                time.sleep(0.5)

                GPIO.output(LED_GREEN, GPIO.HIGH)
                GPIO.output(BUZZER, GPIO.LOW)
                time.sleep(0.5)

        elif price <= 180:
            print("RED ALERT")
            while time.time() - start_time < BLINK_DURATION:
                GPIO.output(LED_RED, GPIO.LOW)
                GPIO.output(LED_GREEN, GPIO.HIGH)

                GPIO.output(BUZZER, GPIO.HIGH)
                time.sleep(0.15)

                GPIO.output(LED_RED, GPIO.HIGH)
                GPIO.output(BUZZER, GPIO.LOW)
                time.sleep(0.15)

        # Return to default state
        GPIO.output(LED_GREEN, GPIO.HIGH)
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(BUZZER, GPIO.LOW)

        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
