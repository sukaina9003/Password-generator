from PIL import Image, ImageTk
import tkinter as  tk
import random
import string


def generate_password():
    password_length = int(length_entry.get())
    if password_length < 6:
        password_display.config(text="Password length must be at least 6 characters.")
        return
    elif password_length > 128:
        password_display.config(text="Password length is too long.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_display.config(text=password)




# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("730x530")
root.configure(bg="light blue")



canvas =tk.Canvas(root, width=650, height=550, bg="light blue")
filename=tk.PhotoImage(file="C:\\Users\\HP\\Desktop\\Capture.PNG") 
back_ground_label=tk.Label(root,image=filename)
back_ground_label.place(x=0,y=0 ,relwidth=1,relheight=1)




# Mention the title of the app
title_label =tk.Label(root, text=" Password Generator",bd=2,borderwidth=2, relief="sunken" , font=('Times', 29))
title_label.pack(pady=32)



# Create and place widgets
length_label = tk.Label(root, text="Password Length:",relief="sunken",font=('Times',14))
length_label.pack(pady=22)



length_entry = tk.Entry(root)
length_entry.pack(pady=2)


generate_button = tk.Button(root, text="Generate Password", command=generate_password,relief="sunken",font=('Times', 14))
generate_button.pack(pady=16)

password_display = tk.Label(root, text="",font=('Times',12))
password_display.pack(pady=15)
canvas.pack()
# Start the Tkinter main loop
root.mainloop()
