import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)

def cartoonize_image(img):
    """Apply cartoon effect to image"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for natural view
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    output = frame.copy()
    filter_name = "Normal"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark
            finger_tips = [8, 12, 16, 20]  # index, middle, ring, pinky tips
            finger_open = []

            for tip in finger_tips:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    finger_open.append(1)
                else:
                    finger_open.append(0)

            # Gesture 1: Open Palm (all fingers open) → Grayscale
            if sum(finger_open) == 4:
                output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
                filter_name = "Grayscale"

            # Gesture 2: Peace Sign (Index + Middle open) → Cartoon
            elif finger_open[0] == 1 and finger_open[1] == 1 and finger_open[2] == 0 and finger_open[3] == 0:
                output = cartoonize_image(frame)
                filter_name = "Cartoon"

            # Gesture 3: Fist (all fingers closed) → Blur
            elif sum(finger_open) == 0:
                output = cv2.GaussianBlur(frame, (25, 25), 30)
                filter_name = "Blur"

            # Gesture 4: One Finger (Index only) → Sepia
            elif finger_open[0] == 1 and finger_open[1] == 0 and finger_open[2] == 0 and finger_open[3] == 0:
                sepia_filter = np.array([[0.272, 0.534, 0.131],
                                          [0.349, 0.686, 0.168],
                                          [0.393, 0.769, 0.189]])
                output = cv2.transform(frame, sepia_filter)
                output = np.clip(output, 0, 255).astype(np.uint8)
                filter_name = "Sepia"

            # Gesture 5: Rock Sign (Index + Pinky) → Edge Detection
            elif finger_open[0] == 1 and finger_open[1] == 0 and finger_open[2] == 0 and finger_open[3] == 1:
                edges = cv2.Canny(frame, 100, 200)
                output = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
                filter_name = "Edge Detection"

            # Gesture 6: OK Sign (Thumb + Index close) → Invert Colors
            thumb_index_distance = abs(landmarks[4].x - landmarks[8].x) + abs(landmarks[4].y - landmarks[8].y)
            if thumb_index_distance < 0.05:
                output = cv2.bitwise_not(frame)
                filter_name = "Invert Colors"

    # Show filter name on screen
    cv2.putText(output, f"Filter: {filter_name}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Gesture Filter App", output)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
