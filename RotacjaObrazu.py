import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "koparki.jpg"
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

M = cv2.getRotationMatrix2D(((700-1)/2, (900-1)/2), 45, 1)
dst = cv2.warpAffine(image, M, (700, 900))

def plot_image(image, label):
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap='gray')
    plt.title(label)
    plt.show()

plot_image(dst, "Rotacja obrazu 45 stopni")