#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the ultrasonic sensor
trigger_pin = 23
echo_pin = 24

def setup_ultrasonic_sensor(trigger_pin, echo_pin):
    # Set up the GPIO pins for the ultrasonic sensor
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

def measure_distance(trigger_pin, echo_pin):
    # Send a pulse to the trigger pin
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    # Wait for the echo pin to go high and then low
    start_time = time.time()
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()

    while GPIO.input(echo_pin) == 1:
        end_time = time.time()

    # Calculate the duration of the pulse (time taken for the sound to travel)
    print(end_time - start_time)
    pulse_duration = (end_time - start_time) 

    # Speed of sound at 20°C is approximately 343 meters/second
    # Divide by 2 to get one-way distance, as the sound travels back and forth
    distance = (pulse_duration * 343) * 100 / 2 

    return distance

def cleanup():
    # Clean up the GPIO settings
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup_ultrasonic_sensor(trigger_pin, echo_pin)

        while True:
            # Measure the distance to the nearby object
            distance_cm = measure_distance(trigger_pin, echo_pin)
            print(f"Distance to nearby object: {distance_cm:.2f} cm")

            # Adjust the frequency of measurements based on your needs
            time.sleep(0.5)

    except KeyboardInterrupt:
        cleanup()

