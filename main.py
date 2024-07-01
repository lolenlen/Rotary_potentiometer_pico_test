# This programs allows an analog potentiometer to control the frequencies of an LED and a buzzer with
# with a max and min pot value, since the pot value does not go below 128 and the buzzer does not have
# a freq value more than 54000

import machine
import utime

# Define analog input pin for the potentiometer (GP26)
potentiometer = machine.ADC(26)

# Set up LED and Buzzer as PWM outputs
led = machine.PWM(machine.Pin(14))
led.freq(1000)  # LED frequency set to 1 kHz

buzzer = machine.PWM(machine.Pin(15))

# Function to map potentiometer value to frequency
def buzzer_freq(pot_value):
    min_freq = 500
    max_freq = 4000
    freq = min_freq + (pot_value * (max_freq - min_freq)) // 65535
    return freq

# Function to read and limit potentiometer value
def get_pot_value():
    pot_value = potentiometer.read_u16()
    if pot_value < 3000:
        pot_value = 0
    elif pot_value > 54000:
        pot_value = 54000  # Limit to 54000
    return pot_value

while True:
    pot_value = get_pot_value()  # Read potentiometer value inside the loop
    print(pot_value)
    
    # Set LED brightness and buzzer frequency based on potentiometer value
    freq = buzzer_freq(pot_value)
    led.duty_u16(pot_value)
    buzzer.freq(freq)
    buzzer.duty_u16(pot_value)  # Set duty cycle to potentiometer value for volume control
    
    utime.sleep(0.01)  # Small delay to avoid overloading the CPU
