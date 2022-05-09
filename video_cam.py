import cv2

cap = cv2.VideoCapture(0) # 0번 카메라 장치 연결
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1: # lms동안 키 입력 대기
                break # 아무 키라도 입력이 있으면 중지
        else:
            print('no frame')
            break
else:
    print('can\'t open camera')
cap.release()
cv2.destroyAllWindows()
