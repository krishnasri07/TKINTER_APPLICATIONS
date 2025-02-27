import tkinter as tk
import random
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk


win = tk.Tk()
win.geometry("500x500")
win.title("IIITDMK")
win.attributes('-alpha', 0.999)
win.iconphoto(False, tk.PhotoImage(file="img_1.png"))

# Creating a photoimage object to use image
#photo = tk.PhotoImage(file="cal.png")
photo1 = tk.PhotoImage(file="Q&A.png")
photo2 = tk.PhotoImage(file="gpa.png")
photo3 = tk.PhotoImage(file="gallery.png")
photo4 = tk.PhotoImage(file="todo.png")
bg = tk.PhotoImage(file="img_4.png")
# Add Image inside the Canvas
canvas = tk.Canvas(win, width=750, height=3500)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')


# Function to resize the window
def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("img_4.png")
    # resize the image with width and height of child3
    resized = image.resize((e.width, e.height), Image.LANCZOS)

    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')


def gpa_func():
    child1 = tk.Toplevel(win)
    child1.title("GPA")
    child1.geometry("700x350")
    child1.iconphoto(False, tk.PhotoImage(file="gpa.png"))
    e1 = tk.Entry(child1)
    e3 = tk.Entry(child1)
    e4 = tk.Entry(child1)
    e5 = tk.Entry(child1)
    e6 = tk.Entry(child1)
    e7 = tk.Entry(child1)
    e8 = tk.Entry(child1)
    e9 = tk.Entry(child1)
    e10 = tk.Entry(child1)
    e11 = tk.Entry(child1)
    e12 = tk.Entry(child1)
    e13 = tk.Entry(child1)
    l = ["S", "A", "B", "C", "D", "E", "P", "U"]
    l1 = ["H", "U"]

    def display():
        global tot
        tot = 0
        if e4.get().upper().upper() == "S":
            tk.Label(child1, text="3").grid(row=3, column=4)
            tot += 30
        if e4.get().upper() == "A":
            tk.Label(child1, text="3").grid(row=3, column=4)
            tot += 27
        if e4.get().upper() == "B":
            tk.Label(child1, text="3").grid(row=3, column=4)
            tot += 24
        if e4.get().upper() == "C":
            tk.Label(child1, text="3").grid(row=3, column=4)
            tot += 21
        if e4.get().upper() == "D":
            tk.Label(child1, text="3").grid(row=3, column=4)
            tot += 18
        if e4.get().upper() == "E":
            tk.Label(child1, text="3").grid(row=3, column=4)
            tot += 15
        if e4.get().upper() == "P":
            tk.Label(child1, text="3").grid(row=3, column=4)
            tot += 12
        if e4.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=3, column=4)
            tot += 0
        if e4.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for first subject.")
        if e5.get().upper() == "S":
            tk.Label(child1, text="3").grid(row=4, column=4)
            tot += 30
        if e5.get().upper() == "A":
            tk.Label(child1, text="3").grid(row=4, column=4)
            tot += 27
        if e5.get().upper() == "B":
            tk.Label(child1, text="3").grid(row=4, column=4)
            tot += 24
        if e5.get().upper() == "C":
            tk.Label(child1, text="3").grid(row=4, column=4)
            tot += 21
        if e5.get().upper() == "D":
            tk.Label(child1, text="3").grid(row=4, column=4)
            tot += 18
        if e5.get().upper() == "E":
            tk.Label(child1, text="3").grid(row=4, column=4)
            tot += 15
        if e5.get().upper() == "P":
            tk.Label(child1, text="3").grid(row=4, column=4)
            tot += 12
        if e5.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=4, column=4)
            tot += 0
        if e5.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for second subject.")
        if e6.get().upper() == "S":
            tk.Label(child1, text="2").grid(row=5, column=4)
            tot += 20
        if e6.get().upper() == "A":
            tk.Label(child1, text="2").grid(row=5, column=4)
            tot += 18
        if e6.get().upper() == "B":
            tk.Label(child1, text="2").grid(row=5, column=4)
            tot += 16
        if e6.get().upper() == "C":
            tk.Label(child1, text="2").grid(row=5, column=4)
            tot += 14
        if e6.get().upper() == "D":
            tk.Label(child1, text="2").grid(row=5, column=4)
            tot += 12
        if e6.get().upper() == "E":
            tk.Label(child1, text="2").grid(row=5, column=4)
            tot += 10
        if e6.get().upper() == "P":
            tk.Label(child1, text="2").grid(row=5, column=4)
            tot += 8
        if e6.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=5, column=4)
            tot += 0
        if e6.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for third subject.")
        if e7.get().upper() == "H":
            tk.Label(child1, text="PASS").grid(row=6, column=4)
            tot += 0
        if e7.get().upper() == "U":
            tk.Label(child1, text="FAIL").grid(row=6, column=4)
            tot += 0
        if e7.get().upper() not in l1:
            messagebox.showerror("warning", "Please enter valid grade for fourth subject.")
        if e8.get().upper() == "S":
            tk.Label(child1, text="3").grid(row=7, column=4)
            tot += 30
        if e8.get().upper() == "A":
            tk.Label(child1, text="3").grid(row=7, column=4)
            tot += 27
        if e8.get().upper() == "B":
            tk.Label(child1, text="3").grid(row=7, column=4)
            tot += 24
        if e8.get().upper() == "C":
            tk.Label(child1, text="3").grid(row=7, column=4)
            tot += 21
        if e8.get().upper() == "D":
            tk.Label(child1, text="3").grid(row=7, column=4)
            tot += 18
        if e8.get().upper() == "E":
            tk.Label(child1, text="3").grid(row=7, column=4)
            tot += 15
        if e8.get().upper() == "P":
            tk.Label(child1, text="3").grid(row=7, column=4)
            tot += 12
        if e8.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=7, column=4)
            tot += 0
        if e8.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for fifth subject.")
        if e9.get().upper() == "S":
            tk.Label(child1, text="2").grid(row=8, column=4)
            tot += 20
        if e9.get().upper() == "A":
            tk.Label(child1, text="2").grid(row=8, column=4)
            tot += 18
        if e9.get().upper() == "B":
            tk.Label(child1, text="2").grid(row=8, column=4)
            tot += 16
        if e9.get().upper() == "C":
            tk.Label(child1, text="2").grid(row=8, column=4)
            tot += 14
        if e9.get().upper() == "D":
            tk.Label(child1, text="2").grid(row=8, column=4)
            tot += 12
        if e9.get().upper() == "E":
            tk.Label(child1, text="2").grid(row=8, column=4)
            tot += 10
        if e9.get().upper() == "P":
            tk.Label(child1, text="2").grid(row=8, column=4)
            tot += 8
        if e9.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=8, column=4)
            tot += 0
        if e9.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for sixth subject.")
        if e10.get().upper() == "S":
            tk.Label(child1, text="3").grid(row=9, column=4)
            tot += 30
        if e10.get().upper() == "A":
            tk.Label(child1, text="2").grid(row=9, column=4)
            tot += 27
        if e10.get().upper() == "B":
            tk.Label(child1, text="3").grid(row=9, column=4)
            tot += 24
        if e10.get().upper() == "C":
            tk.Label(child1, text="3").grid(row=9, column=4)
            tot += 21
        if e10.get().upper() == "D":
            tk.Label(child1, text="3").grid(row=9, column=4)
            tot += 18
        if e10.get().upper() == "E":
            tk.Label(child1, text="3").grid(row=9, column=4)
            tot += 15
        if e10.get().upper() == "P":
            tk.Label(child1, text="3").grid(row=9, column=4)
            tot += 12
        if e10.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=9, column=4)
            tot += 0
        if e10.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for seventh subject.")

        if e11.get().upper() == "S":
            tk.Label(child1, text="2").grid(row=10, column=4)
            tot += 20
        if e11.get().upper() == "A":
            tk.Label(child1, text="2").grid(row=10, column=4)
            tot += 18
        if e11.get().upper() == "B":
            tk.Label(child1, text="2").grid(row=10, column=4)
            tot += 16
        if e11.get().upper() == "C":
            tk.Label(child1, text="2").grid(row=10, column=4)
            tot += 14
        if e11.get().upper() == "D":
            tk.Label(child1, text="2").grid(row=10, column=4)
            tot += 12
        if e11.get().upper() == "E":
            tk.Label(child1, text="2").grid(row=10, column=4)
            tot += 10
        if e11.get().upper() == "P":
            tk.Label(child1, text="2").grid(row=10, column=4)
            tot += 8
        if e11.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=10, column=4)
            tot += 0
        if e11.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for eighth subject.")
        if e12.get().upper() == "S":
            tk.Label(child1, text="3").grid(row=11, column=4)
            tot += 30
        if e12.get().upper() == "A":
            tk.Label(child1, text="3").grid(row=11, column=4)
            tot += 27
        if e12.get().upper() == "B":
            tk.Label(child1, text="3").grid(row=11, column=4)
            tot += 24
        if e12.get().upper() == "C":
            tk.Label(child1, text="3").grid(row=11, column=4)
            tot += 21
        if e12.get().upper() == "D":
            tk.Label(child1, text="3").grid(row=11, column=4)
            tot += 18
        if e12.get().upper() == "E":
            tk.Label(child1, text="3").grid(row=11, column=4)
            tot += 15
        if e12.get().upper() == "P":
            tk.Label(child1, text="3").grid(row=11, column=4)
            tot += 12
        if e12.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=11, column=4)
            tot += 0
        if e12.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for ninth subject.")

        if e13.get().upper() == "S":
            tk.Label(child1, text="2").grid(row=12, column=4)
            tot += 20
        if e13.get().upper() == "A":
            tk.Label(child1, text="2").grid(row=12, column=4)
            tot += 18
        if e13.get().upper() == "B":
            tk.Label(child1, text="2").grid(row=12, column=4)
            tot += 16
        if e13.get().upper() == "C":
            tk.Label(child1, text="2").grid(row=12, column=4)
            tot += 14
        if e13.get().upper() == "D":
            tk.Label(child1, text="2").grid(row=12, column=4)
            tot += 12
        if e13.get().upper() == "E":
            tk.Label(child1, text="2").grid(row=12, column=4)
            tot += 10
        if e13.get().upper() == "P":
            tk.Label(child1, text="2").grid(row=12, column=4)
            tot += 8
        if e13.get().upper() == "U":
            tk.Label(child1, text="0").grid(row=12, column=4)
            tot += 0
        if e13.get().upper() not in l:
            messagebox.showerror("warning", "Please enter valid grade for tenth subject.")
        tot=tot/23
        tk.Label(child1, text=str('%.2f'%tot)).grid(row=14, column=4)

    tk.Label(child1, text="Name").grid(row=0, column=0)

    tk.Label(child1, text="Roll.No").grid(row=1, column=0)

    tk.Label(child1, text="S.No").grid(row=2, column=0)
    tk.Label(child1, text="1").grid(row=3, column=0)
    tk.Label(child1, text="2").grid(row=4, column=0)
    tk.Label(child1, text="3").grid(row=5, column=0)
    tk.Label(child1, text="4").grid(row=6, column=0)
    tk.Label(child1, text="5").grid(row=7, column=0)
    tk.Label(child1, text="6").grid(row=8, column=0)
    tk.Label(child1, text="7").grid(row=9, column=0)
    tk.Label(child1, text="8").grid(row=10, column=0)
    tk.Label(child1, text="9").grid(row=11, column=0)
    tk.Label(child1, text="10").grid(row=12, column=0)

    tk.Label(child1, text="Subject").grid(row=2, column=1)
    tk.Label(child1, text="PP AD101").grid(row=3, column=1)
    tk.Label(child1, text="TDM AD102").grid(row=4, column=1)
    tk.Label(child1, text="PPP AD103").grid(row=5, column=1)
    tk.Label(child1, text="EED DS104").grid(row=6, column=1)
    tk.Label(child1, text="EEM DS108").grid(row=7, column=1)
    tk.Label(child1, text="EEMP DS109").grid(row=8, column=1)
    tk.Label(child1, text="MEFA DS110").grid(row=9, column=1)
    tk.Label(child1, text="HSTI DS112").grid(row=10, column=1)
    tk.Label(child1, text="BEEE EC101").grid(row=11, column=1)
    tk.Label(child1, text="IDS ME106").grid(row=12, column=1)

    tk.Label(child1, text="Grade").grid(row=2, column=2)
    e4.grid(row=3, column=2)
    e5.grid(row=4, column=2)
    e6.grid(row=5, column=2)
    e7.grid(row=6, column=2)
    e8.grid(row=7, column=2)
    e9.grid(row=8, column=2)
    e10.grid(row=9, column=2)
    e11.grid(row=10, column=2)
    e12.grid(row=11, column=2)
    e13.grid(row=12, column=2)

    tk.Label(child1, text="Credit").grid(row=2, column=3)
    tk.Label(child1, text="3").grid(row=3, column=3)
    tk.Label(child1, text="3").grid(row=4, column=3)
    tk.Label(child1, text="2").grid(row=5, column=3)
    tk.Label(child1, text="0").grid(row=6, column=3)
    tk.Label(child1, text="3").grid(row=7, column=3)
    tk.Label(child1, text="2").grid(row=8, column=3)
    tk.Label(child1, text="3").grid(row=9, column=3)
    tk.Label(child1, text="2").grid(row=10, column=3)
    tk.Label(child1, text="3").grid(row=11, column=3)
    tk.Label(child1, text="2").grid(row=12, column=3)
    tk.Label(child1, text="Credit obtained").grid(row=2, column=4)

    e1.grid(row=0, column=1)
    e3.grid(row=1, column=1)

    button1 = tk.Button(child1, text="Submit", bg="salmon", command=display)
    child1.bind('<Return>', lambda event: display())
    button1.grid(row=14, column=1)

    tk.Label(child1, text="SGPA: ").grid(row=14, column=3)


