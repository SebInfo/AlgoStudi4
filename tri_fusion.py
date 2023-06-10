def fusion (tbl1: list, tbl2: list) -> list:
    n1, n2 = len(tbl1), len(tbl2)
    i = 0
    j = 0
    tbl = []

    # Boucle sur les deux tableaux
    while (i < n1) and (j < n2):
        x1, x2 = tbl1[i], tbl2[j]
        # si x1 < x2  on ajoute l'élément x1 à tbl
        if x1 <= x2:
            tbl.append(x1)
            i = i + 1
        # sinon on ajoute l'élément x2
        else:
            tbl.append(x2)
            j = j + 1

    # Finalisation: On ajoute les éléments restants du tableau non vide restant
    # Si tbl1 n'a pas été entièrement vidé, on ajoute ses éléments restants
    if i < n1:
        for i in range(i, n1):
            tbl.append(tbl1[i])
    # Sinon on ajoute les éléments de tbl2 restants
    elif j < n2:
        for i in range(j, n2):
            tbl.append(tbl2[i])
        
    return tbl

def tri_fusion (tbl: list) -> list:
    n = len(tbl) # taille du tableau
    if len(tbl) <= 1: # cas de base (un tableau vide ou avec un élement est trié)
        return tbl
    
    # on divise le tableau en deux
    tbl1 = [tbl[i] for i in range(n//2)]
    tbl2 = [tbl[i] for i in range(n//2, n)]
    
    # On règne avec les appels récursifs et on combine
    return fusion(tri_fusion(tbl1), tri_fusion(tbl2))

print (tri_fusion([0, 25, 36, 41, 1, 465, 2, 3, 987]))