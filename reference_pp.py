 import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from threading import Thread
from face_detect import detect_faces  # Assuming the face detection code is saved in a file named face_detect.py

class KiwiModel:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kiwi Model")
        
        self.label = tk.Label(self.root, text="Select a reference image:")
        self.label.pack()

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.select_button = tk.Button(self.root, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.root.mainloop()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((300, 300))  # Resize image for display
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep reference to the image
            # Call detect_faces function in a separate thread
            Thread(target=detect_faces, args=(file_path,)).start()
            print("Image selected:", file_path)

if __name__ == "__main__":
    kiwi_model = KiwiModel()