def To_do_func():
    def newTask():
        task = my_entry.get()
        if task != "":
            lb.insert(END, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("warning", "Please enter some task.")

    def remove_item():
        selected_checkboxs = lb.curselection()

        for selected_checkbox in selected_checkboxs[::-1]:
            lb.delete(selected_checkbox)

    child2 = tk.Toplevel(win)
    child2.geometry('500x450+1000+500')
    child2.title('TO-Do List')
    child2.config(bg='#223441')
    child2.resizable(width=False, height=False)
    child2.iconphoto(False, tk.PhotoImage(file="todo.png"))
    child2.geometry('%dx%d+%d+%d' % (500, 500, 500, 200))

    frame = Frame(child2)
    frame.pack(pady=10)
    sb = Scrollbar(frame)
    sb1 = Scrollbar(frame, orient='horizontal')
    lb = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none",
        selectmode='multiple',
        yscrollcommand=sb.set,
        xscrollcommand=sb1.set
    )
    task_list = [
        'Eat apple',
        'drink water',
        'go gym',
        'write software',
        'write documentation',
        'take a nap',
        'Learn something',
        'paint canvas'
    ]

    for item in task_list:
        lb.insert(END, item)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    sb1.config(command=lb.xview)
    lb.config(xscrollcommand=sb1.set)
    sb1.pack(side=BOTTOM, fill='x')
    lb.pack(side=LEFT, fill=BOTH)
    sb.pack(side=RIGHT, fill=BOTH)

    my_entry = Entry(
        child2,
        font=('times', 24)
    )
    my_entry.pack(pady=20)

    button_frame = Frame(child2)
    button_frame.pack(pady=20)

    addTask_btn = Button(
        button_frame,
        text='Add Task',
        font=('times 14'),
        bg='#c5f776',
        padx=20,
        pady=10,
        command=newTask
    )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
    child2.bind('<Return>', lambda event: newTask())
    delTask_btn = Button(
        button_frame,
        text='Delete Task',
        font=('times 14'),
        bg='#ff8b61',
        padx=20,
        pady=10,
        command=remove_item
    )
    delTask_btn.pack(fill=BOTH, expand=True)


