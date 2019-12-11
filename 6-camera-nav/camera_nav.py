import gpiozero
from find_contours import setup_camera
from find_contours import get_saturated_contours

robot = gpiozero.Robot(left=(27, 17), right=(24, 23))
camera, capture_buffer = setup_camera()

for raw in camera.capture_continuous(capture_buffer, format="bgr"):
    image = raw.array
    masked, contours, found_colour = get_saturated_contours(image)
    print(f"Colour {found_colour}, h value: {found_colour[0]}")
    if 5 < found_colour[0] < 40:
        print("yellow")
        robot.left()
    elif 100 < found_colour < 135:
        print("blue")
        robot.right()
    else:
        robot.forward()
    capture_buffer.truncate(0)
