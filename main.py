from tkinter import *
import urllib.request
import json

key = "AIzaSyC-m-IdnPon4-UQVR1D2PNmw_T9enY3sdg" #Your youtube api key here

def channel_data():
	name = el.get()
	data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + name + "&key=" + key).read()
	sub = json.loads(data)['items'][0]["statistics"]["subscriberCount"]
	total_view = json.loads(data)['items'][0]["statistics"]["viewCount"]
	total_videos = json.loads(data)['items'][0]["statistics"]["videoCount"]
	l2.config(text=sub)
	l4.config(text=total_view)
	l6.config(text=total_videos)


root = Tk()
root.geometry("500x200")
channel_name = StringVar()
el = Entry(root, textvariable=channel_name)
el.grid(row=1,column=2)
bl = Button(root, text="get", command=channel_data)
bl.grid(row=2,column=2)

l1 = Label(root, text="Total number of subscriber : ",font="times 15 bold")
l1.grid(row=4,column=1)
l2 = Label(root, font="times 15 bold")
l2.grid(row=4,column=3)

l3 = Label(root, text="Total number of views : ",font="times 15 bold")
l3.grid(row=6,column=1)
l4 = Label(root, font="times 15 bold")
l4.grid(row=6,column=3)

l5 = Label(root, text="Total number of videos : ",font="times 15 bold")
l5.grid(row=8,column=1)
l6 = Label(root, font="times 15 bold")
l6.grid(row=8,column=3)

root.mainloop()
