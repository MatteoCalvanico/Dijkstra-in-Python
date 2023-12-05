import numpy as np

#Definizione funzioni:
def importGrafo(file):
    matrix = np.loadtxt(file, delimiter=";")
    return matrix

def isOriented(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]: 
                return True
    return False

def notAllNodeVisited(infoNodi):
    for node, visited in infoNodi.items():
        if(visited.get('visited') == False): 
            return True
    return False

def findVicini(nodo, matrix):
    return [vicino for vicino in range(len(matrix)) if matrix[nodo][vicino] > 0]

def distanza(n1, n2, matrix):
    return matrix[n1][n2]

def dijkstra(matrix, nodeStart):
    #Costruiamo un unico dizionario per salvare tutte le informazioni che ci servono
    infoNodi = {nodo: {'prev': 0, 'dist': 10000, 'visited': False} for nodo in range(len(matrix))} #prev: nodo precedente, dist: distanza minimi, visited: se lo abbiamo già visitato
    infoNodi[nodeStart]['dist'] = 0

    while notAllNodeVisited(infoNodi):  #Finchè ci saranno nodi non visitati continuo
        nodiNonVisitati = [node for node, info in infoNodi.items() if not info['visited']]
        nodoCorrente = min(nodiNonVisitati, key=lambda x: infoNodi[x]['dist'])
        infoNodi[nodoCorrente]['visited'] = True

        for vicino in findVicini(nodoCorrente, matrix):
            dist = infoNodi[nodoCorrente]['dist'] + distanza(nodoCorrente, vicino, matrix)
            if(dist < infoNodi[vicino]['dist']):
                infoNodi[vicino]['dist'] = dist
                infoNodi[vicino]['prev'] = nodoCorrente
    
    for nodo in infoNodi:
        info = infoNodi[nodo]
        print(f"Nodo: {nodo},Distanza: {info['dist']},Prec: {info['prev']}")

#-----------------------------------------------------
#-----------------------------------------------------

#Importiamo il grafo da csv:
mat = importGrafo("grafoEs.csv")

#-----------------------------------------------------

#Controlliamo se è orientato o meno:
if(isOriented(mat)):
    print("Il grafo dato è orientato")
else:
    print("Il grafo dato non è orientato")

#-----------------------------------------------------

#Applichiamo l'algoritmo scelto, Dijkstra:
dijkstra(mat, 0)
