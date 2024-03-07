import cv2
from deepface import DeepFace
import tempfile

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

reference_img = cv2.imread("reference.jpg")

def check_face(frame):
    global face_match
    try:
        temp_img = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        cv2.imwrite(temp_img.name, frame)
        if DeepFace.verify(temp_img.name, "C:/Users/Aadesh/Documents/projects/Shooter/reference.jpg")['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False
    finally:
        temp_img.close()

while True:
    ret, frame = cap.read()
    if ret:
        if counter % 30 == 0:
            try:
                check_face(frame.copy())
            except ValueError:
                pass
        counter += 1
        if face_match:
            cv2.putText(frame, "Terrorist", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "Non-Target", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
