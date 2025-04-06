import tkinter as tk

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Improved Calculator with Keyboard Support")
        master.config(bg="#f0f0f0")

        self.expression = ""
        self.equation = tk.StringVar()
        self.equation.set("0")

        self.entry = tk.Entry(master, textvariable=self.equation, width=20, bd=7, relief=tk.SUNKEN,
                                font=('Segoe UI', 20), justify='right', bg="white", fg="black")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), ipady=5)
        self.entry.focus_set() # Give focus to the entry field initially

        button_data = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('%', 5, 1)
        ]

        for (text, row, col) in button_data:
            button = tk.Button(master, text=text, padx=25, pady=25, font=('Segoe UI', 16),
                                bg="#e0e0e0", activebackground="#d0d0d0", relief=tk.RAISED, bd=3,
                                command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            # Bind keyboard events to buttons (where applicable)
            if text.isdigit() or text in ['.', '+', '-', '*', '/']:
                master.bind(text, lambda event, t=text: self.button_click(t))
            elif text == '=':
                master.bind('<Return>', lambda event: self.button_click('='))
            elif text == 'C':
                master.bind('<Escape>', lambda event: self.clear())
            elif text == '%':
                master.bind('%', lambda event: self.button_click('%')) # Bind the % key

        # Make rows and columns resizable
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def button_click(self, text):
        if text == '=':
            try:
                self.result = eval(self.expression)
                self.equation.set(str(self.result))
                self.expression = str(self.result)
            except Exception as e:
                self.equation.set("Error")
                self.expression = ""
        elif text == 'C':
            self.clear()
        else:
            self.expression += text
            self.equation.set(self.expression)

    def clear(self):
        self.expression = ""
        self.equation.set("0")

def main():
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()