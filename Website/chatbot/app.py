from tkinter import *
from chat import get_response, bot_name

BG_GREY = "#ABB2B9"
BG_COLOR = "#5499C7"
TEXT_COLOR = "#283747"

FONT = "Mesquite 18"
FONT_BOLD = "Mesquite 18 bold"


class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=600, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, width=560, bg=BG_GREY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # instance variable
        self.text_widget = Text(self.window, width=40, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5, wrap="word")
        self.text_widget.place(relheight=0.7, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        bottom_label = Label(self.window, bg=BG_GREY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.message_entry = Entry(bottom_label, bg="#D7BDE2", fg=TEXT_COLOR, font=FONT)
        self.message_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.message_entry.focus()
        self.message_entry.bind("<Return>", self.on_enter_pressed)

        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GREY,
                             command=lambda: self.on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def on_enter_pressed(self, event):
        message = self.message_entry.get()
        self._insert_message(message, "You")

    def _insert_message(self, message, sender):
        if not message:
            return
        self.message_entry.delete(0, END)
        message1 = f"{sender}: {message}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, message1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        message2 = f"{bot_name}: {get_response(message)}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, message2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()

# TODO: fix spacing between text and scroll bar
