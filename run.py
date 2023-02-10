import tkinter
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("ASPIS")
        self.geometry("552x616")
        self.resizable(False, False)
        self.configure(fg_color='#323335')

        # переменная хранящая имя выбранной кнопки клавиатуры
        self.code: str = ""
        # переменная хранящая выбранную кнопку
        self.press_bt: customtkinter.CTkButton = None
        # переменные хранящие выбранные чекбоксы
        self.Ctrl = tkinter.StringVar()
        self.Alt = tkinter.StringVar()
        self.Shift = tkinter.StringVar()
        self.Tab = tkinter.StringVar()

        # self.iconbitmap(default="aspid.ico")
        # img = PhotoImage(file='Frame 1.png')
        # Label(app,image=img,bg='#000000').pack()

        self.button_group()
        self.entry_group()
        self.checkbox_group()

        self.label_1 = customtkinter.CTkLabel(text="Введите макрос набор", text_color="#8AB42F", master=self,
                                              justify=tkinter.LEFT,
                                              bg_color="#323335")
        self.label_1.place(relx=0.550, rely=0.690)

    # в этой ф-ции кнопки клавиатуры
    def button_group(self):
        self.button1 = customtkinter.CTkButton(command=lambda: self.button_function("$key1", self.button1), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button1.place(relx=0.570, rely=0.177)

        self.button2 = customtkinter.CTkButton(command=lambda: self.button_function("$key2",self.button2), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button2.place(relx=0.706, rely=0.177)

        self.button3 = customtkinter.CTkButton(command=lambda: self.button_function("$key3",self.button3), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button3.place(relx=0.840, rely=0.177)
        # второй ряд
        self.button4 = customtkinter.CTkButton(command=lambda: self.button_function("$key4",self.button4), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button4.place(relx=0.032, rely=0.299)

        self.button5 = customtkinter.CTkButton(command=lambda: self.button_function("$key5",self.button5), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button5.place(relx=0.168, rely=0.299)

        self.button6 = customtkinter.CTkButton(command=lambda: self.button_function("$key6",self.button6), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button6.place(relx=0.301, rely=0.299)

        self.button7 = customtkinter.CTkButton(command=lambda: self.button_function("$key7",self.button7), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button7.place(relx=0.436, rely=0.299)

        self.button8 = customtkinter.CTkButton(command=lambda: self.button_function("$key8",self.button8), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button8.place(relx=0.570, rely=0.299)

        self.button9 = customtkinter.CTkButton(command=lambda: self.button_function("$key9", self.button9), text="Имя", master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70,
                                               bg_color="#323335")
        self.button9.place(relx=0.706, rely=0.299)

        self.button10 = customtkinter.CTkButton(command=lambda: self.button_function("$key10",self.button10), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button10.place(relx=0.840, rely=0.299)
        # третий ряд
        self.button11 = customtkinter.CTkButton(command=lambda: self.button_function("$key11",self.button11), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=144,
                                                height=70,
                                                bg_color="#323335")
        self.button11.place(relx=0.032, rely=0.420)

        self.button12 = customtkinter.CTkButton(command=lambda: self.button_function("$key12",self.button12), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button12.place(relx=0.301, rely=0.420)

        self.button13 = customtkinter.CTkButton(command=lambda: self.button_function("$key13",self.button13), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button13.place(relx=0.436, rely=0.420)

        self.button14 = customtkinter.CTkButton(command=lambda: self.button_function("$key14",self.button14), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button14.place(relx=0.570, rely=0.420)

        self.button15 = customtkinter.CTkButton(command=lambda: self.button_function("$key15",self.button15), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button15.place(relx=0.706, rely=0.420)

        self.button16 = customtkinter.CTkButton(command=lambda: self.button_function("$key16",self.button16), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=144,
                                                bg_color="#323335")
        self.button16.place(relx=0.840, rely=0.420)

        self.button17 = customtkinter.CTkButton(command=lambda: self.button_function("$key17",self.button17), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button17.place(relx=0.032, rely=0.541)

        self.button18 = customtkinter.CTkButton(command=lambda: self.button_function("$key18",self.button18), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button18.place(relx=0.168, rely=0.541)

        self.button19 = customtkinter.CTkButton(command=lambda: self.button_function("$key19",self.button19), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button19.place(relx=0.301, rely=0.541)

        self.button20 = customtkinter.CTkButton(command=lambda: self.button_function("$key20",self.button20), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=144,
                                                height=70,
                                                bg_color="#323335")
        self.button20.place(relx=0.436, rely=0.541)

        self.button21 = customtkinter.CTkButton(command=lambda: self.button_function("$key21",self.button21), text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70,
                                                bg_color="#323335")
        self.button21.place(relx=0.706, rely=0.541)

    # в этой ф-ции поле ввода
    def entry_group(self):
        self.entry = customtkinter.CTkEntry(placeholder_text="Желательно Eng", master=self, corner_radius=6, width=230,
                                            height=30,
                                            fg_color="#323335", bg_color="#323335", text_color='#FFFFFF')
        self.entry.place(relx=0.549, rely=0.743)

    # в этой ф-ции чекбоксы и кнопка сохранить
    def checkbox_group(self):
        self.checkbox1 = customtkinter.CTkCheckBox(variable=self.Ctrl, offvalue='', onvalue="+Ctrl", master=self,
                                                   text_color="#cce74f", text="Ctrl",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox1.place(relx=0.032, rely=0.700)

        self.checkbox2 = customtkinter.CTkCheckBox(variable=self.Alt, offvalue='', onvalue="+Alt", master=self,
                                                   text_color="#cce74f", text="Alt",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox2.place(relx=0.032, rely=0.745)

        self.checkbox3 = customtkinter.CTkCheckBox(variable=self.Shift, offvalue='', onvalue="+Shift", master=self,
                                                   text_color="#cce74f", text="Shift",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox3.place(relx=0.032, rely=0.79)

        self.checkbox4 = customtkinter.CTkCheckBox(variable=self.Tab, offvalue='', onvalue="+Tab", master=self,
                                                   text_color="#cce74f", text="Tab",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox4.place(relx=0.032, rely=0.835)

        self.button = customtkinter.CTkButton(command=self.save, text="Сохранить", master=self, text_color="#FFFFFF",
                                              fg_color='#323335',
                                              hover_color="#8AB42F", corner_radius=8, width=120, height=40,
                                              bg_color="#323335", state="disabled")
        self.button.place(relx=0.655, rely=0.811)

    # функция сохранения значния выбраной кнопки клавиатуры
    def button_function(self, arg: str, bt):
        self.code = arg
        if self.press_bt: self.press_bt.configure(fg_color='#FFFFFF')
        if self.button.cget('state') == 'disabled':
            self.button.configure(state='active')
        self.press_bt = bt
        bt.configure(fg_color='#8AB42F')


    def save(self):
        name = f"+{self.entry.get()}" if self.entry.get() else ''
        data_to_send = self.code + self.Ctrl.get() + self.Alt.get() + self.Shift.get() + self.Tab.get() + name + ';'
        print(data_to_send)

    # def click_btn(self, arg, bt, bt_sd):
    #     bt_sd["state"] = ["active"]
    #     press_bt[0]["bg"] = color_bt
    #     bt["bg"] = color_press
    #     press_bt[0] = bt

    # def click_btn_send(self, bt, tx_b: tk.Entry, ):
    #     for el in (kp1, kp2, kp3, kp4):
    #         el.set('')
    #     tx_b.delete(0, tk.END)
    #     bt["state"] = ["disabled"]
    #     press_bt[0]['bg'] = color_bt


if __name__ == "__main__":
    app = App()
    app.mainloop()
