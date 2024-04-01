import cv2
from deepface import DeepFace
import tempfile
import pyfirmata
#I dont fucking care about you guys ! professionalism
'''
i cannot asure you that this will be sure because it depends
'''

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


board = pyfirmata.Arduino('COM3')


pan_pin = board.get_pin('d:9:s')  # Digital pin 9 for pan servo
tilt_pin = board.get_pin('d:10:s')  # Digital pin 10 for tilt servo
#trigger pin is not defined ,only after model design

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
          # Convert frame to grayscale for face detection
          gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          faces = face_cascade.detectMultiScale(gray, 1.1, 5)

          for (x, y, w, h) in faces:
            # Crop face region for verification
            face_img = frame[y:y+h, x:x+w]
            temp_img = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
            cv2.imwrite(temp_img.name, face_img)
            if DeepFace.verify(temp_img.name, reference_img_path)['verified']:
              face_match = True
            else:
              face_match = False
            temp_img.close()

          
          if face_match:
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)

            # Map center coordinates to servo angles (adjust ranges as needed)
            pan_angle = map(center_x, 0, frame.shape[1], 0, 180)
            tilt_angle = map(center_y, 0, frame.shape[0], 0, 180)

            
            pan_pin.write(pan_angle)
            tilt_pin.write(tilt_angle)

        except ValueError:
          face_match = False

      counter += 1

      # Display bounding box and label
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
