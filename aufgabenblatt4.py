import matplotlib.pyplot as plt

# Aufgabe 4.0
def umrechnenTemperatur(termperatur:str) -> dict:
    einheiten = ["C", "F", "K"]
    tempurEinheit = termperatur[-1]
    temperaturenDictionary = {"C": 0, "F": 0, "K": 0}

    if tempurEinheit not in einheiten:
        raise Exception("Falsche Eingabe")
    
    temperaturWert = int(termperatur[:-1])

    if tempurEinheit == "C":
        temperaturenDictionary["C"] = temperaturWert
        temperaturenDictionary["F"] = temperaturWert * 9/5 + 32
        temperaturenDictionary["K"] = temperaturWert + 273.15
    elif tempurEinheit == "F":
        temperaturenDictionary["F"] = temperaturWert
        temperaturenDictionary["C"] = (temperaturWert - 32) * 5/9
        temperaturenDictionary["K"] = (temperaturWert - 32) * 5/9 + 273.15
    else:
        temperaturenDictionary["K"] = temperaturWert
        temperaturenDictionary["C"] = temperaturWert - 273.15
        temperaturenDictionary["F"] = (temperaturWert - 273.15) * 9/5 + 32

    return temperaturenDictionary

# Aufgabe 4.1
def istZahlPrimzahl(n:int) -> bool:
    if type(n) is not int:
        raise Exception("Falsche Eingabe")
    
    return n > 1 and all(n % i != 0 for i in range(2, n))

# Aufgabe 4.2
def findeZwillingsprimzahlen() -> tuple:
    primzahlen = [i for i in range(2, 10000) if istZahlPrimzahl(i)]

 


    print(primzahlen)
    zwillingsPrimzahlen = [i for i in primzahlen if i + 2 in primzahlen]

    zwillingsPrimzahlenManuell = []
    for i in primzahlen:
        if i + 2 in primzahlen:
            zwillingsPrimzahlenManuell.append((i, i + 2))

    return len(zwillingsPrimzahlen), len(zwillingsPrimzahlenManuell)

def erstelleStreudiagramm_4_a():
    plt.scatter(range(10), range(10));
    plt.show()

def erstelleStreudiagramm_4_b():
    plt.scatter(range(20)[::-1],range(20))
    plt.show()

def erstelleStreudiagramm_4_c():
    #plt.scatter([i for i in range(1,10)], [i for i in range(1,10)]);
    #plt.scatter([-i for i in range(1,10)], [i for i in range(1,10)])
    #plt.scatter([i for i in range(-20,20)], [i for i in range(20,-20, -1)])
   
    # Werte für jede Achse erzeugen
    x = [i for i in range(-10, 10)]
    y = [10 for i in range(-10, 10)]

    x += [i for i in range(-10, 10)]
    y += [-10 for i in range(-10, 10)]

    x += [-10 for i in range(-10, 10)]
    y += [i for i in range(-10, 10)]

    x += [10 for i in range(-10, 10)]
    y += [i for i in range(-10, 10)]

    y+= [10]
    x+= [10]

    plt.scatter(x, y)
    plt.show()

if __name__ == "__main__":
    #print(findeZwillingsprimzahlen())
    erstelleStreudiagramm_4_b()
