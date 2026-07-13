import cv2
import mediapipe as mp
import pyautogui
import time

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = True 

screen_width, screen_height = pyautogui.size()
cam_width, cam_height = 640, 480 

click_threshold = 25 


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,    
    max_num_hands=1,            
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7   
)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

print("Program Virtual")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Gagal mengambil gambar dari kamera.")
        continue

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]


            index_x = int(index_tip.x * cam_width)
            index_y = int(index_tip.y * cam_height)
            thumb_x = int(thumb_tip.x * cam_width)
            thumb_y = int(thumb_tip.y * cam_height)

          
            mouse_x = screen_width * index_tip.x
            mouse_y = screen_height * index_tip.y
            
            
            pyautogui.moveTo(mouse_x, mouse_y, duration=0) 

            distance = ((thumb_x - index_x)**2 + (thumb_y - index_y)**2)**0.5

            cv2.putText(frame, f'Jarak: {int(distance)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.line(frame, (index_x, index_y), (thumb_x, thumb_y), (255, 0, 0), 2)

            if distance < click_threshold:
                cv2.line(frame, (index_x, index_y), (thumb_x, thumb_y), (0, 0, 255), 3)
                
                pyautogui.click()
                time.sleep(0.1) 



    cv2.imshow('Virtual Touchpad (Python)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()