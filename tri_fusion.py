def fusion (tbl1: list, tbl2: list) -> list:
    # Initialisation
    N1, N2 = len(tbl1), len(tbl2)
    i1 = 0
    i2 = 0
    tbl = []

    # Boucle sur les deux tableaux
    while (i1 < N1) and (i2 < N2):
        x1, x2 = tbl1[i1], tbl2[i2]
        # si x1 < x2  on ajoute l'élément x1 à tbl
        if x1 <= x2:
            tbl.append(x1)
            i1 = i1 + 1
        # sinon on ajoute l'élément x2
        else:
            tbl.append(x2)
            i2 = i2 + 1

    # Finalisation: On ajoute les éléments restants du tableau non vide restant
    # Si tbl1 n'a pas été entièrement vidé, on ajoute ses éléments restants
    if i1 < N1:
        for i in range(i1, N1):
            tbl.append(tbl1[i])
    # Sinon on ajoute les éléments de tbl2 restants
    elif i2 < N2:
        for i in range(i2, N2):
            tbl.append(tbl2[i])
        
    return tbl

def tri_fusion (tbl: list) -> list:
    N = len(tbl)
    # cas de base: un tableau de zéro ou un élément est forcément trié!
    if N < 2:
        return tbl
    
    # on coupe le tableau en deux
    tbl1 = [tbl[i] for i in range(N//2)]
    tbl2 = [tbl[i] for i in range(N//2, N)]
    
    # appels récursifs
    return fusion(tri_fusion(tbl1), tri_fusion(tbl2))

print (tri_fusion([0, 25, 36, 41, 1, 465, 2, 3, 987]))