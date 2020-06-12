import tkinter
import os
from PIL import ImageTk,Image #adds pillow which supports current image types

root = tkinter.Tk()
root.title('Image Viewer')
root.iconbitmap('image viewer.ico')

img_location=[]
for filename in os.listdir("images"):
    img_location.append("images/" + filename)

img_list=[]
for img in img_location:
    my_img = ImageTk.PhotoImage(Image.open(img))
    img_list.append(my_img)

def rbutton_click():
    global view_index,my_label
    if view_index + 1 == len(img_list):
        view_index = 0
    else:
        view_index += 1
    my_label.grid_forget()
    my_label = tkinter.Label(root,image=img_list[view_index])
    my_label.grid(row=0, column=0, columnspan=3)

def lbutton_click():
    global view_index,my_label
    if view_index == 0:
        view_index = len(img_list)-1
    else:
        view_index -= 1
    my_label.grid_forget()
    my_label = tkinter.Label(root,image=img_list[view_index])
    my_label.grid(row=0, column=0, columnspan=3)


view_index = 0
my_label = tkinter.Label(root,image=img_list[view_index])
right_button = tkinter.Button(root, text='>>', command=rbutton_click)
left_button = tkinter.Button(root, text='<<', command=lbutton_click)

my_label.grid(row=0, column=0, columnspan=3)
left_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)
root.mainloop()
