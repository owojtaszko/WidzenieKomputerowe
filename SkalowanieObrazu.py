import cv2
from matplotlib import pyplot as plt

image_path = "koparki.jpg"

image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = image.shape[:2]

scaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
scaled2 = cv2.resize(image, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)


def plot_image(image, label):
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image, cmap='gray')
    plt.title(label)
    plt.show()

plot_image(scaled, "Skalowanie poprzez współczynnik")
plot_image(scaled2, "Skalowanie poprzez rozmiar")
