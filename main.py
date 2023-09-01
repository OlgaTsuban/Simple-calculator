from tkinter import *
from math import sqrt
from math import cos, tan, sin

# Decorator to handle errors in input calculations
def input_error(func):
    def inner(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
        except Exception:
            result = "Error"
        self.field.delete("1.0", "end")
        self.field.insert("1.0", result)
        self.field_of_calc = str(result)
    return inner

class Calculator:
    def __init__(self):
        self.field_of_calc = ""
        # Create the main window
        self.window = Tk()
        self.window.configure(background="lavender")
        self.window.title("Simple Calculator")
        self.window.geometry("330x255")
        # Create a text field for displaying calculations
        self.field = Text(self.window, height=2, width=21, font=("Arial", 20))
        self.field.grid(row=1, column=1, columnspan=4)
        # Create numeric buttons and additional buttons
        self.create_buttons()
        
    def write_in_field(self, information):
        # Function to add information to the calculation field
        self.field_of_calc += information
        self.field.delete("1.0", "end")
        self.field.insert("1.0", self.field_of_calc)

    @input_error
    def calculate(self):
        # Function to perform the calculation
        return str(eval(self.field_of_calc))

    def clear(self):
        # Function to clear the calculation field
        self.field_of_calc = ""
        self.field.delete("1.0", "end")
        
    @input_error
    def calculate_sqrt(self, smth):
        # Function to calculate the square root
        return sqrt(eval(self.field_of_calc))
        
    @input_error
    def calculate_pow(self, smth):
        # Function to calculate the square of a number
        return pow(eval(self.field_of_calc), 2)
    
    @input_error
    def calculate_sin(self, smth):
        # Function to calculate the sin of a number
        return sin(eval(self.field_of_calc))
        
    @input_error
    def calculate_cos(self, smth):
        # Function to calculate the cos of a number
        return cos(eval(self.field_of_calc))
    
    @input_error
    def calculate_tg(self, smth):
        # Function to calculate the tg of a number
        return tan(eval(self.field_of_calc))
    
    @input_error
    def calculate_ctg(self, smth):
        # Function to calculate the ctg of a number
        return 1/tan(eval(self.field_of_calc))
    
    def delete(self):
        # Function to delete the last character from the calculation field
        self.field_of_calc = self.field_of_calc[0:-1]
        self.field.delete("1.0", "end")
        self.field.insert("1.0", self.field_of_calc)

    def create_buttons(self):
        #Create numeric buttons
        button_positions = [(5, 1), (4, 1), (4, 2), (4, 3), (3, 1), (3, 2), (3, 3), (2, 1), (2, 2), (2, 3)]
        for position, number in zip(button_positions, range(0, 10)):
            button_frame = Frame(self.window)
            button = Button(button_frame, text=f' {number} ', command=lambda n=number: self.write_in_field(str(n)), width=5, fg="black")
            button.pack(fill="both", expand=True)
            button_frame.grid(row=position[0], column=position[1])
        #Create sign buttons
        add_button_positions = [(4, 4), (5, 4), (2, 4), (3, 4), (6, 1), (6, 2), (7, 1), (7, 2), (8, 1), (8, 2), (8, 3), (8, 4)]
        button_styles = {
            '+': ('#7D9EC0', self.write_in_field, "+"),
            '-': ('#CDB5CD', self.write_in_field, "-"),
            '/': ('#CDAF95', self.write_in_field, "/"),
            '*': ('#EEB4B4', self.write_in_field, "*"),
            '(': ('#AEEEEE', self.write_in_field, "("),
            ')': ('#FFBBFF', self.write_in_field, ")"),
            '√': ('#4EEE94', self.calculate_sqrt, ""),
            'x²': ('#FFA500', self.calculate_pow, ""),
            'sin': ('#87CEFA', self.calculate_sin, ""),
            'cos': ('#C0C0C0', self.calculate_cos, ""),
            'tg': ('#B0E0E6', self.calculate_tg, ""),
            'ctg': ('#EEAEEE', self.calculate_ctg, "")
        }
        for position, sign in zip(add_button_positions, button_styles.keys()):
            button_frame = Frame(self.window)
            button = Button(button_frame, text=f' {sign} ', command=lambda s=sign: button_styles[s][1](str(button_styles[s][2])), width=5, highlightbackground=button_styles[sign][0])
            button.pack(fill="both", expand=True)
            button_frame.grid(row=position[0], column=position[1])

        button_clear = Button(self.window, text='CLEAR', command=lambda: self.clear(), width=5)
        button_clear.grid(row=5, column=3)

        button_decimal = Button(self.window, text=' . ', command=lambda: self.write_in_field("."), width=5)
        button_decimal.grid(row=5, column=2)

        button_equal = Button(self.window, text=' = ', command=lambda: self.calculate(), width=13,  highlightbackground='#FFEC8B')
        button_equal.grid(row=6, column=3, columnspan=2)

        button_delete = Button(self.window, text=' DEL ', command=lambda: self.delete(), width=13,  highlightbackground='#FFEC8B')
        button_delete.grid(row=7, column=3, columnspan=2)

    def on_button_click(self, button):
        return lambda: self.write_in_field(str(button))
    
    def run(self):
        self.window.mainloop()
        
if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()

