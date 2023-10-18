# Лабораторна №3 варіант 2
from sys import exit

MATRIX_HEIGHT = 12
MATRIX_WIDTH = 12
SYMBOL = [["x", ".", "x"], [".", "x", "."], ["x", ".", "x"]]
SYMBOL_HEIGHT = len(SYMBOL[0])
SYMBOL_WIDTH = len(SYMBOL)


# Functions
def matrix_to_string(matrix):
    result = ""
    cols = len(matrix)
    rows = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            result += matrix[col][row] + " "

        if row != rows - 1:
            result += "\n"

    return result


def insert_symbol(main_matrix, symbol_matrix, pos_x, pos_y):
    cols_range = range(0, 0)
    if pos_x >= 0: cols_range = range(pos_x, SYMBOL_WIDTH + pos_x)
    if pos_x < 0: cols_range = range(MATRIX_WIDTH + pos_x - SYMBOL_WIDTH + 1, MATRIX_WIDTH + pos_x + 1)

    rows_range = range(0, 0)
    if pos_y >= 0: rows_range = range(pos_y, SYMBOL_HEIGHT + pos_y)
    if pos_y < 0: rows_range = range(MATRIX_HEIGHT + pos_y - SYMBOL_HEIGHT + 1, MATRIX_HEIGHT + pos_y + 1)

    symbol_col = 0
    for col in cols_range:
        symbol_row = 0

        for row in rows_range:
            main_matrix[col][row] = symbol_matrix[symbol_col][symbol_row]

            symbol_row += 1

        symbol_col += 1


def ask_x():
    x = input("Type x position: ").strip()
    if x == "exit()": exit("Script stopped")

    if not x.isdigit() and not (x.startswith("-") and x[1:].isdigit()):
        print(" Invalid value")
        return ask_x()
    
    int_x = int(x)
    if int_x >= 0 and int_x <= MATRIX_WIDTH - SYMBOL_WIDTH:
        return int_x
    elif int_x < 0 and int_x >= SYMBOL_WIDTH - MATRIX_WIDTH - 1:
        return int_x
    else:
        print(" Invalid value") 
        return ask_x() 

def ask_y():
    y = input("Type y position: ").strip()
    if y.strip() == "exit()": exit("Script stopped")

    if not y.isdigit() and not (y.startswith("-") and y[1:].isdigit()):
        print(" Invalid value")
        return ask_y()
    
    int_y = int(y)
    if int_y >= 0 and int_y <= MATRIX_HEIGHT - SYMBOL_HEIGHT:
        return int_y
    elif int_y < 0 and int_y >= SYMBOL_HEIGHT - MATRIX_HEIGHT - 1:
        return int_y
    else: 
        print(" Invalid value")
        return ask_y()


# Main code
matrix = []

for i in range(MATRIX_WIDTH):
    col = (". " * MATRIX_HEIGHT).strip().split(" ")
    matrix.append(col)

x = ask_x()
print(f"x = {x}")
y = ask_y()
print(f"y = {y}")

insert_symbol(matrix, SYMBOL, x, y)


print("\n", " Result:")
print(matrix_to_string(matrix))