# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nl : int, nc : int) -> list:
    """Fonction qui crée une grille"""
    if type(nl) != int or type(nc) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes {type(nl)} ou de colonnes {type(nc)} n’est pas un entier.")
    elif nl <= 0 or nc <= 0:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes {nl} ou de colonnes {nc} est négatif ou nul.")
    else:
        grille = []
        for ligne in range(nl):
            lg = []
            for colonne in range(nc):
                lg.append(construireCellule())
            grille.append(lg)
    return grille

def getNbLignesGrilleDemineur(grille : list) -> int:
    """Fonction qui récupère le nombre de ligne"""
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    else:
        return len(grille)

def getNbColonnesGrilleDemineur(grille : list) -> int:
    """Fonction qui récupère le nombre de colonne"""
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    else:
        return len(grille[0])

def isCoordonneeCorrecte(grille : list, coord : tuple) -> bool:
    """Fonction qui vérifie si la coordonnée est présente dans la grille"""
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type")
    else:
        return coord[0] < getNbLignesGrilleDemineur(grille) and coord[1] < getNbColonnesGrilleDemineur(grille)

def getCelluleGrilleDemineur(grille : list, coord : tuple) -> dict:
    """Fonction qui donne la cellule aux coordonnées si elles sont dans la grille"""
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if not isCoordonneeCorrecte(grille,coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    else:
        return grille[coord[0]][coord[1]]

def  getContenuGrilleDemineur(grille : list, coord : tuple)  -> int:
    """Fonction qui renvoie le contenu de la cellule aux coordonnées dans la grille"""
    return getContenuCellule(getCelluleGrilleDemineur(grille,coord))

def setContenuGrilleDemineur(grille : list, coord : tuple, contenu : int) -> None:
    """Fonction qui modifie le contenu de la cellule aux coordonnées dans la grille"""
    setContenuCellule(getCelluleGrilleDemineur(grille,coord),contenu)
    return None

def isVisibleGrilleDemineur(grille : list, coord : tuple) -> bool:
    """Fonction qui renvoie la visibilité de la cellule aux coordonnées dans la grille"""
    return isVisibleCellule(getCelluleGrilleDemineur(grille,coord))

def setVisibleGrilleDemineur(grille : list, coord : tuple, visible : bool) -> None:
    """Fonction qui modifie la visibilité de la cellule aux coordonnées dans la grille"""
    setVisibleCellule(getCelluleGrilleDemineur(grille,coord),visible)
    return None

def contientMineGrilleDemineur(grille : list, coord : tuple) -> bool:
    """Fonction qui dit si la cellule aux coordonnées coord contient une mine True ou non False"""
    return contientMineCellule(getCelluleGrilleDemineur(grille,coord))


def getCoordonneeVoisinsGrilleDemineur(grille : list, coord : tuple) -> list:
    """Fonction qui récupère les voisins d'une coordonnée"""
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    elif not isCoordonneeCorrecte(grille,coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    else:
        voisins = []
        for lg in range(coord[0]-1, coord[0]+2):
            for cl in range(coord[1]-1, coord[1]+2):
                if lg >= 0 and cl >= 0 and (lg,cl) != coord:
                    cd = (lg,cl)
                    if isCoordonneeCorrecte(grille,cd):
                        voisins.append(cd)
        return voisins

def placerMinesGrilleDemineur(grille : list, nb : int, coord : tuple) -> None:
    """Fonction qui place nb bombes dans la grille mais n'en pose pas dans la cellule aux coordonnées coord"""
    lignes = getNbLignesGrilleDemineur(grille)
    colonnes = getNbColonnesGrilleDemineur(grille)
    if nb < 0 or nb >= lignes * colonnes:
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    elif not isCoordonneeCorrecte(grille,coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    else:
        while nb != 0:
            rd_lg = randint(0, lignes-1)
            rd_cl = randint(0, colonnes-1)
            if not contientMineGrilleDemineur(grille,(rd_lg,rd_cl)) and (rd_lg,rd_cl) != coord:
                setContenuGrilleDemineur(grille,(rd_lg,rd_cl),const.ID_MINE)
                nb -= 1
        compterMinesVoisinesGrilleDemineur(grille)
    return None

def compterMinesVoisinesGrilleDemineur(grille : list) -> None:
    """Fonction qui compte le nombre de mines présentes dans les 8 cellules voisines d'une cellule"""
    lignes = getNbLignesGrilleDemineur(grille)
    colonnes = getNbColonnesGrilleDemineur(grille)
    for lg in range(lignes):
        for cl in range(colonnes):
            cpt = 0
            voisins = getCoordonneeVoisinsGrilleDemineur(grille,(lg,cl))
            for voisin in voisins:
                if contientMineGrilleDemineur(grille,voisin) and not contientMineGrilleDemineur(grille,(lg,cl)):
                    cpt += 1
            if not contientMineGrilleDemineur(grille,((lg,cl))):
                setContenuGrilleDemineur(grille,(lg,cl),cpt)
    return None

def getNbMinesGrilleDemineur(grille : list) -> int:
    """Fonction qui compte le nombre de mine dans la grille"""
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    else:
        cpt = 0
        lignes = getNbLignesGrilleDemineur(grille)
        colonnes = getNbColonnesGrilleDemineur(grille)
        for ligne in range(lignes):
            for colonne in range(colonnes):
                if contientMineGrilleDemineur(grille, (ligne, colonne)):
                    cpt += 1
    return cpt


def getAnnotationGrilleDemineur(grille : list, coord : tuple) -> str:
    """Fonction qui donne l'annotation de la cellule aux coordonnées coord dans la grille"""
    return getAnnotationCellule(getCelluleGrilleDemineur(grille,coord))

def getMinesRestantesGrilleDemineur(grille : list) -> int:
    """Fonction qui donne le nombre de mines restantes dans la grille"""
    nb_flag = 0
    lignes = getNbLignesGrilleDemineur(grille)
    colonnes = getNbColonnesGrilleDemineur(grille)
    for lg in range(lignes):
        for cl in range(colonnes):
            annotation = getAnnotationGrilleDemineur(grille,(lg,cl))
            if annotation == const.FLAG:
                nb_flag += 1
    return getNbMinesGrilleDemineur(grille) - nb_flag

def gagneGrilleDemineur(grille : list) -> bool:
    """
    Fonction qui vérifie si la partie est gagné
    Gagné si toutes les cellules n'ayant pas de mine sont découvertes et qu'aucune mine ne soit découverte
    Perdu sinon.
    """
    lignes = getNbLignesGrilleDemineur(grille)
    colonnes = getNbColonnesGrilleDemineur(grille)
    gagne = True
    for lg in range(lignes):
        for cl in range(colonnes):
            cd = (lg, cl)
            if (not contientMineGrilleDemineur(grille, cd) and not isVisibleGrilleDemineur(grille, cd)) or (contientMineGrilleDemineur(grille, cd) and isVisibleGrilleDemineur(grille, cd)):
                gagne = False
    return gagne

def perduGrilleDemineur(grille : list) -> bool:
    """Fonction qui vérifie si la partie est perdue
    Perdue si une cellule ayant une mine est découverte
    En cours sinon
    """
    lignes = getNbLignesGrilleDemineur(grille)
    colonnes = getNbColonnesGrilleDemineur(grille)
    perdu = False
    for lg in range(lignes):
       for cl in range(colonnes):
            cd = (lg, cl)
            if contientMineGrilleDemineur(grille, cd) and isVisibleGrilleDemineur(grille,cd):
                perdu = True
    return perdu

def reinitialiserGrilleDemineur(grille : list) -> None:
    """Fonction qui réinistialise la grille du démineur"""
    lignes = getNbLignesGrilleDemineur(grille)
    colonnes = getNbColonnesGrilleDemineur(grille)
    for lg in range(lignes):
        for cl in range(colonnes):
            reinitialiserCellule(getCelluleGrilleDemineur(grille,construireCoordonnee(lg,cl)))
    return None


def decouvrirGrilleDemineur(grille : list, coord : tuple) -> set:
    """
    Fonction qui découvre la grille selon les voisins d'une coordonnée coord et si dans les voisins,
    il y a une cellule qui n'a pas de mine dans les cellules voisines, on relance la fonction avec les voisins
    avec la cellule qui a 0 mine dans ces voisins
    """
    setVisibleGrilleDemineur(grille, coord, True)
    cellule_dc = set()
    cellule_dc.add(coord)
    if getContenuGrilleDemineur(grille,coord) == 0:
        voisins = getCoordonneeVoisinsGrilleDemineur(grille,coord)
        for voisin in voisins:
            if getAnnotationGrilleDemineur(grille,voisin) == None and not isVisibleGrilleDemineur(grille,voisin):
                setVisibleGrilleDemineur(grille,voisin,True)
                cellule_dc.add(voisin)
                if getContenuGrilleDemineur(grille,voisin) == 0 and getAnnotationGrilleDemineur(grille,voisin) is None:
                    temp = decouvrirGrilleDemineur(grille,voisin)
                    for tp in temp:
                        cellule_dc.add(tp)
                    temp.clear()
    return cellule_dc

def simplifierGrilleDemineur(grille : list, coord : tuple) -> set:
    """
    Fonction qui découvre les coordonnées voisines à coord lorsque le nombre de drapeaux est égal au nombre
    de voisins ayant une mine pour une coordonnée coord
    """
    cellule_dc = set()
    if not isVisibleGrilleDemineur(grille,coord):
        return cellule_dc
    else:
        if not getCelluleGrilleDemineur(grille,coord)[const.RESOLU]:
            cellule_dc.add(coord)
            voisins = getCoordonneeVoisinsGrilleDemineur(grille,coord)
            nb_flag = 0
            for voisin in voisins:
                if getAnnotationGrilleDemineur(grille,voisin) == const.FLAG:
                    nb_flag += 1
            if nb_flag == getContenuGrilleDemineur(grille,coord):
                for voisin in voisins:
                    if getAnnotationGrilleDemineur(grille,voisin) != const.FLAG and not isVisibleGrilleDemineur(grille,voisin) and not getCelluleGrilleDemineur(grille,voisin)[const.RESOLU]:
                        setVisibleGrilleDemineur(grille,voisin,True)
                        cellule_dc.add(voisin)
                        temp = simplifierGrilleDemineur(grille,voisin)
                        for tp in temp:
                            cellule_dc.add(tp)
                        temp.clear()
        return cellule_dc

def ajouterFlagsGrilleDemineur(grille :list, coord : tuple)-> set:
    """Fonction qui ajoute des drapeaux sur les cellules lorsque c'est évident"""
    flag = set()
    if not getCelluleGrilleDemineur(grille,coord)[const.RESOLU]:
        voisins = getCoordonneeVoisinsGrilleDemineur(grille,coord)
        cpt = 0
        for voisin in voisins:
            if not isVisibleGrilleDemineur(grille,voisin):
                cpt +=1
        if getContenuGrilleDemineur(grille,coord) == cpt:
            for voisin in voisins:
                if getAnnotationGrilleDemineur(grille,voisin) != const.FLAG and not isVisibleGrilleDemineur(grille,voisin) and not getCelluleGrilleDemineur(grille,voisin)[const.RESOLU]:
                    cellule = getCelluleGrilleDemineur(grille,voisin)
                    cellule[const.ANNOTATION] = const.FLAG
                    flag.add(voisin)
    return flag

def simplifierToutGrilleDemineur(grille : list) -> tuple:
    """Fonction qui simplifie le plus possible la grille"""
    flag = set()
    cellule_dc = set()
    lignes = getNbLignesGrilleDemineur(grille)
    colonnes = getNbColonnesGrilleDemineur(grille)
    for lg in range(lignes):
        for cl in range(colonnes):
            cd = construireCoordonnee(lg,cl)
            if not getCelluleGrilleDemineur(grille,cd)[const.RESOLU]:
                temp_cl = simplifierGrilleDemineur(grille, cd)
                modifs = len(temp_cl)
                for tp_cl in temp_cl:
                    cellule_dc.add(tp_cl)
                temp_cl.clear()
                temp_fl = ajouterFlagsGrilleDemineur(grille,cd)
                modifs += len(temp_fl)
                for tp_fl in temp_fl:
                    flag.add(tp_fl)
                temp_fl.clear()
                getCelluleGrilleDemineur(grille,cd)[const.RESOLU] == True
    if modifs >= 2 and not gagneGrilleDemineur(grille):
        donnees = simplifierToutGrilleDemineur(grille)
        for tp_cl in donnees[0]:
            cellule_dc.add(tp_cl)
        for tp_fl in donnees[1]:
            flag.add(tp_fl)
    print(cellule_dc,"sep",flag)
    return (cellule_dc,flag)