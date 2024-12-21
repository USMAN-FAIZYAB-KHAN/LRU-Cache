
# _________________________________________   Import _____________________________________________ #

import tkinter
from CTkMessagebox import *
from customtkinter import *
from PIL import Image
from LRU import *

# ________________________________________ LRU Cache GUI __________________________________________ #

root = CTk()
set_appearance_mode("dark")
set_default_color_theme("green")
root.title("LRU Cache")
w = 1200
h = 700
root.geometry(f"{w}x{h}")

#                   __________________________ Import Image __________________________

arrow = CTkImage(Image.open("./GUI images/arrow.png"), size=(65, 150))
right_arrow = CTkImage(Image.open("./GUI images/right-end-arrow.png"), size=(65, 150))
left_arrow = CTkImage(Image.open("./GUI images/left-end-arrow.png"), size=(65, 150))
LRU_image = CTkImage(Image.open("./GUI images/LRU_img.jpg"), size=(1600, 350))

#                      __________________________ Object __________________________

LRU = LRUCache()

#                      _________________________ Set Size __________________________

def set_size():

    def change(value):
        label2 = CTkLabel(frame, text="", text_color="#D40674",
                          font=CTkFont("Time New Roman", size=15, weight="bold"))
        label2.place(relx=0.45, rely=0.66, anchor=tkinter.NW)
        LRU.capacity = round(value, 0)
        label2.configure(text=round(value, 0))

    label_title = CTkLabel(root, text="Welcome To !! LRU Cache",font=CTkFont(family="Arial", size=50, weight="bold"), fg_color="#A40674"
                           , corner_radius=20)
    label_title.place(relx=0.05, rely=.06, relwidth=0.9, relheight=0.3,  anchor=tkinter.NW)

    frame = CTkFrame(root, width=500, height=200, border_color="#A40674", corner_radius=20, border_width=4)
    frame.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    label1 = CTkLabel(frame, text="Select Size", font=CTkFont(family="Time New Roman", size=25))
    label1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    label_line1 = CTkButton(frame, text="", bg_color="#D40674", height=2, anchor="center", width=130,
                            fg_color="#D40674",
                            hover=None)
    label_line1.place(relx=0.37, rely=0.4, anchor=tkinter.NW)

    Slider = CTkSlider(frame, from_=0, to=50, button_color="#D40674", button_hover_color="#A40674", width=300, command=change)
    Slider.place(relx=0.2, rely=0.5, anchor=tkinter.NW)
    Slider.set(0)

    button = CTkButton(root, text="Continue", height=40, width=150, fg_color="#D40674",
                       command=lambda: func(Slider.get(), frame, label_title, button), corner_radius=10, hover_color="#A40674")
    button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

#                        _________________________ Main __________________________

