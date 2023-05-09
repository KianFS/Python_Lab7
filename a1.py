# ******************part1************************
import cv2
import numpy as np
import argparse

# ******************part2************************
image = cv2.imread("monsters.jpeg")
# ******************part3-4************************
B, G, R = cv2.split(image)
# ******************part5************************
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ******************part6************************
(B, G, R) = cv2.split(image)
g = G * 0
red_and_blue = cv2.merge([B, g, R])
cv2.imshow("red & blue", red_and_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ******************part7************************
red_and_blue_plus_green = cv2.merge([B, G, R])
cv2.imshow("recombined red+green+blue ", red_and_blue_plus_green)
cv2.waitKey(0)
cv2.destroyAllWindows()


