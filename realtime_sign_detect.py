import os
import cv2
import numpy as np
import time  # ✅ Required for delay handling
import mediapipe as mp
from tensorflow.keras.models import load_model

# Force CPU only
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


# Load the trained model
try:
    model = load_model("asl_model_v3.h5", compile=False)
except Exception as e:
    print(f"Model load error: {e}")
    exit()


# Initialize MediaPipe
try:
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7
    )
    mp_draw = mp.solutions.drawing_utils
except Exception as e:
    print(f"MediaPipe setup failed: {e}")
    exit()

# Labels for A–Z and special symbols
labels = [chr(i) for i in range(65, 91)]  # A–Z
labels += ['del', 'space', 'nothing']

# Open webcam
print("Trying to open webcam...")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("ERROR: Webcam not accessible.")
    exit()

# Prediction state
predicted_text = ""
prev_letter = ""
letter_start_time = 0
letter_delay = 2.0  # Seconds

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("⚠️ Frame not read properly")
        continue  # Don't break, try next frame

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x_vals = [lm.x for lm in hand_landmarks.landmark]
            y_vals = [lm.y for lm in hand_landmarks.landmark]

            xmin = max(int(min(x_vals) * w) - 20, 0)
            xmax = min(int(max(x_vals) * w) + 20, w)
            ymin = max(int(min(y_vals) * h) - 20, 0)
            ymax = min(int(max(y_vals) * h) + 20, h)

            hand_img = frame[ymin:ymax, xmin:xmax]
            if hand_img.size == 0:
                print("⚠️ Empty hand image, skipping")
                continue

            hand_img = cv2.resize(hand_img, (224, 224))
            hand_img = cv2.cvtColor(hand_img, cv2.COLOR_BGR2RGB)
            hand_img = hand_img / 255.0
            hand_img = np.expand_dims(hand_img, axis=0)

            try:
                prediction = model.predict(hand_img, verbose=0)[0]
                class_id = np.argmax(prediction)
                confidence = np.max(prediction)
            except Exception as e:
                print(f"Prediction error: {e}")
                continue

            if confidence > 0.75 and class_id < len(labels):
                letter = labels[class_id]
                current_time = time.time()

                if letter != prev_letter:
                    prev_letter = letter
                    letter_start_time = current_time
                elif current_time - letter_start_time > letter_delay:
                    if letter == "del":
                        predicted_text = predicted_text[:-1]
                    elif letter == "space":
                        predicted_text += " "
                    elif letter != "nothing":
                        predicted_text += letter

                    with open("output.txt", "w") as f:
                        f.write(predicted_text)

                    prev_letter = ""

                cv2.putText(frame, f"{letter} ({confidence:.2f})", (xmin, ymin - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Draw predicted text box
    cv2.rectangle(frame, (10, 30), (w - 10, 80), (0, 0, 0), -1)
    cv2.putText(frame, "Output: " + predicted_text, (20, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

    cv2.imshow("ASL Real-Time Detection", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("Quit key pressed. Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
