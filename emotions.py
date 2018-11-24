import cv2
import numpy as np
import winsound
from keras.models import load_model
from statistics import mode
from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input
from tkinter import *
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from PIL import Image, ImageTk
from pygame import mixer # Load the required library
import time
import tkinter



USE_WEBCAM = True # If false, loads video file source

# parameters for loading data and images
emotion_model_path = './models/emotion_model.hdf5'
emotion_labels = get_labels('fer2018')

# hyper-parameters for bounding boxes shape
frame_window = 10
emotion_offsets = (20, 40)

# loading models
face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
emotion_classifier = load_model(emotion_model_path)

# getting input model shapes for inference
emotion_target_size = emotion_classifier.input_shape[1:3]

# starting lists for calculating modes
emotion_window = []


# starting video streaming

cv2.namedWindow('window_frame')
video_capture = cv2.VideoCapture(0)

# Select video or webcam feed
cap = None
if (USE_WEBCAM == True):
    cap = cv2.VideoCapture(0) # Webcam source
else:
    cap = cv2.VideoCapture('./demo/dinner.mp4') # Video file source

while cap.isOpened(): # True:
    ret, bgr_image = cap.read()

    # bgr_image = video_capture.read()[1]

    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    #print( gray_image)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
			minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for face_coordinates in faces:

        x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
        gray_face = gray_image[y1:y2, x1:x2]
        try:
            gray_face = cv2.resize(gray_face, (emotion_target_size))
        except:
            continue

        gray_face = preprocess_input(gray_face, True)
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        emotion_prediction = emotion_classifier.predict(gray_face)
        emotion_probability = np.max(emotion_prediction)
        emotion_label_arg = np.argmax(emotion_prediction)
        emotion_text = emotion_labels[emotion_label_arg]
        emotion_window.append(emotion_text)

        if len(emotion_window) > frame_window:
            emotion_window.pop(0)
        try:
            emotion_mode = mode(emotion_window)
        except:
            continue

        if emotion_text == 'angry':
            color = emotion_probability * np.asarray((255, 0, 0))


            start_time = time.time()
            time.sleep(1.0 - time.time() + start_time)
            pass
            no_dupes = [x for n, x in enumerate(emotion_text) if x not in emotion_text[:n]]


            for v in range(len(no_dupes)):

                if v == 3:
                    pass
                    pass
                    pass
                    print(v)
                    break
                    break
            mixer.init()
            mixer.music.load('D:/r/phyton/Mankatha theme.mp3')
            mixer.music.play()

            top = tkinter.Tk()
            canvas = Canvas(top, width=650, height=550)
            canvas.pack(fill=BOTH, expand=True)
            canvas.create_text(350, 55, text='EMOTION PREDICTON', font=('Helvetica', 21, 'bold'), justify='center', fill='green')
            canvas.update
            load = Image.open("./matrix.PNG")
            load = load.resize((378, 378))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=20, y=100)

            load = Image.open("./ANG_SMY.png")
            load = load.resize((128, 128))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=500, y=250)
            top.after(4000, lambda: top.destroy())  # Destroy the widget after 30 seconds
            top.mainloop()
            top.mainloop()

        elif emotion_text == 'sad':
            color = emotion_probability * np.asarray((0, 0, 255))
            start_time = time.time()
            time.sleep(1.0 - time.time() + start_time)
            mixer.init()
            mixer.music.load('D:/r/phyton/love_me_like_you_do-RingtonesHub-820.mp3')
            mixer.music.play()
            top = tkinter.Tk()
            # Code to add widgets will go here...
            canvas = Canvas(top, width=650, height=550)
            canvas.pack(fill=BOTH, expand=True)
            canvas.create_text(350, 55, text='EMOTION PREDICTON', font=('Helvetica', 21, 'bold'), justify='center',
                               fill='green')
            canvas.update
            load = Image.open("./matrix.PNG")
            load = load.resize((378, 378))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=20, y=100)

            load = Image.open("./SAD_SMY.png")
            load = load.resize((128, 128))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=500, y=250)
            top.after(2000, lambda:top.destroy())  # Destroy the widget after 30 seconds
            top.mainloop()
            top.mainloop()
        elif emotion_text == 'happy':
            color = emotion_probability * np.asarray((255, 255, 0))
            start_time = time.time()
            time.sleep(1.0 - time.time() + start_time)

            mixer.init()
            mixer.music.load('D:/r/phyton/Shape_Of_You_Marimba_Remix.mp3')
            mixer.music.play()

            top = tkinter.Tk()
            # Code to add widgets will go here...
            canvas = Canvas(top, width=650, height=550)
            canvas.pack(fill=BOTH, expand=True)
            canvas.create_text(350, 55, text='EMOTION PREDICTON', font=('Helvetica', 21, 'bold'), justify='center',
                               fill='green')
            canvas.update
            load = Image.open("./matrix.PNG")
            load = load.resize((378, 378))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=20, y=100)

            load = Image.open("./HPY_SMY.png")
            load = load.resize((128, 128))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=500, y=250)
            top.after(1000, lambda:top.destroy())  # Destroy the widget after 30 seconds
            top.mainloop()
            top.mainloop()
        elif emotion_text == 'surprise':
            color = emotion_probability * np.asarray((0, 255, 255))
            start_time = time.time()
            time.sleep(1.0 - time.time() + start_time)

            mixer.init()
            mixer.music.load('D:/r/phyton/Banjaara - Mohammad Irfan_1417348739963.mp3')
            mixer.music.play()
            top = tkinter.Tk()
            # Code to add widgets will go here...
            canvas = Canvas(top, width=650, height=550)
            canvas.pack(fill=BOTH, expand=True)
            canvas.create_text(350, 55, text='EMOTION PREDICTON', font=('Helvetica', 21, 'bold'), justify='center',
                               fill='green')
            canvas.update
            load = Image.open("./matrix.PNG")
            load = load.resize((378, 378))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=20, y=100)

            load = Image.open("./SPS_SMY.png")
            load = load.resize((128, 128))
            render = ImageTk.PhotoImage(load)

            img = tk.Label(top, image=render)
            img.image = render
            img.place(x=500, y=250)
            top.after(1000, lambda:top.destroy())  # Destroy the widget after 30 seconds
            top.mainloop()
            top.mainloop()
        else:
            color = emotion_probability * np.asarray((0, 255, 0))
            # start_time = time.time()
            # time.sleep(1.0 - time.time() + start_time)

        color = color.astype(int)
        color = color.tolist()

        draw_bounding_box(face_coordinates, rgb_image, color)
        draw_text(face_coordinates, rgb_image, emotion_mode,
                  color, 0, -45, 1, 1)

    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)



    cv2.imshow('window_frame', bgr_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break





cap.release()
cv2.destroyAllWindows()



from tkinter import *
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from PIL import Image, ImageTk
# self = Tk()
# self.resizable(width=FALSE, height=FALSE)
# self.geometry('{}x{}'.format(460, 350))
# top_frame = Frame(self, bg='cyan', width = 450, height=50, pady=3)
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.title_font = tkfont.Font(family='Helvetica', size=14, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, bg="green")
        # canvas = container(self, width=650, height=550)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # canvas.update
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageTree, PageFour, PageFive):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.centerWindow()
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def centerWindow(self):
            w = 650
            h = 550
            sw = self.winfo_screenwidth()
            sh = self.winfo_screenheight()
            x = (sw - w) / 2
            y = (sh - h) / 2
            self.geometry('%dx%d+%d+%d' % (w, h, x, y))

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,
                         text="Emotion",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="This software recognizes human faces and \ntheir corresponding emotions from \na video or webcam feed. \nPowered by OpenCV and Deep Learning. ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        # button1 = tk.Button(self, text="NUTRAL", bg="green",
        #                     command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="EMO_ON",
                            command=lambda: controller.show_frame("PageTwo"))
        # button3 = tk.Button(self, text="HAPPY",
        #                     command=lambda: controller.show_frame("PageTree"))
        # button4 = tk.Button(self, text="PRE_PRO",
        #                     command=lambda: controller.show_frame("PageFour"))
        button5 = tk.Button(self, text="AVG_VAL",
                            command=lambda: controller.show_frame("PageFive"))
        # button1.pack()
        button2.pack()
        # button3.pack()
        # button4.pack()
        button5.pack()

        # load = Image.open("./sad.png")
        # render = ImageTk.PhotoImage(load)
        #
        # # labels can be text or images
        # img = tk.Label(self, image=render)
        # img.image = render
        # img.place(x=0, y=0)
        #
        # load = Image.open("./neutral.PNG")
        # load = load.resize((128, 128))
        # render = ImageTk.PhotoImage(load)
        #
        # img = tk.Label(self, image=render)
        # img.image = render
        # img.place(x=500, y=50)
        #
        # load = Image.open("./neutral.PNG")
        # load = load.resize((128, 128))
        # render = ImageTk.PhotoImage(load)
        #
        # img = tk.Label(self, image=render)
        # img.image = render
        # img.place(x=500, y=50)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="nerual", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        load = Image.open("./sad.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        load = Image.open("./neutral.PNG")
        load = load.resize((128, 128))
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=500, y=50)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="EMOTION", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        load = Image.open("./angry2.PNG")
        load = load.resize((258, 258))
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=30, y=40)

        load = Image.open("./happy22.PNG")
        load = load.resize((258, 258))
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=350, y=40)

        load = Image.open("./neutral22.PNG")
        load = load.resize((258, 258))
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=40, y=300)



        load = Image.open("./surprise222.PNG")
        load = load.resize((258, 258))
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=350, y=300)
class PageTree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="START PAGE", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="HOME",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        load = Image.open("./happy.png")
        render = ImageTk.PhotoImage(load)


        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        load = Image.open("./neutral.PNG")
        load = load.resize((228, 228))
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=490, y=50)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
     tk.Frame.__init__(self, parent)
     self.controller = controller
     label = tk.Label(self, text="surprise", font=controller.title_font)
     label.pack(side="top", fill="x", pady=10)
     button = tk.Button(self, text="surprise",
                                   command=lambda: controller.show_frame("StartPage"))
     button.pack()

     load = Image.open("./neutral.PNG")
     load = load.resize((228, 228))
     render = ImageTk.PhotoImage(load)

     img = tk.Label(self, image=render)
     img.image = render
     img.place(x=500, y=50)

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
     tk.Frame.__init__(self, parent)
     self.controller = controller
     label = tk.Label(self, text="MATRIX VALUE", font=controller.title_font)
     label.pack(side="top", fill="x", pady=10)
     button = tk.Button(self, text="HOME",
                                   command=lambda: controller.show_frame("StartPage"))
     button.pack()

     load = Image.open("./matrix.PNG")
     load = load.resize((428, 428))
     render = ImageTk.PhotoImage(load)

     img = tk.Label(self, image=render)
     img.image = render
     img.place(x=100, y=100)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()