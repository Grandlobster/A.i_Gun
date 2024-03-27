import cv2
from deepface import DeepFace
import tempfile
import serial

# Initialize the serial connection to the Arduino
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to match your Arduino's serial port

# Initialize face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def move_servos(pan_angle, tilt_angle):
    # Send servo commands to Arduino
    ser.write(f'x{pan_angle}y{tilt_angle}\n'.encode())

def detect_faces(reference_img_path):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    counter = 0
    face_match = False

    while True:
        ret, frame = cap.read()
        if ret:
            if counter % 30 == 0:
                try:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
                    for (x, y, w, h) in faces:
                        face_img = frame[y:y+h, x:x+w]
                        temp_img = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
                        cv2.imwrite(temp_img.name, face_img)
                        if DeepFace.verify(temp_img.name, reference_img_path)['verified']:
                            face_match = True
                        else:
                            face_match = False
                        temp_img.close()
                except ValueError:
                    face_match = False

            counter += 1
            if face_match:
                # Map face position to servo angles
                pan_angle = int((x + w/2) * 180 / frame.shape[1])
                tilt_angle = int((y + h/2) * 180 / frame.shape[0])
                move_servos(pan_angle, tilt_angle)

            for (x, y, w, h) in faces:
                color = (0, 255, 0) if face_match else (0, 0, 255)
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                label = "Terrorist" if face_match else "Non-Target"
                cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            cv2.imshow("video", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Usage
detect_faces('path_to_reference_image.jpg')
