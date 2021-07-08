import cv2
from matplotlib import pyplot as plt

image_path = "koparki.jpg"
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# zmiana kolejności kolorów BGR -> RBG
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# wyłaczenie znacznikow wartosci osi wspolrzednych i opisow
plt.xticks([])
plt.yticks([])

plt.imshow(image)
plt.title(image_path)
plt.show()
