import tkinter
import os
from PIL import ImageTk,Image #adds pillow which supports current image types

root = tkinter.Tk()
root.title('Image Viewer')
root.iconbitmap('image viewer.ico')
view_index = 0

def rbutton_click():
    global view_index,current_image
    if view_index + 1 == len(img_list):
        view_index = 0
    else:
        view_index += 1
    current_image.grid_forget()
    current_image = tkinter.Label(root,image=img_list[view_index])
    current_image.grid(row=0, column=0, columnspan=3)
    status_bar = tkinter.Label(root, text=f'Image {view_index+1} of {str(len(img_list))}', bd=1, relief="sunken", anchor="e")
    status_bar.grid(row=2, column=0, sticky="ew", columnspan=3)


def lbutton_click():
    global view_index,current_image
    if view_index == 0:
        view_index = len(img_list)-1
    else:
        view_index -= 1
    current_image.grid_forget()
    current_image = tkinter.Label(root,image=img_list[view_index])
    current_image.grid(row=0, column=0, columnspan=3)
    status_bar = tkinter.Label(root, text=f'Image {view_index+1} of {str(len(img_list))}', bd=1, relief="sunken", anchor="e")
    status_bar.grid(row=2, column=0, sticky="ew", columnspan=3)

img_location=[]
for filename in os.listdir("images"):
    img_location.append("images/" + filename)

img_list=[]
for img in img_location:
    my_img = ImageTk.PhotoImage(Image.open(img))
    img_list.append(my_img)

current_image = tkinter.Label(root,image=img_list[view_index])
right_button = tkinter.Button(root, text='>>', height=2, width=8, command=rbutton_click)
left_button = tkinter.Button(root, text='<<', height=2, width=8, command=lbutton_click)
status_bar = tkinter.Label(root, text=f'Image {view_index+1} of {str(len(img_list))}', bd=1, relief="sunken", anchor="e")

current_image.grid(row=0, column=0, columnspan=3)
left_button.grid(row=1, column=0, pady=10)
right_button.grid(row=1, column=2)
status_bar.grid(row=2, column=0, sticky="ew", columnspan=3)
root.mainloop()
