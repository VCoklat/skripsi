import cv2
import time

cam = cv2.VideoCapture(0)

cv2.namedWindow("Tekan spasi untuk memulai ambil foto selama 5 detik dan esc untuk menutup")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("Tekan spasi untuk memulai ambil foto selama 5 detik dan esc untuk menutup", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        for x in range(5):
            ret, frame = cam.read()
            img_name = str(x+1)+".jpg"
            cv2.imwrite(img_name, frame)
            time.sleep(1)

cam.release()

cv2.destroyAllWindows()
