import cv2
import os

LABEL = "love"
save_dir = os.path.join("dataset", LABEL)
os.makedirs(save_dir, exist_ok=True)
count = len(os.listdir(save_dir))
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. 좌우 반전
    frame = cv2.flip(frame, 1)

    # 2. 네모 박스(ROI) 좌표 설정: (x1, y1)은 왼쪽 위, (x2, y2)는 오른쪽 아래
    # 가로 250, 세로 250 크기의 정사각형 (CNN 입력용)
    x1, y1 = 350, 200
    x2, y2 = 600, 450
    roi = frame[y1:y2, x1:x2].copy()
    
    # 3. 원본 화면에 초록색 네모 박스 그리기
    # 인자 순서: (이미지, 시작점, 끝점, 색상(B,G,R), 선 두께)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)


    # 5. 전체 화면과 잘린 박스 화면 띄우기
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord(' '):  # 스페이스바 누르는 동안 저장
        filename = os.path.join(save_dir, f"{LABEL}_{count}.jpg")
        cv2.imwrite(filename, roi)
        count += 1
        print(f"저장됨: {filename} (총 {count}장)")
    elif key == ord('q'):
        break
    
    # 두 창 중 하나라도 'X' 버튼으로 닫히면 종료
    if cv2.getWindowProperty("Camera", cv2.WND_PROP_VISIBLE) < 1 : 
        break

cap.release()
cv2.destroyAllWindows()