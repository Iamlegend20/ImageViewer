import tkinter
from PIL import ImageTk,Image #adds pillow which supports current image types

root = tkinter.Tk()
root.title('Image Viewer')
#root.iconbitmap('Image Viewer.ico')

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

    
my_img1 = ImageTk.PhotoImage(Image.open("images/mario.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/luigi.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/peach.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/yoshi.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/bowser.jpg"))
img_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

view_index = 0
my_label = tkinter.Label(root,image=img_list[view_index])
right_button = tkinter.Button(root, text='>>', command=rbutton_click)
left_button = tkinter.Button(root, text='<<', command=lbutton_click)

my_label.grid(row=0, column=0, columnspan=3)
left_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)
root.mainloop()
