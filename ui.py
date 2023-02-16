import tkinter
from tkinter.messagebox import showinfo

import customtkinter


class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("ASPIS")
        self.geometry("550x600")
        self.resizable(False, False)
        self.configure(fg_color='#323335')
        self.button1 = customtkinter.CTkButton(command=lambda: self.button_function("$key1", self.button1), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button1.place(relx=0.570, rely=0.177)

        self.button2 = customtkinter.CTkButton(command=lambda: self.button_function("$key2", self.button2), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button2.place(relx=0.706, rely=0.177)

        self.button3 = customtkinter.CTkButton(command=lambda: self.button_function("$key3", self.button3), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button3.place(relx=0.840, rely=0.177)
        # второй ряд
        self.button4 = customtkinter.CTkButton(command=lambda: self.button_function("$key4", self.button4), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button4.place(relx=0.032, rely=0.299)

        self.button5 = customtkinter.CTkButton(command=lambda: self.button_function("$key5", self.button5), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button5.place(relx=0.168, rely=0.299)

        self.button6 = customtkinter.CTkButton(command=lambda: self.button_function("$key6", self.button6), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button6.place(relx=0.301, rely=0.299)

        self.button7 = customtkinter.CTkButton(command=lambda: self.button_function("$key7", self.button7), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button7.place(relx=0.436, rely=0.299)

        self.button8 = customtkinter.CTkButton(command=lambda: self.button_function("$key8", self.button8), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button8.place(relx=0.570, rely=0.299)

        self.button9 = customtkinter.CTkButton(command=lambda: self.button_function("$key9", self.button9), text="Имя",
                                               master=self,
                                               text_color="#008bd0",
                                               fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                               height=70, font=('TButton', 10),
                                               bg_color="#323335")
        self.button9.place(relx=0.706, rely=0.299)

        self.button10 = customtkinter.CTkButton(command=lambda: self.button_function("$key10", self.button10),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button10.place(relx=0.840, rely=0.299)
        # третий ряд
        self.button11 = customtkinter.CTkButton(command=lambda: self.button_function("$key11", self.button11),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=144,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button11.place(relx=0.032, rely=0.420)

        self.button12 = customtkinter.CTkButton(command=lambda: self.button_function("$key12", self.button12),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button12.place(relx=0.301, rely=0.420)

        self.button13 = customtkinter.CTkButton(command=lambda: self.button_function("$key13", self.button13),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button13.place(relx=0.436, rely=0.420)

        self.button14 = customtkinter.CTkButton(command=lambda: self.button_function("$key14", self.button14),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button14.place(relx=0.570, rely=0.420)

        self.button15 = customtkinter.CTkButton(command=lambda: self.button_function("$key15", self.button15),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button15.place(relx=0.706, rely=0.420)

        self.button16 = customtkinter.CTkButton(command=lambda: self.button_function("$key16", self.button16),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=144, font=('TButton', 10),
                                                bg_color="#323335")
        self.button16.place(relx=0.840, rely=0.420)

        self.button17 = customtkinter.CTkButton(command=lambda: self.button_function("$key17", self.button17),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button17.place(relx=0.032, rely=0.541)

        self.button18 = customtkinter.CTkButton(command=lambda: self.button_function("$key18", self.button18),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button18.place(relx=0.168, rely=0.541)

        self.button19 = customtkinter.CTkButton(command=lambda: self.button_function("$key19", self.button19),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button19.place(relx=0.301, rely=0.541)

        self.button20 = customtkinter.CTkButton(command=lambda: self.button_function("$key20", self.button20),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=144,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button20.place(relx=0.436, rely=0.541)

        self.button21 = customtkinter.CTkButton(command=lambda: self.button_function("$key21", self.button21),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=70,
                                                height=70, font=('TButton', 10),
                                                bg_color="#323335")
        self.button21.place(relx=0.706, rely=0.541)

        # ЭНКОДЕРЫ
        # Вертикальный
        self.button24 = customtkinter.CTkButton(command=lambda: self.button_function("$key24", self.button24),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#ECECEC', hover_color="#A3B8BD", corner_radius=8, width=55,
                                                height=44, font=('TButton', 10),
                                                bg_color="#323335")
        self.button24.place(relx=0.035, rely=0.190)

        self.button23 = customtkinter.CTkButton(command=lambda: self.button_function("$key23", self.button23),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#ECECEC', hover_color="#A3B8BD", corner_radius=8, width=55,
                                                height=44, font=('TButton', 10),
                                                bg_color="#323335")
        self.button23.place(relx=0.2, rely=0.190)

        self.button22 = customtkinter.CTkButton(command=lambda: self.button_function("$key22", self.button22),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=8, width=60,
                                                height=60, font=('TButton', 10),
                                                bg_color="#323335")
        self.button22.place(relx=0.11, rely=0.177)
        # Горизонтальный

        self.button25 = customtkinter.CTkButton(command=lambda: self.button_function("$key25", self.button25),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=3, width=140,
                                                height=25, font=('TButton', 10),
                                                bg_color="#323335")
        self.button25.place(relx=0.306, rely=0.189)

        self.button26 = customtkinter.CTkButton(command=lambda: self.button_function("$key26", self.button26),
                                                text="Имя", master=self,
                                                text_color="#008bd0",
                                                fg_color='#FFFFFF', hover_color="#A3B8BD", corner_radius=3, width=140,
                                                height=25, font=('TButton', 10),
                                                bg_color="#323335")
        self.button26.place(relx=0.306, rely=0.229)

        self.entry = customtkinter.CTkEntry(placeholder_text="Желательно Eng", master=self, corner_radius=6, width=230,
                                            height=30,
                                            fg_color="#323335", bg_color="#323335", text_color='#FFFFFF')
        self.entry.place(relx=0.549, rely=0.743)

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

        self.checkbox5 = customtkinter.CTkCheckBox(variable=self.Esc, offvalue='', onvalue="+Esc", master=self,
                                                   text_color="#cce74f", text="Esc",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox5.place(relx=0.165, rely=0.700)

        self.checkbox6 = customtkinter.CTkCheckBox(variable=self.Bac, offvalue='', onvalue="+Bac", master=self,
                                                   text_color="#cce74f", text="Bac",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox6.place(relx=0.165, rely=0.745)

        self.checkbox7 = customtkinter.CTkCheckBox(variable=self.Entr, offvalue='', onvalue="+Entr", master=self,
                                                   text_color="#cce74f", text="Entr",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox7.place(relx=0.165, rely=0.79)

        self.checkbox8 = customtkinter.CTkCheckBox(variable=self.Del, offvalue='', onvalue="+Del", master=self,
                                                   text_color="#cce74f", text="Del",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox8.place(relx=0.165, rely=0.835)

        self.checkbox9 = customtkinter.CTkCheckBox(variable=self.F3, offvalue='', onvalue="+F3", master=self,
                                                   text_color="#cce74f", text="F3",
                                                   fg_color="#cce74f", hover_color="#cce74f", checkmark_color="#313335",
                                                   bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                   border_width=1, corner_radius=3)
        self.checkbox9.place(relx=0.302, rely=0.700)

        self.checkbox10 = customtkinter.CTkCheckBox(variable=self.F4, offvalue='', onvalue="+F4", master=self,
                                                    text_color="#cce74f", text="F4",
                                                    fg_color="#cce74f", hover_color="#cce74f",
                                                    checkmark_color="#313335",
                                                    bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                    border_width=1, corner_radius=3)
        self.checkbox10.place(relx=0.302, rely=0.745)

        self.checkbox11 = customtkinter.CTkCheckBox(variable=self.Space, offvalue='', onvalue="+Space", master=self,
                                                    text_color="#cce74f", text="Space",
                                                    fg_color="#cce74f", hover_color="#cce74f",
                                                    checkmark_color="#313335",
                                                    bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                    border_width=1, corner_radius=3)
        self.checkbox11.place(relx=0.302, rely=0.79)

        self.checkbox12 = customtkinter.CTkCheckBox(variable=self.Comm, offvalue='', onvalue="+Comm", master=self,
                                                    text_color="#cce74f", text="Comm",
                                                    fg_color="#cce74f", hover_color="#cce74f",
                                                    checkmark_color="#313335",
                                                    bg_color="#323335", width=70, checkbox_width=13, checkbox_height=13,
                                                    border_width=1, corner_radius=3)
        self.checkbox12.place(relx=0.302, rely=0.835)

        # ____________________________________________________________________________________________________________

        self.label_1 = customtkinter.CTkLabel(text="Введите макрос набор", text_color="#8AB42F", master=self,
                                              justify=tkinter.LEFT,
                                              bg_color="#323335")
        self.label_1.place(relx=0.550, rely=0.690)
        self.button = customtkinter.CTkButton(command=self.save, text="Сохранить", master=self, text_color="#FFFFFF",
                                              fg_color='#323335',
                                              hover_color="#8AB42F", corner_radius=8, width=120, height=40,
                                              bg_color="#323335", state="disabled")
        self.button.place(relx=0.655, rely=0.811)

        border_1 = customtkinter.CTkLabel(self, text="©Aspis Keyboard 2022", text_color="#cce74f", justify=tkinter.LEFT)
        border_1.place(relx=0.01, rely=0.95)

        labelr1 = tkinter.Label(self, text="behance", fg="#0058fb", cursor="hand2", bg='#313335')
        labelr1.bind("<Button-1>", lambda event: self.open_link(r"https://www.behance.net/shakirovnz"))
        labelr1.place(relx=0.36, rely=0.95)

        labelr2 = tkinter.Label(self, text="telegram", fg="#2aa2de", cursor="hand2", bg='#313335')
        labelr2.bind("<Button-1>", lambda event: self.open_link(r"https://t.me/shakirovnz"))
        labelr2.place(relx=0.45, rely=0.95)

        labelr3 = tkinter.Label(self, text="about", fg="#2aa2de", cursor="hand2", bg='#313335')
        labelr3.bind("<Button-1>", lambda event: showinfo(title="Информация", message=self.about))
        labelr3.place(relx=0.54, rely=0.95)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
