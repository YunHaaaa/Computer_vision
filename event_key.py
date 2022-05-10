import cv2

img_file = '../img/cat.JPG'
img = cv2.imread(img_file)
title = 'IMG'
x, y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF # 키보드 입력 무한 대기, 8비트 마스크 처리
    print(key, chr(key))
    
    if key == ord('h'):
        x -= 10
    elif key == ord('j'):
        y += 10
    elif key == ord('k'):
        y -= 10
    elif key == ord('l'):
        x += 10
    elif key == ord('q') or key == 27: # 27 = esc
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title, x, y) # 새로운 좌표로 창 이동
        
