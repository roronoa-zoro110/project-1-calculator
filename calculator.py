import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("sayyad's Calculator")
        root.geometry("300x400")
        root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Create input frame
        input_frame = tk.Frame(root, width=300, height=50, bd=2, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP)

        # Input field inside input frame
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                               textvariable=self.input_text, width=28, bd=0, bg="#eee", justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)  # internal padding for height

        # Create buttons frame
        btns_frame = tk.Frame(root, width=300, height=350, bg="black")
        btns_frame.pack()

        # First row
        clear = tk.Button(btns_frame, text="C", fg="black", width=7, height=3, bd=0, bg="#eee",
                          cursor="hand2", command=self.clear).grid(row=0, column=0, padx=1, pady=1)
        divide = tk.Button(btns_frame, text="/", fg="black", width=7, height=3, bd=0, bg="#eee",
                           cursor="hand2", command=lambda: self.press("/")).grid(row=0, column=1, padx=1, pady=1)
        multiply = tk.Button(btns_frame, text="*", fg="black", width=7, height=3, bd=0, bg="#eee",
                             cursor="hand2", command=lambda: self.press("*")).grid(row=0, column=2, padx=1, pady=1)
        subtract = tk.Button(btns_frame, text="-", fg="black", width=7, height=3, bd=0, bg="#eee",
                             cursor="hand2", command=lambda: self.press("-")).grid(row=0, column=3, padx=1, pady=1)

        # Second row
        btn7 = tk.Button(btns_frame, text="7", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("7")).grid(row=1, column=0, padx=1, pady=1)
        btn8 = tk.Button(btns_frame, text="8", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("8")).grid(row=1, column=1, padx=1, pady=1)
        btn9 = tk.Button(btns_frame, text="9", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("9")).grid(row=1, column=2, padx=1, pady=1)
        add = tk.Button(btns_frame, text="+", fg="black", width=7, height=3, bd=0, bg="#eee",
                        cursor="hand2", command=lambda: self.press("+")).grid(row=1, column=3, padx=1, pady=1)

        # Third row
        btn4 = tk.Button(btns_frame, text="4", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("4")).grid(row=2, column=0, padx=1, pady=1)
        btn5 = tk.Button(btns_frame, text="5", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("5")).grid(row=2, column=1, padx=1, pady=1)
        btn6 = tk.Button(btns_frame, text="6", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("6")).grid(row=2, column=2, padx=1, pady=1)
        equals = tk.Button(btns_frame, text="=", fg="black", width=7, height=7, bd=0, bg="#eee",
                           cursor="hand2", command=self.equalpress)
        equals.grid(row=2, column=3, rowspan=2, padx=1, pady=1)

        # Fourth row
        btn1 = tk.Button(btns_frame, text="1", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("1")).grid(row=3, column=0, padx=1, pady=1)
        btn2 = tk.Button(btns_frame, text="2", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("2")).grid(row=3, column=1, padx=1, pady=1)
        btn3 = tk.Button(btns_frame, text="3", fg="black", width=7, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("3")).grid(row=3, column=2, padx=1, pady=1)

        # Fifth row
        btn0 = tk.Button(btns_frame, text="0", fg="black", width=16, height=3, bd=0, bg="#fff",
                         cursor="hand2", command=lambda: self.press("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = tk.Button(btns_frame, text=".", fg="black", width=7, height=3, bd=0, bg="#eee",
                          cursor="hand2", command=lambda: self.press(".")).grid(row=4, column=2, padx=1, pady=1)
        
        # On closing the window, show thank you
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def press(self, num):
        self.expression += str(num)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equalpress(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to exit?"):
            messagebox.showinfo("Thank You", "Thank you for using the calculator!")
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
