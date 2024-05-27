class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, element) -> None:
        self.stack.append(element)

    def pop(self) -> any:
        return self.stack.pop()
    
    def toList(self) -> list:
        return self.stack
    
    def multPop(self, n:int) -> list:
        return [self.stack.pop() for i in range(n)]

class AufgabenManager:
    def __init__(self) -> None:
        self.aufgaben = {}

    def neueAufgabe(self, aufgabe:str, prioritaet:int) -> None:
        if prioritaet not in self.aufgaben:
            self.aufgaben[prioritaet] = Stack()
        self.aufgaben[prioritaet].push(aufgabe)

    def hoechstePrioritaet(self) -> str:
        return max(self.aufgaben.keys())

    def erledigeAufgabe(self) -> str:
        # output tuple? 
        # highestPrioItem = list(filter(lambda x: x[1] == self.hoechstePrioritaet(), self.aufgaben.items()))
        highestPrioItem = self.hoechstePrioritaet()
        aufgabe = self.aufgaben[highestPrioItem].pop()
        if len(self.aufgaben[highestPrioItem].toList()) == 0:
            del self.aufgaben[highestPrioItem]
        return aufgabe
    
    def alleAufgabenMitPrio(self, prio:int) -> list:
        return self.aufgaben[prio].toList()
    
    def allePrios(self) -> list:
        return list(self.aufgaben.keys())
    
    def anzahlAufgabenPrio(self, prio:int) -> int:
        return len(self.aufgaben[prio].toList())
    
    def anzahlAufgaben(self) -> int:
        return len(self.aufgaben)
    
if __name__ == "__main__":
    s = Stack()
    s.push(0)
    s.push(4.312)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop(), s.pop())
    s.push(True)
    print(s.pop())
    s.push("Hallo")
    print(s.multPop(3))

    am = AufgabenManager()
    am.neueAufgabe("Aufgabe 1", 1)
    am.neueAufgabe("Aufgabe 3", 3)
    am.neueAufgabe("Aufgabe 4", 4)
    am.neueAufgabe("Aufgabe 2", 2)
    am.neueAufgabe("Aufgabe 5", 1)


    print(am.alleAufgabenMitPrio(1))

    print(am.allePrios())
    print(am.anzahlAufgabenPrio(1))
    print(am.anzahlAufgaben())
    # print(am.hoechstePrioritaet())
    # print(am.erledigeAufgabe())
    # print(am.aufgaben)