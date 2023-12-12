import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_650 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_650["font"] = ft
        GLabel_650["fg"] = "#333333"
        GLabel_650["justify"] = "center"
        GLabel_650["text"] = "label"
        GLabel_650.place(x=90, y=60, width=242, height=83)

        GButton_287 = tk.Button(root)
        GButton_287["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_287["font"] = ft
        GButton_287["fg"] = "#000000"
        GButton_287["justify"] = "center"
        GButton_287["text"] = "Button"
        GButton_287.place(x=300, y=170, width=70, height=25)
        GButton_287["command"] = self.GButton_287_command

        GLineEdit_780 = tk.Entry(root)
        GLineEdit_780["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_780["font"] = ft
        GLineEdit_780["fg"] = "#333333"
        GLineEdit_780["justify"] = "center"
        GLineEdit_780["text"] = "Entry"
        GLineEdit_780.place(x=140, y=230, width=341, height=69)

        GListBox_276 = tk.Listbox(root)
        GListBox_276["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_276["font"] = ft
        GListBox_276["fg"] = "#333333"
        GListBox_276["justify"] = "center"
        GListBox_276.place(x=140, y=310, width=80, height=25)

        GMessage_172 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_172["font"] = ft
        GMessage_172["fg"] = "#333333"
        GMessage_172["justify"] = "center"
        GMessage_172["text"] = "Message"
        GMessage_172.place(x=400, y=100, width=80, height=25)

    def GButton_287_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
