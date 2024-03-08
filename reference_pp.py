import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from threading import Thread
from face_detect import detect_faces  

class KiwiModel:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Terrorist Input")

        
        style = ttk.Style()
        style.theme_use('clam') 

       
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack()

        
        self.label = ttk.Label(self.frame, text="Select a reference image:", font=('Arial', 14))
        self.label.pack(pady=10)

     
        self.select_button = ttk.Button(self.frame, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)

        self.image_label = ttk.Label(self.frame)
        self.image_label.pack()

        self.root.mainloop()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((300, 300))  
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo 
          
            Thread(target=detect_faces, args=(file_path,)).start()
            print("Image selected:", file_path)

if __name__ == "__main__":
    kiwi_model = KiwiModel()
