import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# function for calculatio
def calculate():
    user_input = entry.get()  #
    operators = ["+", "-", "/", "*", "(", ")"]
    calculationString = ""
    valueArray = []

    for char in user_input:  # user input wird in liste gepsichert
        if char not in operators:
            calculationString += char
        else:
            if calculationString != "":
                valueArray.append(
                    float(calculationString)
                )  # input wird als float gepsciehrt um dezimalzahlen zu rechnen
                calculationString = ""  # MICH NERVT ALLES
            valueArray.append(char)

    if calculationString != "":
        valueArray.append(float(calculationString))

    result = valueArray[0]

    def prio_input(input):  # code aus einem beispielprojekt überarbeitet und angepasst
        operators = []
        values = [] 

        index = 0  # index wird auf 0 gestzt
        while index < len(input):
            if input[index] == " ":
                index += 1  # geht zum nächsten
                continue
            if (
                input[index] in "0123456789"
            ):  # nimmt alle digits raus und speichert in liste als float
                temp_index = index  #####
                while (
                    temp_index < len(input) and input[temp_index] in "0123456789."
                ):  #####
                    temp_index += 1  #####
                values.append(
                    float(input[index:temp_index])
                )  # Changed to float for decimal numbers ######
                index = temp_index
            elif input[index] in "+-*/":
                while (
                    len(operators) > 0
                    and operators[-1] in "+-*/"
                    and prio_op(operators[-1]) >= prio_op(input[index])
                ):
                    calculation_variants(operators, values)
                operators.append(input[index])
                index += 1
            elif input[index] == "(":
                operators.append(input[index])
                index += 1
            elif input[index] == ")":
                while operators[-1] != "(":
                    calculation_variants(operators, values)
                operators.pop()
                index += 1
            else:
                raise ValueError("Invalid character in input")

        while len(operators) > 0:
            calculation_variants(operators, values)

        return values[0]

    def prio_op(operator):
        if operator in ("+", "-"):
            return 1
        elif operator in ("*", "/"):
            return 2
        elif operator in ("(", ")"):
            return 0
        return 0

    def calculation_variants(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == "+":
            values.append(left + right)
        elif operator == "-":
            values.append(left - right)
        elif operator == "*":
            values.append(left * right)
        elif operator == "/":
            if right == 0:
                raise ValueError("Division by zero is not allowed.")
            values.append(left / right)

    try:
        result = prio_input(user_input)
        result_label.config(text="Ergebnis: " + str(result))
    except ValueError as e:
        result_label.config(text="Ungültige Eingabe: " + str(e))


# GUI erstellen
root = tk.Tk()
root.title("Calculatorium by Maxus")
root.geometry("312x412")
root.minsize(width=250, height=300)
root.maxsize(width=500, height=600)

# Eingabefeld
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=20, padx=10, expand=True)

# Ergebnis-Anzeige
result_label = tk.Label(root, text="Ergebnis ", font=("Arial", 16))
stinker_label = tk.Label(root, text="ICH HASSE STINKER", font=("Arial", 16))
result_label.pack(pady=20)
stinker_label.pack(pady=20)

# Zahlen und Operatoren
buttons_frame = ttk.Frame(root)
buttons_frame.pack()


image = Image.open("test.jpg").resize((300, 100))
photo = ImageTk.PhotoImage(image)
imagelable = ttk.Label(root, image=photo)
imagelable.pack()
# Ich will nicht mehr dieser kak geht mir aufm nerv alda
# Liste der Buttons
buttons = [
    "7",
    "8",
    "9",
    "/",
    "4",
    "5",
    "6",
    "*",
    "1",
    "2",
    "3",
    "-",
    "0",
    "=",
    "+",
    "(",
    ")",
]

row_val = 1  # Row setzen
col_val = 0  # Column

# Mit Hilfe von Video und Google
for button in buttons:
    ttk.Button(
        buttons_frame,
        text=button,
        width=10,
        command=lambda b=button: entry.insert(
            tk.END, b
        ),  # On button click insert entry to input
    ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:  # Überprüft, ob bereits 4 Buttons platziert wurden in der Spalte
        col_val = 0  # Falls ja, macht er eine neue Zeile
        row_val += 1

# Clear Entry Button
ttk.Button(
    buttons_frame, text="Clear", width=10, command=lambda: entry.delete(0, tk.END)
).grid(row=row_val, column=col_val)

# Berechnen-Button
ttk.Button(buttons_frame, text="Berechnen", width=10, command=calculate).grid(
    row=row_val + 2, column=0
)  ## kack stinker

ttk.Button(buttons_frame, text="Kill everyone in the Calulatorium", width=30, command=root.destroy).grid(
    row=row_val +2, column=1, columnspan=4
)


# ich geh heim reicht mir ey
root.mainloop()
