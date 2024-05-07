
class Graph:
    def __init__(self) -> None:
        self.graph = {"nodes": [], "edges": []}

    def addNode(self, k) -> None:
        if k not in self.graph["nodes"]:
            self.graph["nodes"] = [*self.graph["nodes"], k]
            # self.graph["nodes"].append(k)

    def addEdge(self, k1, k2) -> None:
        if k1 not in self.graph["nodes"] or k2 not in self.graph["nodes"]:
            return
        self.graph["edges"].append((k1, k2))

    def getGraph(self) -> dict:
        return self.graph

    def E(self) -> list:
        return self.graph["edges"]
    
    def V(self) -> list:
        return self.graph["nodes"]
    
    def allSingles(self) -> list:
        return [node for node in self.graph["nodes"] if node not in [edge[0] for edge in self.graph["edges"]] and node not in [edge[1] for edge in self.graph["edges"]]]

    def mostEdges(self) -> int:
        edgesPerNode = {}
        for node in self.graph["nodes"]:
            edgesPerNode[node] = 0;
            for edge in self.graph["edges"]:
                
                if edge[0] is node or edge[1] is node:
                    edgesPerNode[node] += 1;

        print(edgesPerNode)

        return max(edgesPerNode, key=edgesPerNode.get)
    
    def neighbours(self, v:int) -> list: 
        neighbours = []
        for a, b in [edge for edge in self.graph["edges"] if v in edge]:
            if a not in neighbours and b not in neighbours: 
                if a is not v:
                    neighbours.append(a)
                elif b is not v:
                    neighbours.append(b)

        return neighbours;
        

class Cntr:
    def __init__(self, word:str) -> None:
        self.cntr : dict = {}
        for l in word:
            if l not in self.cntr:
                self.cntr[l] = 1
            else:
                self.cntr[l] += 1

    def __repr__(self) -> str:
        for k in self.cntr.keys():
            print(f"{k}:{self.cntr[k]}")

    def most(self) -> str:
        largestKey = list(self.cntr.keys())[0];
        for k in self.cntr.keys():
            if self.cntr[largestKey] < self.cntr[k]:
                largestKey = k

        return largestKey
        
    def __add__ (self, other) -> dict:
        for k in self.cntr.keys():
            for k2 in other.cntr.keys():
                if k is k2:
                    self.cntr[k] += other.cntr[k2]

        return self.cntr

    def __mul__ (self, other) -> dict:
        for k in self.cntr.keys():
            for k2 in other.cntr.keys():
                if k is k2:
                    self.cntr[k] *= other.cntr[k2]

        return self.cntr


if __name__ == "__main__":
    g = Graph()
    
    for i in range (1 ,6): 
        g.addNode (i)
    for i ,j in [(1 ,2) ,(2 ,2) ,(1 ,3) ,(2 ,3) ,(3 ,4) ,(1 ,4) ,(4 ,5) ,(5 ,1)]:
        g.addEdge(i,j)

    graph = g.getGraph()
    print(g.mostEdges()) 
    print(g.neighbours(1))   

    c = Cntr("Hello World!")
    c2 = Cntr("Hallo Welt!")
    c.__repr__()
    print(c.most())
    
    #print(c + c2)
    
    print(c * c2)