def gallery_func():
    global j
    child3 = tk.Toplevel(win)# creating the required child3  
#child3.resizable() # geometry of the child3  
    child3.geometry("1000x1000")
    child3.iconphoto(False, tk.PhotoImage(file="gallery.png"))
    child3.title('College gallery') # title of the child3
    Label(child3, text = "IIITDM Kurnool", font = ('bold', 20)).pack() # label
   
#creating the required frame  
    frames = Frame(child3, width = 800, height = 200, bg = 'white')  
    frames.pack()  
  
# creating the two, next and back buttons  
# The back button, to move to previous image  

# assigning a variable for each image to be stored  
    img1 = ImageTk.PhotoImage(Image.open("p01.png"))
    img2 = ImageTk.PhotoImage(Image.open("p02.png"))
    img3 = ImageTk.PhotoImage(Image.open("p03.png"))
    img4 = ImageTk.PhotoImage(Image.open("p1.png"))
    img5 = ImageTk.PhotoImage(Image.open("p2.png"))
    img6 = ImageTk.PhotoImage(Image.open("p3.png"))
    img7 = ImageTk.PhotoImage(Image.open("p4.png"))
    img8 = ImageTk.PhotoImage(Image.open("p5.png"))
    img9 = ImageTk.PhotoImage(Image.open("p6.png"))
    img10 = ImageTk.PhotoImage(Image.open("p7.png"))
    img11 = ImageTk.PhotoImage(Image.open("p8.png"))
    img12= ImageTk.PhotoImage(Image.open("p9.png"))
    img13 = ImageTk.PhotoImage(Image.open("p10.png"))
    img14 = ImageTk.PhotoImage(Image.open("p11.png"))
    img15= ImageTk.PhotoImage(Image.open("p12.png"))
    img16 = ImageTk.PhotoImage(Image.open("p13.png"))
    img17 = ImageTk.PhotoImage(Image.open("p14.png"))
    img18 = ImageTk.PhotoImage(Image.open("p15.png"))
    img19 = ImageTk.PhotoImage(Image.open("p16.png"))
    img20 = ImageTk.PhotoImage(Image.open("p17.png"))
    img21 = ImageTk.PhotoImage(Image.open("p18.png"))
    img22 = ImageTk.PhotoImage(Image.open("p19.png"))
    img23 = ImageTk.PhotoImage(Image.open("p20.png"))
    img24 = ImageTk.PhotoImage(Image.open("p21.png"))
    img25 = ImageTk.PhotoImage(Image.open("p22.png"))
    img26 = ImageTk.PhotoImage(Image.open("p23.png"))
    img27 = ImageTk.PhotoImage(Image.open("p24.png"))
    img28 = ImageTk.PhotoImage(Image.open("p25.png"))
    img29 = ImageTk.PhotoImage(Image.open("p26.png"))
    img30 = ImageTk.PhotoImage(Image.open("p27.png"))
    img31 = ImageTk.PhotoImage(Image.open("p28.png"))
    img32 = ImageTk.PhotoImage(Image.open("p29.png"))
    img33 = ImageTk.PhotoImage(Image.open("p30.png"))
    img34 = ImageTk.PhotoImage(Image.open("p31.png"))
    img35 = ImageTk.PhotoImage(Image.open("p32.png"))
    img36 = ImageTk.PhotoImage(Image.open("p33.png"))
    img37 = ImageTk.PhotoImage(Image.open("p34.png"))
    img38 = ImageTk.PhotoImage(Image.open("p35.png"))
    img39 = ImageTk.PhotoImage(Image.open("p36.png"))
    img40 = ImageTk.PhotoImage(Image.open("p37.png"))


   
