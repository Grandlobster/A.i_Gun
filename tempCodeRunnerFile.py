board = pyfirmata.Arduino('COM5')
pan_pin = board.get_pin('d:9:s')  # Digital pin 9 for pan servo
tilt_pin = board.get_pin('d:10:s') 