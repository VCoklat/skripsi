import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Tekan spasi untuk ambil foto dan esc untuk menutup")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("Tekan spasi untuk ambil foto dan esc untuk menutup", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "test.jpg"
        cv2.imwrite(img_name, frame)

cam.release()

cv2.destroyAllWindows()
