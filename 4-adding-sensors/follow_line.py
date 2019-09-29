from signal import pause
import atexit
import gpiozero
from gpiozero.tools import scaled, negated

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))
left_line_sensor = gpiozero.LineSensor(5)
right_line_sensor = gpiozero.LineSensor(6)
# Ensure it will stop
atexit.register(robot.stop)

robot.left_motor.source = scaled(negated(left_line_sensor), -0.3, 0.4)
robot.right_motor.source = scaled(negated(right_line_sensor), -0.3, 0.4)

pause()
