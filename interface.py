from tkinter import *
from PIL import Image
import webbrowser as wb
root=Tk()
root.geometry('200x550')
root.title("websites names that are present:")
def leftClick(event):
    url='https://www.youtube.com'
    wb.get().open_new(url)
name1=Label(root,text="YouTube")
icon=PhotoImage(file="icons8-play-button-48.png")
label=Label(root,image=icon)
name1.bind("<Button-1>",leftClick)
label.bind("<Button-1>",leftClick)
label.pack()
name1.pack()
def leftClick(event):
    url='https://www.google.com'
    wb.get().open_new(url)
name2=Label(root,text="Google")
icon2=PhotoImage(file="icons8-google-48.png")
label2=Label(root,image=icon2)
name2.bind("<Button-1>",leftClick)
label2.bind("<Button-1>",leftClick)
label2.pack()
name2.pack()
def leftClick(event):
    url='https://gaana.com'
    wb.get().open_new(url)
name3=Label(root,text="Gaana")
icon3=PhotoImage(file="Gaana.png")
label3=Label(root,image=icon3)
name3.bind("<Button-1>",leftClick)
label3.bind("<Button-1>",leftClick)
label3.pack()
name3.pack()
def leftClick(event):
    url='https://soundcloud.com'
    wb.get().open_new(url)
name4=Label(root,text="SoundCloud")
icon4=PhotoImage(file="soundcloud (1).png")
label4=Label(root,image=icon4)
name4.bind("<Button-1>",leftClick)
label4.bind("<Button-1>",leftClick)
label4.pack()
name4.pack()
def leftClick(event):
    url='https://en-gb.facebook.com'
    wb.get().open_new(url)
name5=Label(root,text="Facebook")
icon5=PhotoImage(file="Facebook_icon-icons.com_66805.png")
label5=Label(root,image=icon5)
name5.bind("<Button-1>",leftClick)
label5.bind("<Button-1>",leftClick)
label5.pack()
name5.pack()
def leftClick(event):
    url='https://www.flipkart.com'
    wb.get().open_new(url)
name6=Label(root,text="Flipkart")
icon6=PhotoImage(file="flipkart_icon-icons.com_62718.png")
label6=Label(root,image=icon6)
name6.bind("<Button-1>",leftClick)
label6.bind("<Button-1>",leftClick)
label6.pack()
name6.pack()
def leftClick(event):
    url='https://www.amazon.in'
    wb.get().open_new(url)
name7=Label(root,text="Amazon")
icon7=PhotoImage(file="amazon_socialnetwork_19996.png")
label7=Label(root,image=icon7)
name7.bind("<Button-1>",leftClick)
label7.bind("<Button-1>",leftClick)
label7.pack()
name7.pack()
root.mainloop()
def quit(self):
    self.root.destroy()
    return quit(self)
