from tkinter import *

class CalculatorApp:

    def __init__(self, window, name="Calculator", size="400x600"):
        self.calculator_window = window
        self.calculator_window.title(name)
        self.calculator_window.geometry(size)
        self.calculator_window.configure(bg="#252728")
        self.calculator_window.resizable(False, False)

        self.calculator_buttons_name = [
            ["C", "()", "%", "/"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
        ]

        self.initialize_calculator_widgets()
        self.initialize_calculator_buttons()
    
    def initialize_calculator_widgets(self):
        self.calculator_display_frame = Frame(self.calculator_window, height=150, bg="#1a1c1e")
        self.calculator_display_frame.pack(expand=True, fill="both")
        self.calculator_display_frame.pack_propagate(False)

        self.calculator_display_text = StringVar()
        self.calculator_display_label = Label(self.calculator_display_frame,
                                              textvariable=self.calculator_display_text,
                                              anchor="e",
                                              font=("Arial", 30),
                                              bg="#1a1c1e",
                                              fg="#FFFFFF",
                                              padx=10)
        self.calculator_display_label.pack(expand=True, fill="both")

        self.calculator_display_divider = Frame(self.calculator_window, height=2, bg="#fdfffd")
        self.calculator_display_divider.pack(fill="x", pady=0)

        self.calculator_extras_frame = Frame(self.calculator_window, bg="#252728")
        self.calculator_extras_frame.pack(expand=True, fill="both")

        self.calculator_buttons_frame = Frame(self.calculator_window, bg="#252728")
        self.calculator_buttons_frame.pack(expand=True, fill="both", padx=10)
    
    def initialize_calculator_buttons(self):
        for row in range(5):
            for column in range(4):
                button_char = self.calculator_buttons_name[row][column]
                button_method = self.initialize_calculator_buttons_method(button_char)

                Button(self.calculator_buttons_frame, 
                       text=button_char,
                       font=("Arial", 20, "bold"),
                       relief="flat",
                       fg="#fefbfa",
                       bg=self.initialize_calculator_buttons_color(row, column),
                       command=button_method
                       ).grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        
        for row in range(5):
            self.calculator_buttons_frame.rowconfigure(row, weight=1)
        for column in range(4):
            self.calculator_buttons_frame.columnconfigure(column, weight=1)
    
    def initialize_calculator_buttons_method(self, button_char):
        command = None

        if button_char == "C":
            command = self.clear_text
        elif button_char == "=":
            comman = self.calculate()
        else:
            command = lambda ch=button_char: self.display_text(ch)
        
        return command


    def initialize_calculator_buttons_color(self, row, column):
        color = None

        if row == 0 and column < 3:
            color = "#857c6a"
        elif row != 0 and column < 3:
            color = "#533d27"
        elif row == 4 and column == 3:
            color = "#f1a01c"
        elif column == 3:
            color = "#f1b062"

        return color
    
    def display_text(self, char):
        text_to_display = self.calculator_display_text.get()
        self.calculator_display_text.set(text_to_display + str(char))
    
    def clear_text(self):
        self.calculator_display_text.set("")
    
    def calculate(self):
        pass