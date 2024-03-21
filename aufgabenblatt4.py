def umrechnenTemperatur(termperatur:str):
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

def istZahlPrimzahl(n:int):
    # nicht nötig wegen typesafe Parameter aber trotzdem:
    if type(n) is not int:
        raise Exception("Falsche Eingabe")
    
    return n > 1 and all(n % i is not 0 for i in range(2, n))


if __name__ == "__main__":
    print(umrechnenTemperatur("0C"))
    print(umrechnenTemperatur("0F"))
    print(umrechnenTemperatur("0K"))

    primzahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in primzahlen:
        print(istZahlPrimzahl(i))
