import random
import quicksortcrafter_hi as q_hi

liste = random.sample(range(0,100),90)
#print(liste)
#q_hi.quicksort(liste)

def bubblesort(liste):
    for i in range(1,len(liste)):
        for bbv in range(len(liste)-i):
            if liste[bbv]>liste[bbv+1]:
                liste.insert(bbv,liste.pop(bbv+1))
    return liste

folge = [(3**i-1)//2 for i in range(4,0,-1)] #mathematisch sinnvoll für hohe Effizienz
print(folge)


def shellshort(liste):
    for divident in folge:
        liste2d=[]
        for i in range(0,divident):
            liste2d.append([])
            
        for i in range(0,len(liste2d)):
            stelle=i
            while stelle<len(liste):
                liste2d[i].append(liste[stelle])
                stelle+=divident

        liste=[]
        for i in liste2d:
            i=bubblesort(i)
            liste=liste+i

    return liste
