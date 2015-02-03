# -*- coding: utf-8 -*-
import glob
from Tkinter import *
from PIL import Image, ImageTk
"""
Filename: imageLoadandPoint
Author: Sogo
Project title: Yerago image processing
Contribution date: 03/02/2015

Sogang University (c) All rights reserved
"""

# collect images <.jpg>file, in dir_path, and attach label if user wants
def collect_images(dir_path):
    images = glob.glob(dir_path + '/*.jpg')
    # return list of <.jpg> file list
    return images

# Load images and point it out
def load_and_point_images(image_dir, file_path):
    file_name = file_path + '/result.txt'
    f = open(file_name, 'a')
    print '%d images will be tested' % len(image_dir)
    count = 1

    # load each image
    for image_name in image_dir:
        global clickList
        clickList = []
        print '[%4d 번째 파일] %s' % (count, image_name)
        count += 1
        # setting up a tkinter canvas with scrollbars
        frame = Frame(Tk(), bd=2, relief=SUNKEN)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        xscroll = Scrollbar(frame, orient=HORIZONTAL)
        xscroll.grid(row=1, column=1, sticky=E+W)
        yscroll = Scrollbar(frame)
        yscroll.grid(row=1, column=1, sticky=N+S)
        canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        canvas.grid(row=0, column=0, sticky=N+S+E+W)
        xscroll.config(command=canvas.xview())
        yscroll.config(command=canvas.yview())
        frame.pack(fill=BOTH, expand=1)

        # adding the image
        img = ImageTk.PhotoImage(Image.open(image_name))
        canvas.create_image(0, 0, image=img, anchor="nw")
        canvas.config(scrollregion=canvas.bbox(ALL))

        # when click event happened
        def mouseClick(event):
            canvas.create_rectangle(event.x-5, event.y-5, event.x, event.y,
                                    fill="#f50")
            clickList.append(event.x)
            clickList.append(event.y)
            print "clicked at: ", event.x, event.y

        # when mouse right button clicked
        canvas.bind("<Button-1>", mouseClick)
        mainloop()
        sentance = "%s " % image_name
        sentance += str(clickList)
        sentance += "\n"
        f.write(sentance)
        print clickList
    f.close()