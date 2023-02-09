import tkinter as tk
from config_gui import Constant


CONSTANT = Constant()
W = CONSTANT.widht_box
H = CONSTANT.height_box
pd_ch = CONSTANT.pad_ch_box
pd_x = CONSTANT.pd_box_x
pd_y = CONSTANT.pd_box_y
color_bt = CONSTANT.color_blue
text_color = CONSTANT.color_white
color_press = CONSTANT.color_press

name = ""
size = ""
text = ""
press_bt = [{"bg": None}]


def click_btn(arg, bt, bt_sd):
    bt_sd["state"] = ["active"]
    press_bt[0]["bg"] = color_bt
    bt["bg"]=color_press
    press_bt[0] = bt
    

def click_btn_send(bt):
    bt["state"] = ["disabled"]
    press_bt[0]['bg']=color_bt

def run_win():
    root = tk.Tk()
    root.title("Названние приложения")
    root.geometry("800x480")

    frame_top = tk.Frame(root) 
    frame_top.pack(ipady=30)
    frame_bottom = tk.Frame(root)
    frame_bottom.pack()
    frame21 = tk.Frame(frame_bottom)
    frame21.pack(ipady=15) 
    frame22 = tk.Frame(frame_bottom) 
    frame22.pack(ipady=70)

    # раздел 1 в верхней рамке
 
    button1 = tk.Button(frame_top, text='один', command=lambda: click_btn('$kp1', button1, button_send), width=W, height=H,bg=color_bt, fg=text_color,font='arial 14')
    button1.pack(side='left', padx=pd_x, pady=pd_y)
    button2 = tk.Button(frame_top,text='один',width=W, command=lambda: click_btn('$kp2', button2, button_send), height=H,bg=color_bt, fg=text_color,font='arial 14')
    button2.pack(side='left', padx=pd_x, pady=pd_y)
    button3 = tk.Button(frame_top,text='один',width=W, command=lambda: click_btn('$kp3', button3, button_send), height=H,bg=color_bt, fg=text_color,font='arial 14')
    button3.pack(side='left', padx=pd_x, pady=pd_y)
    button4 = tk.Button(frame_top,text='один',width=W, command=lambda: click_btn('$kp4', button4, button_send), height=H,bg=color_bt, fg=text_color,font='arial 14')
    button4.pack(side='left', padx=pd_x, pady=pd_y)

    # раздел 2 в нижней рамке, верхней подрамке
    kp1 = tk.StringVar()
    ch_box1 = tk.Checkbutton(frame21, text=u'small', variable=kp1, onvalue="$kp1")
    ch_box1.pack(side='left', ipadx=pd_ch)

    kp2 = tk.StringVar()
    ch_box2 = tk.Checkbutton(frame21, text=u'medium', variable=kp2, onvalue="$kp2")
    ch_box2.pack(side='left', ipadx=pd_ch)

    kp3 = tk.StringVar()
    ch_box3 = tk.Checkbutton(frame21, text=u'large', variable=kp3, onvalue="$kp3")
    ch_box3.pack(side='left', ipadx=pd_ch)

    kp4 = tk.StringVar()
    ch_box4 = tk.Checkbutton(frame21, text=u'huge', variable=kp4, onvalue="$kp4")
    ch_box4.pack(side='left', ipadx=pd_ch)

    # раздел 3 в нижней рамке, нижней подрамке

    textbox = tk.Entry(frame22, width=30)
    textbox.pack(side='left',padx=40)

    button_send = tk.Button(frame22, text='Отправить', command=lambda: click_btn_send(button_send), width=10, height=1, bg='#0d99ff',fg=text_color,font='arial 14', state='disabled')
    button_send.pack(side='left', padx=40)

    root.mainloop()


if __name__ == "__main__":
    run_win()