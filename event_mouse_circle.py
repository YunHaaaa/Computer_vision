import cv2

title = 'mouse event'
img = cv2.imread('../img/blank_500.jpeg')
cv2.imshow(title, img)

def onMouse(event, x, y, flags, param): # 아무스 콜백 함수
    print(event, x, y, )
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 30, (0, 0, 0), -1)
        cv2.imshow(title, img)
cv2.setMouseCallback(title, onMouse) # 마우스 콜백 함수를 GUI 윈도우에 등록

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()
