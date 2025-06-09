from tkinter import *
from calculator_logic_class import CalculatorLogic

class CalculatorProgram:
    def __init__(self, window, name="Calculator", size="400x600"):
        self.window = window
        self.window.title(name)
        self.window.geometry(size)
        self.window.configure(bg="#252728")
        self.window.resizable(False, False)

        self.button_names = [
            ["C", "()", "%", "/"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
        ]

        self.initialize_widgets()
        self.initialize_extra_buttons()
        self.initialize_buttons()
    
    def initialize_widgets(self):
        self.change_color_mode_frame = Frame(self.window, height=25, bg="#1a1c1e")
        self.change_color_mode_frame.pack(fill="x")
        self.change_color_mode_frame.pack_propagate(False)

        self.change_color_mode_button = Button(self.change_color_mode_frame, width=10)
        self.change_color_mode_button.pack(side=LEFT, padx=10)

        self.change_color_mode_label = Label(self.change_color_mode_frame, text="Switch to Light")
        self.change_color_mode_label.pack(side=LEFT)

        self.input_display_frame = Frame(self.window, height=75, bg="#1a1c1e")
        self.input_display_frame.pack(fill="x")
        self.input_display_frame.pack_propagate(False)

        self.input_display_text = StringVar()

        self.input_display_label = Label(self.input_display_frame, textvariable=self.input_display_text, anchor="e", font=("Arial Rounded MT Bold", 30, "bold"), bg="#1a1c1e", fg="#959493", padx=10)
        self.input_display_label.pack(expand=True, fill="both")

        self.output_display_frame = Frame(self.window, height=75, bg="#1a1c1e")
        self.output_display_frame.pack(fill="x")
        self.output_display_frame.pack_propagate(False)

        self.output_display_text = StringVar()

        self.output_display_label = Label(self.output_display_frame, textvariable=self.output_display_text, anchor="e", font=("Arial Rounded MT Bold", 30, "bold"), bg="#1a1c1e", fg="#fdfffd", padx=10)
        self.output_display_label.pack(expand=True, fill="both")

        self.display_divider = Frame(self.window, height=4, bg="#fdfffd")
        self.display_divider.pack(fill="x", pady=0)

        self.extra_buttons_frame = Frame(self.window, bg="#252728")
        self.extra_buttons_frame.pack(expand=True, fill="both", padx=10)

        self.buttons_frame = Frame(self.window, bg="#252728")
        self.buttons_frame.pack(expand=True, fill="both", padx=10)
    
    def initialize_extra_buttons(self):
        history = Button(self.extra_buttons_frame, text="O", bg="#252728", fg="#f1b062", relief=FLAT, font=("Arial Rounded MT Bold", 20, "bold"))
        history.pack(side=LEFT, padx=10, pady=10)

        delete = Button(self.extra_buttons_frame, text="<", bg="#252728", fg="#f1b062", relief=FLAT, font=("Arial Rounded MT Bold", 20, "bold"))
        delete.pack(side=RIGHT, padx=10, pady=10)
    
    def initialize_buttons(self):
        for row in range(5):
            for column in range(4):
                button_char = self.button_names[row][column]
                button_method = self.initialize_button_method(button_char)

                Button(self.buttons_frame, text=button_char,font=("Arial Rounded MT Bold", 20, "bold"), relief="flat",fg="#fefbfa",bg=self.initialize_button_color(row, column),command=button_method).grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        
        for row in range(5):
            self.buttons_frame.rowconfigure(row, weight=1)
        for column in range(4):
            self.buttons_frame.columnconfigure(column, weight=1)
    
    def initialize_button_method(self, button_char):
        command = None

        if button_char == "C":
            command = self.clear_all
        elif button_char == "=":
            command = self.evaluate
        elif button_char == "±":
            pass
        else:
            command = lambda ch=button_char: self.display_text(ch)
        
        return command

    def initialize_button_color(self, row, column):
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
        if self.input_display_text.get() == "" and char in ["()", "%", "x", "+", "-", "/"]:
            pass
        else:
            input_to_display = self.input_display_text.get()
            self.input_display_text.set(input_to_display + str(char))
    
    def clear_all(self):
        self.input_display_text.set("")
        self.output_display_text.set("")
    
    def evaluate(self):
        input_to_calculate = self.input_display_text.get()

        if input_to_calculate != "":
            result = CalculatorLogic.calculate(input_to_calculate)
            self.output_display_text.set(result)