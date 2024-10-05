
#Main Logic
# n = int(input("how many characters do you want"))
# length = int(input("Enter the length of the password"))
# password = ''.join(rd.choices(all_character,k=length))
# print("ansers:" + password)

from tkinter import *
from PIL import Image, ImageTk  # For handling images
import string as st
import random as rd

root = Tk()

root.title("PASSGEN")
root.geometry('600x1200')

#Background Color

bg_color = "#ffffff"  
root.configure(bg=bg_color)





# Functions to handle button click
#function for generating password

def PasswordClicked(password_length):
    all_character = st.ascii_letters + st.digits + st.punctuation
    password = ''.join(rd.choices(all_character, k=password_length))
    finalPassword = ("password : " + password)
    password_text = Text(root, height=1, width=40, bg=bg_color, fg="black", font=('Helvetica', 16), bd=0)
    password_text.insert(END,finalPassword)  # Insert the generated password
    password_text.config(state="normal")  # Ensure it's editable for selecting/copying
    password_text.pack(pady=10,padx=20 )
    
    # Make the Text widget uneditable by the user but selectable
    password_text.config(state="disabled")
    lbl5 = Label(root, bg=bg_color,text=f'password generated Successfully, press start for new password ^ ', font=('helvantica', 12))
    lbl5.pack()
  
def ClickedAgain(mes):
    try:
        password_length = int(mes.get())
        lbl2 = Label(root,  bg=bg_color,text=f"Password length: {password_length}")
        lbl2.pack(pady=10)  # Center and add spacing
        PasswordClicked(password_length)
    except ValueError:
        lbl2 = Label(root, bg=bg_color, text="Invalid input! Please enter a number.")
        lbl2.pack(pady=10)

def Clicked():
    lbl3 = Label(root, text="Enter the length of password:", font=('Helvetica', 12))
    lbl3.pack(pady=10)  # Center and add spacing
    mes = Entry(root, width=10)
    mes.pack(pady=5)
    btn2 = Button(root, text="Generate Password", activebackground="black",fg="white", bg="red", command=lambda: ClickedAgain(mes))
    btn2.pack(pady=10)

# Load the image
image_path =r"./Shield lock.jpg"
image = Image.open(image_path)  # Replace with your image file path
image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image if necessary
img = ImageTk.PhotoImage(image)

# Add the image as the first widget
img_label = Label(root, image=img)
img_label.pack(pady=10)

# Label and Button widgets centered
lbl = Label(root, text="PASSGen: A Password Generator", bg=bg_color ,font=('Helvetica', 16))
lbl.pack(pady=10)

btn = Button(root, text="Start",activebackground="black", fg="white", bg="red", command=Clicked)
btn.pack(pady=10)

root.mainloop()



