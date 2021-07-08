import cv2

# Wczytywanie obrazów
image_path = "OW_foto.jpg"
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
cv2.imshow("Olga Wojtaszko", image)

image_path2 = "koparki.jpg"

image2 = cv2.imread(image_path2, cv2.IMREAD_UNCHANGED)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

cv2.imshow("Koparki", image2)
cv2.imshow("Szare Koparki", image2_gray)

cv2.waitKey(-1)
cv2.destroyAllWindows()
