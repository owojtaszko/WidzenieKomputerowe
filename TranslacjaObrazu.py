import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "koparki.jpg"
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)


# funkcja pomocnicza
def plot_image(image, label):
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap='gray')
    plt.title(label)
    plt.show()


# Translacja obrazu
M = np.float32([[1, 0, 50], [0, 1, 25]])
dst = cv2.warpAffine(image, M, (700, 900))
# 700x900 rozmiar wynikowego obrazu

plot_image(dst, "Translacja obrazu")
