from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("image")
root.geometry("1000x1000")
upload = Image.open("image1.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, height=900, width=500)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add images in Tkinter window")
label2.place(x=40, y=360)
root.mainloop()