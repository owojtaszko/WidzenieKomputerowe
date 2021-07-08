import cv2

image_path = "koparki.jpg"
image_bgr = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)  # konwersja BGR na RGB
image_gray = cv2.cvtColor(image_bgr,cv2.COLOR_BGR2GRAY)
# konwersja BGR na obraz w odcieniach szarości (monochromatyczny)

cv2.imshow("Koparki RGB", image_bgr)
cv2.imshow("Koparki BGR", image_rgb)
cv2.imshow("Koparki GRAY", image_gray)

cv2.waitKey(-1)
cv2.destroyAllWindows()
