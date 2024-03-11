import servo 
import serial 
width =640
height=480
servo_x_position=90
servo_y_position=90
tilt_channel=0
pan_channel=1
mid_face_y=0
mid_face_x=0
mid_screen_y= height // 2
mid_screen_x=width // 2
mid_screen_window= 10
# dont know what does servo moment does 
step_size=1

if face_match==True:
    def track_face(faces):
    if len(faces) > 0:
        x, y, w, h = faces[0]
        mid_face_x = x + (w // 2)
        mid_face_y = y + (h // 2)

        if mid_face_y < (mid_screen_y - mid_screen_window):
            if servo_tilt_position >= 5:
                servo_tilt_position -= step_size
        elif mid_face_y > (mid_screen_y + mid_screen_window):
            if servo_tilt_position <= 175:
                servo_tilt_position += step_size

        if mid_face_x < (mid_screen_x - mid_screen_window):
            if servo_pan_position >= 5:
                servo_pan_position -= step_size
        elif mid_face_x > (mid_screen_x + mid_screen_window):
            if servo_pan_position <= 175:
                servo_pan_position += step_size

def update_servo_positions():
    port.write(bytes([tilt_channel]))  
    port.write(bytes([servo_tilt_position]))
    port.write(bytes([pan_channel]))
    port.write(bytes([servo_pan_position]))
else:
  # DO nothing 
