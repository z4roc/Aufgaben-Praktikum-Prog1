
def isReflexive(menge:list, relation:list) -> bool:
    for i in menge:
        if (i, i) not in relation:
            return False
    return True

    # for tup in relation:
       # if set(list(tup)).issubset(set(menge)):
        #    return True
        
    
    # return False

def isSymmetric(menge, relation) -> bool:
    for tup in relation:
        if (tup[1], tup[0]) not in relation:
            return False
    return True

def calc_aufgabe_a(s:int, e:int) -> int:
    return sum(range(s,e))

def calc_aufgabe_b():
    return sum([i for i in range(0, 100) if i % 3 is 0])

def calc_aufgabe_c():
    return [i for i in range(0, 100) if i % 11 != 0 and i % 13 != 0]

def calc_aufgabe_d():
    return len([i for i in range(0, 1000) if sum([int(j) for j in str(i)]) % 7 == 0])

if __name__ == "__main__":
    print(calc_aufgabe_d())
    print(isReflexive([1,2,3], [(1,2) ,(1,1) ,(2,2) ,(2,1) ,(3,3)]))
    print(isReflexive([1,2,3], [(1,1), (2,2)]))
    print(isSymmetric([1 ,2 ,3] ,[(1 ,2) ,(2 ,1) ,(2 ,2) ,(1 ,3) ,(3 ,1)]))
    print(isSymmetric([1 ,2 ,3] ,[(1 ,2) ,(2 ,1) ,(2 ,2) ,(1 ,3)]))