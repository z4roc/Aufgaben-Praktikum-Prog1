# Aufgabe 1.0

# TODO: Comment the code

import sys

# Maximale Integer-Zahlelänge auf 1000000 setzen, weil sonst ab Berechnung von
# Aufgabe E ein Fehler auftritt, da die Zahl zu lang ist
sys.set_int_max_str_digits(1000000)

def calculate_solution_a():
    return 1000 * 12

def calculate_solution_b():
    return 2 * (8921 -2348 + 123) - 400

def calculate_solution_c():
    return 123 ** 456

def calculate_solution_d():
    return ((12 ** 3 + 13 ** 4) ** 0.5) / 2 ** 0.5

def calculate_solution_e():
    return 2 ** (2 ** 17)

def calculate_solution_f():
    return int(0x5) + int(0b0101)

def calculate_solution_g():
    return len(str(2 ** (2**17)))

def calculate_solution_h():
    return str(2 ** 10000)[42]

def calculate_solution_i():
    return str(2 ** 10000).count("4")

def calculate_solution_j():
    return str(2 ** 10000)[1000] == "4" or str(2 ** 10000)[1000] == "6"

def calculate_solution_k():
    numberList = str(2 ** 10000)
    firstNumber = numberList[1000]
    secondNumber = numberList[2000]
    return (firstNumber == "1" or firstNumber == "3") and (secondNumber == "1" or secondNumber == "3")

def calculate_solution_l():
    print(complex(2,5))
    print(complex(-1,2)) 
    #return complex(2,5) ** complex(-1,2)
    return 2+5j ** -1+2j

def calculate_solution_m(i:int):
    return 1j**1j

def calculate_solution_n():
    # Wurzel ziehen und mit Modulo 1 prüfen ob das Ergebnis eine ganze Zahl ist
    return ((345744 ** 0.5) % 1) == 0

if __name__ == "__main__":
    print(calculate_solution_n())


# Aufgabe 1.1
    
# a) str, list, tuple
# b) list, dict
# c) list[-1] index -1 => letztes Element
# d) type(variable) => type Methode gibt typ zurück
# e) return => gibt Wert zurück oder springt aus Methode frühzeitig raus, print() gibt Wert in der Konsole aus