import tkinter as tk
import time

from PIL import Image, ImageGrab, ImageTk, ImageEnhance

selection_start_x = 0
selection_start_y = 0

def getstart(event):
    global selection_start_x
    global selection_start_y
    selection_start_x = event.x
    selection_start_y = event.y

def mousemove(event):
    if event.x == selection_start_x or event.y == selection_start_y:
        return
    canvas.delete("selection_area")
    canvas.create_rectangle(selection_start_x, selection_start_y, event.x, event.y, width = 5, outline="red", tag="selection_area")


def getend(event):
    if event.x == selection_start_x or event.y == selection_start_y:
        return
    # print(selection_start_x,selection_start_y,event.x,event.y)
    width_percent = int(round((event.x - selection_start_x) * 100 / screen_width, 0))
    height_percent = int(round((event.y - selection_start_y) * 100 / screen_height, 0))
    x_offset_percent = int(round(selection_start_x * 100 / screen_width, 0))
    y_offset_percent = int(round(selection_start_y * 100 / screen_height, 0))
    print("screen_mapping:")
    print("    width_percent: " + str(width_percent))
    print("    height_percent: " + str(height_percent))
    print("    x_offset_percent: " + str(x_offset_percent))
    print("    y_offset_percent: " + str(y_offset_percent))

    time.sleep(0.5)
    root.destroy()

root = tk.Tk()

root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, width = screen_width, height=screen_height, bg="gray", cursor = "cross")
img = ImageGrab.grab((0, 0, screen_width, screen_height))
brightEnhancer = ImageEnhance.Brightness(img)
imgb = brightEnhancer.enhance(0.5)
im = ImageTk.PhotoImage(imgb)
canvas.create_image(0, 0, image = im, anchor="nw")
canvas.create_text(0, 0, text = "Press 'Esc' to Exit.", fill = "white", font = ("Sans",30), anchor="nw")

canvas.pack()

root.bind("<Button-1>", getstart)
root.bind("<ButtonRelease-1>", getend)
root.bind("<B1-Motion>", mousemove)
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