# adding all the images to a list  
    imglst = [img1, img2, img3,img40,img4,img5, img6, img7,img8,img9, img10, img11,img12,img13, img14, img15,img16,img17, img18, img19,img20,img21, img22, img23,img24,img25, img26, img27,img28,img29, img30, img31,img32,img33, img34, img35,img36,img37, img38,img39]
    j = 0  
    img_label = Label(frames, image = imglst[j])   
  
# packing the images into the child3  
    img_label.pack(padx=40)  
  
# defining a forward function to be called when next image is to be displayed  
    def Forward():  
        global j # creating a global variable j  
        j = j + 1  
        try:  
            img_label.config(image = imglst[j])  
        except:  
            j = -1  
            Forward() # calling the forward function  
  
# defining a backward function to be called when next image is to be displayed  
    def Backward():  
        global j # creating a global variable j  
  
        j = j - 1  
        try:  
            img_label.config(image = imglst[j])  
        except:  
            j = 0  
            Backward() # calling the forward function  
    Button(frames, text = 'Back', command = Backward ).pack(side="left")  
    
# The next button, to move to next image  
    Button(frames, text = 'Next', command = Forward).pack(side="right")
    child3.bind('<Left>', lambda event: Backward())
    child3.bind('<Right>', lambda event: Forward())

