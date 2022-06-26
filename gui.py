import os
import tkinter

from tkinter import filedialog
root = tkinter.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title("Object Detection")

pwd = tkinter.Label(root, text='')
done_label = tkinter.Label(root, text="Detection is finished")


def browse_files():
    filename = filedialog.askopenfilename(initialdir="/home/asus",
                                          title="Select a File",
                                          filetypes=(("Text files", "*.jpg*"), ("all files", "*.*")))
    pwd.configure(text=filename)
    label_file_explorer.configure(text="File Opened: " + filename)


def real_time():
    os.system('python3 detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source 0')


def image_detect():
    os.system(f'python3 detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source {pwd.cget("text")}')
    done_label.place(x=10, y=100)


def video_detect():
    os.system(f'python3 detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source {pwd.cget("text")}')
    done_label.place(x=10, y=100)


def close():
    root.destroy()


real_time_b = tkinter.Button(root, text="Real-Time", command=real_time)
real_time_b.pack()
real_time_b.place(x=10, y=10)

image_detect_b = tkinter.Button(root, text="Image-detect", command=image_detect)
image_detect_b.pack()
image_detect_b.place(x=110, y=10)

video_detect_b = tkinter.Button(root, text="Video-detect", command=video_detect)
video_detect_b.pack()
video_detect_b.place(x=230, y=10)

button_explore = tkinter.Button(root, text="Browse Files", command=browse_files)
button_explore.place(x=400, y=10)

exit_button = tkinter.Button(root, text="Exit", command=close)
exit_button.place(x=10, y=150)

label_file_explorer = tkinter.Label(root, text="File is not selected")
label_file_explorer.place(x=10, y=50)


root.mainloop()
