import cv2

# Strumień video z pliku

video_path = "https://ogarnij.ai/wp-content/uploads/2021/03/MongKok.mp4"

cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imshow('MP4', frame)
        key = cv2.waitKey(40)
        if key == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
print('Koniec odtwarzania')
