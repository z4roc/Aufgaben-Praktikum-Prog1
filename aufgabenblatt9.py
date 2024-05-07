import random
import matplotlib.pyplot as plt

def createRandonList() -> list:
    return [random.randint(1, 6) for i in range(10)]

def countNumberOfThrows() -> float:
    t = [True for i in range(100000) if 1 in createRandonList()]
    return len(t) / 100000

def erstelleListeAllerTeiler(n) -> list:
    return [i for i in range(1, n + 1) if n % i == 0]

def alleZahlenMitAchtTeilern() -> list:
    return [i for i in range(1, 1000) if len(erstelleListeAllerTeiler(i)) == 8]

def ermittleZahlMitMeistenTeilern() -> list:
    return max([(len(erstelleListeAllerTeiler(i)), i+1) for i in range(1, 1000)])[1]

def plotAlleTeiler(teiler:list) -> None:
    plt.plot(range(1, len(teiler) + 1), teiler)
    plt.show()

if __name__ == "__main__":
    print(createRandonList())
    print(f"{countNumberOfThrows() * 100}%")
    print(erstelleListeAllerTeiler(45))
    print(ermittleZahlMitMeistenTeilern())
    plotAlleTeiler([len(erstelleListeAllerTeiler(i)) for i in range(1, 1000)])