import time
import imutils
import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera


def setup_camera():
    camera = PiCamera()
    camera.resolution = (128, 128)
    camera.rotation = 180

    capture_buffer = PiRGBArray(camera, size=(128, 128))
    camera.start_preview()
    time.sleep(2)
    return camera, capture_buffer


def get_saturated_contours(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Mask for vivid colours
    masked = cv2.inRange(hsv, np.array([0, 140, 30]), np.array([255, 255, 255]))
    # Find Contours
    cnts = cv2.findContours(masked.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(cnts)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    colour = [0, 0, 0]
    if len(contours) > 0:
        # Find the center of the contour
        m = cv2.moments(contours[0])
        if m["m00"] > 0:
            cx = int(m["m10"] / m["m00"])
            cy = int(m["m01"] / m["m00"])
            colour = hsv[cy, cx]
    return masked, contours, colour


if __name__ == '__main__':
    camera, capture_buffer = setup_camera()
    camera.capture(capture_buffer, format="bgr")
    image = capture_buffer.array
    masked, contours, found_colour = get_saturated_contours(image)
    cv2.imwrite('original.png', image)
    cv2.imwrite('masked.png', masked)
    cv2.drawContours(image, contours[:1], -1, (0, 255, 0), 1)
    cv2.imwrite('with_contours.png', image)
    print(found_colour)
