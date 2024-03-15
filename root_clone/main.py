import cv2
from deepface import DeepFace
import tempfile

# Load pre-trained face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    counter += 1
    if counter % 2 != 0:  # Process every other frame
        continue

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each detected face
    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]  # Extract face region
        try:
            temp_img = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
            cv2.imwrite(temp_img.name, face_img)

            # Perform face verification
            if DeepFace.verify(temp_img.name, "C:/Users/Aadesh/Documents/projects/Shooter/reference.jpg")['verified']:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0,255), 2)
                cv2.putText(frame, "Terrorist", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                '''
                
                
                '''
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255,0), 2)
                cv2.putText(frame, "Non-Target", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        except ValueError:
            pass
        finally:
            temp_img.close()

    cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()

