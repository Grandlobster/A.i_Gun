import cv2
#import serial
import numpy as np


#arduino = serial.Serial('COM3', 9600)  

# 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture
cap = cv2.VideoCapture(0)

# Function to map values from one range to another
def map_value(value, from_low, from_high, to_low, to_high):
    return int((value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Map face position to servo angles and send to Arduino
        servo_x = map_value(x + w // 2, 0, frame.shape[1], 0, 180)
        servo_y = map_value(y + h // 2, 0, frame.shape[0], 0, 180)

        # Send servo angles to Arduino
     #   arduino.write(f'{servo_x},{servo_y}\n'.encode())

    # Display the resulting frame
    cv2.imshow('Face Tracking', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and don't  close all windows
cap.release()
cv2.destroyAllWindows()
