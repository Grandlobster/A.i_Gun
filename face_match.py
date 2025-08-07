import cv2
from deepface import DeepFace
import pyfirmata

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#board = pyfirmata.Arduino('COM5')
#pan_pin = board.get_pin('d:9:s')  # Digital pin 9 for pan servo
#tilt_pin = board.get_pin('d:10:s')  # Digital pin 10 for tilt servo

def mirror_value(val,):
    midpoint = (0 + 180) / 2
    mirror_val = midpoint - (val - midpoint)
    return mirror_val
def make_positive(n):
    if n < 0:
        return -n  # Return the absolute value
    return n
def map_value(value, from_min, from_max, to_min, to_max):
    return int((value - from_min) * (to_max - to_min) / (from_max - from_min) + to_min)

def detect_faces(reference_img_path):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    counter = 0
    face_match = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if counter % 30 == 0:  # Process every 30th frame
            try:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 5)

                face_match = False
                for (x, y, w, h) in faces:
                    if DeepFace.verify(frame[y:y+h, x:x+w], reference_img_path)['verified']:
                        face_match = True

                    center_x = int(x + w / 2)
                    center_y = int(y + h / 2)

                    pan_angle = map_value(center_x, 0, frame.shape[1], 0, 180)
                    tilt_angle = map_value(center_y, 0, frame.shape[0], 0, 180)
                    mirror_pan_angle=mirror_value(pan_angle)
                    mirror_tilt_angle=mirror_value(tilt_angle)

                  #  pan_pin.write(make_positive(mirror_pan_angle+40))
                   # tilt_pin.write(make_positive(mirror_tilt_angle-75))
                    
                    

                for (x, y, w, h) in faces:
                    
                    color = (0, 255, 0) if face_match else (0, 0, 255)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

                    
                    label = "Target" if face_match else "Non-Target"
                    cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            except ValueError:
                pass

        counter += 1

        cv2.imshow("video", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Usage
detect_faces(r'C:\Users\Aadesh\Documents\projects\Shooter\reference.jpg')
