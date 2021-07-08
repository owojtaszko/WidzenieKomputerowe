import cv2

# Strumień video z kamery

cap = cv2.VideoCapture(0)

# zamiast podawać ścieżkę do pliku podajemy indeks kamer.
# Jeżeli w systemie obecna jest jedna kamera, będzie to indeks = 0.
# W przypadku większej ilości kamer możemy podać inne ID (np. 1), co pozwoli nam na uruchomienie innej kamery.

# zmiana rozmiaru klatki
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# zmiana FPS
cap.set(cv2.CAP_PROP_FPS, 40)
# zmiana jasności
cap.set(cv2.CAP_PROP_BRIGHTNESS, 15)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Kamera', frame)
        key = cv2.waitKey(40)
        if key == ord('q'):
            break
    else:
        break

cap.release()  # funkcja zwalnia kamery
cv2.destroyAllWindows()
print('Koniec odtwarzania')