def chatbot():
    child4 = tk.Toplevel(win)
    child4.title("FAQs")
    child4.iconphoto(False, tk.PhotoImage(file="Q&A.png"))
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    def send():
        send1 = "You -> " + e.get()
        txt.insert(END, "\n" + send1)

        user = e.get().lower()
        joke=["Bot -> What did the buffalo say when his son left for college? Bison.! ",
              "Bot ->  I failed math so many times at school, I can’t even count.",
              "Bot -> The proudest moment of any student:You know nothing and the teacher says: 'hide your answer sheet, the boy behind you is copying you.'",
              "Bot -> Why is it a waste to study history? Because there is no future in it.",
              "Bot -> How do I sleep the night before any exam? I sleep next to my notes, sincerely hoping they transfer into my brain by osmosis.",
              "Bot -> Why do old people start reading the holy books more often? They are studying for their final exam",
              "Bot -> Never drink water while studying .It’ll dilute your concentration ",
              "Bot -> People like studying gravity.Maybe that’s because it’s a really attractive field."]

        if ("hello" in user):
            txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

        elif ("hi" in user):
            txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

        elif ("how are you" in user):
            txt.insert(END, "\n" + "Bot -> fine! and you")

        elif ("fine" in user or "i am good" in user or "i am doing good" in user):
            txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

        elif ("thanks" in user or "thank you" in user or "now its my time" in user):
            txt.insert(END, "\n" + "Bot -> My pleasure !")
        elif ("tell me a joke" in user or "tell me something funny" in user or "crack a funny line" in user):
            txt.insert(END, "\n" + random.choice(joke))
        elif ("bye" in user or "quit" in user or "leave" in user):
            txt.insert(END, "\n" + "Bot -> Have a nice day!")
        elif (("about iiitdm " in user ) or "iitdm kurnool" in user):
            txt.insert(END, "\n" + "Bot -> Indian Institute of Information Technology, Design & Manufacturing, Kurnool (IIITDMK) was announced in 2014 . IIITDM Kurnool is fully funded by Ministry of Education.")
        elif ("director" in user or "somayajulu" in user or "director of iiitdmk" in user ):
            txt.insert(END, "\n" + "Bot -> DIRECTOR of IIITDMK : PROF. D V L N SOMAYAJULU.Prof. Somayajulu has 33 years of experience in teaching, research, consultancy and outreach in the field of Computer Science and Engineering.   To contact : 08518 – 289114,,director@iiitk.ac.in")
        elif ("visitor" in user ):
            txt.insert(END, "\n" + "Bot -> The Honourable President of India, Smt. Droupadi Murmu  is the Visitor of our Institute. ")
        elif ("chairperson" in user):
            txt.insert(END, "\n" + "Bot -> PROFESSOR H.A. RANGANATH (Hassan Annegowda Ranganath)")
        elif ("board of governors" in user or "board members" in user or "board of iiitdm" in user):
            txt.insert(END, "\n" + "Bot ->(1.)PROF.H.A.RANGANATH,(2.)SHRI.J.SYAMALA RAO,IAS ,(3.)SMT.SAUMYA GUPTA,IAS ,(4.)SHRI.BHUVNESH KUMAR,(5.)PROF.K.N.SATYANARAYANA,(6.)PROF.M.CHANDRASEKHAR,(7.)SHRI.VENKATA NARASIMHAM PERI,(8.)PROF.N.V.RAMANA RAO,(9.)SMT.SASHI SAIRAMAN,(10.)PROF.SANDEEP SANCHETI,(11.)PROF.P.NAGABHUSHAN,(12.)PROF.DVLN SOMAYAJULU,(13.)SHRI KYATHARI GURUMURTHY")
        elif ("codetantra" in user or "online class" in user ):
            txt.insert(END, "\n" + "Bot -> Open browser->search for https://iiitk.ac.in/ -> click on Other Links -> click on Online class - Codetantra -> login in with your given college Id -> Then you can listen to your online classes.")
        elif ("moodle" in user or "eabyas" in user ):
            txt.insert(END, "\n" + "Bot -> Open browser->search for https://iiitk.ac.in/ -> click on Other Links -> click on Moodle -eabyas -> login with your given college Id -> Then you can view your class assignments and notes sent by your professors")
        elif ("academic calendar" in user ):
            txt.insert(END, "\n" + "Bot ->  Open browser->search for https://iiitk.ac.in/ -> click on Academics -> There you can see the academic calendar -> download to view the academic calendar")
        elif ("holidays" in user ):
            txt.insert(END, "\n" + "Bot ->  Open browser->search for https://iiitk.ac.in/ -> click on Academics -> There you can see the Holidays list of this year -> download to view the holidays list")
        elif ("timetable" in user or "schedule" in user ):
            txt.insert(END, "\n" + "Bot ->  Open browser->search for https://iiitk.ac.in/ -> click on Academics -> There you can see the Timetable -> download to view the Timetable")
        elif ("cse syllabus" in user or "cse schema" in user or "computer science and engineering syllabus" in user):
            txt.insert(END, "\n" + "Bot ->  Open browser->search for https://iiitk.ac.in/ -> click on Academics -> click on departments -> click on computer science and engineering -> to the down of the page u can see year wise syllabus and schema -> click on them to download the syallbus ")
        elif ("ece syllabus" in user or "ece schema" in user or "electronics and communication engineering syllabus" in user):
            txt.insert(END, "\n" + "Bot -> Open browser->search for https://iiitk.ac.in/ -> click on Academics -> click on departments -> click on electronics and communication engineering -> to the down of the page u can see year wise syllabus and schema -> click on them to download the syallbus")
        elif ("mech syllabus" in user or "mech schema" in user or "mechanical engineering syllabus" in user):
            txt.insert(END, "\n" + "Bot -> Open browser->search for https://iiitk.ac.in/ -> click on Academics -> click on departments -> click on mechanical engineering -> to the down of the page u can see year wise syllabus and schema -> click on them to download the syallbus")
        else:
            txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

        e.delete(0, END)
    global Hsrl,Vsrl
    label = Label(child4, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20,height=1).grid(row=0)

    txt = Text(child4, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=100)
    txt.grid(row=1, column=0, columnspan=2)
    scrollbar = Scrollbar(txt)
    #scrollbar1 = Scrollbar(txt)
    scrollbar.place(relheight=0.1, relx=1.0)
    #scrollbar1.place(relwidth=1, rely=0.974)

    e = Entry(child4, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=95)
    e.grid(row=2, column=0)
    send1 = Button(child4, text="Send", font=FONT_BOLD, bg=BG_GRAY,command=send).grid(row=2, column=1)
    child4.bind('<Return>', lambda event: send())


button1 = Button(win, text='Gallery', image=photo3, compound=TOP, command=gallery_func)
button2 = Button(win, text='GPA Calculator', image=photo2, compound=TOP, command=gpa_func)
button3 = Button(win, text='TO Do list', image=photo4, compound=TOP, command=To_do_func)
button4 = Button(win, text="FAQs about IIITDMK", image=photo1, compound=TOP, command=chatbot)
button1_canvas = canvas.create_window(100, 100, anchor="nw", window=button1)

button2_canvas = canvas.create_window(350, 100, anchor="nw", window=button2)

button3_canvas = canvas.create_window(100, 300, anchor="nw", window=button3)
button4_canvas = canvas.create_window(350, 300, anchor="nw", window=button4)

# Bind the function to configure the parent window
win.bind("<Configure>", resize_image)
win.mainloop()
