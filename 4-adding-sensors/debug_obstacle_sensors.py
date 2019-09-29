import gpiozero
from signal import pause

left_obstacle_sensor = gpiozero.DigitalInputDevice(13)
right_obstacle_sensor = gpiozero.DigitalInputDevice(26)

left_obstacle_sensor.when_deactivated = lambda: print("Left obstacle in range")
left_obstacle_sensor.when_activated = lambda: print("Left obstacle out of range")

right_obstacle_sensor.when_deactivated = lambda: print("Right obstacle in range")
right_obstacle_sensor.when_activated = lambda: print("Right obstacle out of range")

pause()