def Main(x):

    frame0 = CTkFrame(root, border_color="#A40674", border_width=4)
    frame0.place(relx=0.01, rely=0.02, relwidth=0.3, relheight=0.96, anchor=tkinter.NW)

    label_res_title = CTkLabel(frame0, text='Miss Rate', font=CTkFont(family="Arial", size=25))
    label_res_title.place(relx=0.5, rely=.15, anchor=tkinter.CENTER)

    label_res = CTkLabel(frame0, text='0.0 %', height=40, fg_color="#D40674", anchor="center",
                         font=CTkFont(family="Time New Roman", size=15), corner_radius=7)
    label_res.place(relx=0.5, rely=0.22, relwidth=0.6, anchor=tkinter.CENTER)

    frame1 = CTkFrame(root, border_color="#A40674", border_width=4,)
    frame1.place(relx=0.33, rely=0.02, relwidth=0.66, relheight=0.96, anchor=tkinter.NW)

    frame3 = CTkFrame(frame1, height=150)
    frame3.place(relx=0.05, rely=0.03, relwidth=0.898, anchor=tkinter.NW)

    label_least_count = CTkLabel(frame3, text="None", height=40, fg_color="#D40674", width=150, corner_radius=10,
                                 font=CTkFont(family="Arial", size=16))
    label_least_count.place(relx=0.18, rely=0.6, anchor=tkinter.CENTER)

    def generate_get(val=None):

        label_return = CTkLabel(frame3, text="Cache Return", font=CTkFont(family="Time New Roman", size=25))
        label_return.place(relx=0.83, rely=0.25, anchor=tkinter.CENTER)

        button_return = CTkButton(frame3, height=40, text="None", fg_color="#D40674", width=150, corner_radius=10,
                                  font=CTkFont(family="Arial", size=16), hover=None)
        button_return.place(relx=0.83, rely=0.6, anchor=tkinter.CENTER)

        if val == -1:
            button_return.configure(text="Not Found")
            CTkMessagebox(message="Cache Miss !!", title="Status", icon="cancel", button_color="#E40674", sound=True
                          , border_width=4, border_color='#A40674')
            # label_res.configure(text=f'{round((LRU.miss/LRU.access)*100, 0)}%')

        elif val is not None:
            msg = CTkMessagebox(message="Cache Hit !!", title="Status", icon="check", sound=True, option_1="Ok",
                                 justify="center", button_color="#D40674", button_hover_color="#A40674", border_width=4,
                                border_color='#A40674')
            if msg.get() == "Ok":
                button_return.configure(text=val)
                LRU_Dash()

    def check_empty_put(entry_key, entry_value):

        if entry_value.get() == "" or entry_key.get() == "":
            CTkMessagebox(message="Entry Empty", title="Error", icon="cancel", button_color="#D40674",
                          button_hover_color="#A40674", border_width=4, border_color='#A40674')
            entry_key.delete(0, tkinter.END)
            entry_value.delete(0, tkinter.END)
        else:
            msg = CTkMessagebox(message="Cache Update", title="Successful", icon="check", sound=True, option_1="Ok",
                                option_2="Cancle", justify="center", button_color="#D40674", button_hover_color="#A40674"
                                , border_width=4, border_color='#A40674')
            if msg.get() == "Ok":
                LRU.put(entry_key.get(), entry_value.get())
                entry_key.delete(0, tkinter.END)
                entry_value.delete(0, tkinter.END)
                print(round((LRU.miss/LRU.access)*100, 2))
                label_res.configure(text=f'{round((LRU.miss / LRU.access) * 100, 0)}%')
                LRU_Dash()

    def check_empty_get(entry_key):

        if entry_key.get() == "":
            CTkMessagebox(message="Entry Empty", title="Error", icon="cancel", button_color="#D40674",
                          button_hover_color="#A40674", border_width=4, border_color='#A40674')
            entry_key.delete(0, tkinter.END)
        else:
            check = LRU.get(entry_key.get())
            entry_key.delete(0, tkinter.END)
            label_res.configure(text=f'{round((LRU.miss / LRU.access) * 100, 0)}%')
            generate_get(check)

    def LRU_Dash():

        frame2 = CTkScrollableFrame(frame1, scrollbar_button_color="#A40674")
        frame2.place(relx=0.05, rely=0.27, anchor=tkinter.NW, relwidth=0.898, relheight=0.7)
        i = 0
        j = 0
        curr = LRU.lst.head
        while curr is not None:
            if i == 0 and j == 0:
                button = CTkLabel(frame2, text="", height=90, width=90, anchor="center", corner_radius=20,
                                  font=CTkFont("Arial", 20), fg_color="transparent")
                button.grid(row=i, column=j, pady=7)

            elif j == 8 and i in [0, 2]:
                button = CTkLabel(frame2, height=90, width=90, anchor="center", text="",
                                  image=right_arrow, fg_color="transparent")
                button.grid(row=i, column=j, pady=7, rowspan=2)

            elif j == 0 and i in [1, 3]:

                button = CTkLabel(frame2, height=90, width=90, anchor="center", text="",
                                  image=left_arrow, fg_color="transparent")
                button.grid(row=i, column=j, pady=7, rowspan=2)

            elif j not in [0, 8] and not j % 2:

                button = CTkLabel(frame2, height=90, width=90, anchor="center", text="",
                                  image=arrow, fg_color="transparent")
                button.grid(row=i, column=j, pady=7)

            elif j != 8 and j != 0:

                button = CTkLabel(frame2, text=f"k = {curr.key}\nv = {curr.data}", height=90, width=90, anchor="center",
                                  corner_radius=20,
                                  font=CTkFont("Arial", 20), fg_color="#D40674")
                button.grid(row=i, column=j, pady=7)
                label_least_count.configure(text=LRU.lst.tail.data)

                curr = curr.right

            if i in [1, 3]:
                j -= 1
            else:
                j += 1

            if j == 9:
                j = 8
                i += 1
            elif j == -1:
                j = 0
                i += 1

    def Data_Dash(x):

        label1 = CTkLabel(frame3, text="Least Recently Used", font=CTkFont(family="Time New Roman", size=25))
        label1.place(relx=0.18, rely=0.25, anchor=tkinter.CENTER)

        label2 = CTkLabel(frame3, text="LRU Cache Size", font=CTkFont(family="Time New Roman", size=25))
        label2.place(relx=0.52, rely=0.25, anchor=tkinter.CENTER)

        label_size = CTkLabel(frame3, height=40, text=x, fg_color="#D40674", width=150,
                              corner_radius=10, font=CTkFont(family="Arial", size=16))

        label_size.place(relx=0.52, rely=0.6, anchor=tkinter.CENTER)

        LRU_Dash()

    def Main_Dash():

        label_title = CTkLabel(frame0, text="LRU CACHE", font=CTkFont(family="Time New Roman", size=40, weight="bold"))
        label_title.place(relx=0.5, rely=0.07, anchor=tkinter.CENTER)

        label_line1 = CTkButton(frame0, text="", bg_color="#D40674", height=1, anchor="center")
        label_line1.place(relx=0.5, rely=0.28, relwidth=0.9, anchor=tkinter.CENTER)

        entry_put_key = CTkEntry(frame0, height=40, placeholder_text="Enter Key", font=CTkFont(family="Arial", size=10))
        entry_put_key.place(relx=0.5, rely=0.4, relwidth=0.6, anchor=tkinter.CENTER)

        entry_put_value = CTkEntry(frame0, height=40, placeholder_text="Enter Value",
                                   font=CTkFont(family="Arial", size=10))
        entry_put_value.place(relx=0.5, rely=0.49, relwidth=0.6, anchor=tkinter.CENTER)

        button_put_data = CTkButton(frame0, height=40, text="Put", fg_color="#E40674", anchor="center",
                                    command=lambda: check_empty_put(entry_put_key, entry_put_value),
                                    hover_color="#D40674")
        button_put_data.place(relx=0.5, rely=0.58, relwidth=0.6, anchor=tkinter.CENTER)

        label_line2 = CTkButton(frame0, text="", bg_color="#E40674", height=1, anchor="center")
        label_line2.place(relx=0.5, rely=0.68, relwidth=0.9, anchor=tkinter.CENTER)

        entry_get_data = CTkEntry(frame0, height=40, placeholder_text="Enter Key",
                                  font=CTkFont(family="Arial", size=10))
        entry_get_data.place(relx=0.5, rely=0.78, relwidth=0.6, anchor=tkinter.CENTER)

        button_get_data = CTkButton(frame0, height=40, text="Get", fg_color="#E40674", anchor="center",
                                    command=lambda: check_empty_get(entry_get_data), hover_color="#D40674")
        button_get_data.place(relx=0.5, rely=0.87, relwidth=0.6, anchor=tkinter.CENTER)

    Main_Dash()
    Data_Dash(x)
    generate_get()



def func(x, *windows):

        x = round(x)
        if x is not None and x > 0:
            LRU.capacity = x
            if windows is not None:
                for i in windows:
                    i.destroy()
            Main(x)

        else:
            CTkMessagebox(message="Invalid Size !!", title="Error", sound=True, button_color="#D40674", icon="warning"
                          , button_hover_color="#A40674", border_width=4, border_color='#A40674')

if __name__ == '__main__':
    set_size()

root.mainloop()

