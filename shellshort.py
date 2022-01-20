def bubblesort(liste):
    for i in range(1,len(liste)):
        for bbv in range(len(liste)-i):
            if liste[bbv]>liste[bbv+1]:
                liste.insert(bbv,liste.pop(bbv+1))
    return liste


def shellshort(liste):
    f=int(log(len(liste)+1,3))
    folge = [(3**j-1)//2 for j in range(f,0,-1)] #mathematisch sinnvoll für hohe Effizienz
    print(folge)
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

        for i in range(0,len(liste2d[0])):
            for l in liste2d:
                if len(l)>i:
                    liste.append(l[i])  

    return liste
