# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect(contenu : int) -> bool:
    """Fonction qui vérifie si le contenu est compris entre 0 et 8 ou égal à la constante const.ID_MINE"""
    res = False
    if type(contenu) == int:
        if (0 <= contenu and contenu <= 8) or contenu == const.ID_MINE:
            res = True
    return res

def construireCellule(contenu : int = 0, visible : bool = False) -> dict:
    """Fonction qui crée une cellule avec un contenu et une visibilité"""
    if isContenuCorrect(contenu) and type(visible) == bool:
        cellule = {const.CONTENU: contenu, const.VISIBLE: visible, const.ANNOTATION : None, const.RESOLU :False}
        return cellule
    elif type(visible) != bool:
        raise TypeError(f"construireCellule : le second paramètre {type(visible)} n’est pas un booléen")
    else:
        raise ValueError(f"construireCellule : le contenu {contenu} n’est pas correct")

def getContenuCellule(cellule : dict) -> int:
    """Fonction qui récupère le contenu de la cellule"""
    if type_cellule(cellule):
        return cellule[const.CONTENU]
    else:
        raise TypeError("« getContenuCellule : Le paramètre n’est pas une cellule.")

def isVisibleCellule(cellule :dict) -> bool:
    """Fonction qui récupère la visibilité de la cellule"""
    if type_cellule(cellule):
        return cellule[const.VISIBLE]
    else:
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule.")

def setContenuCellule(cellule : dict, contenu : int) -> None:
    """Fonction qui modifie le contenu de la cellule"""
    if not type_cellule(cellule):
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")
    elif type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    elif not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : la valeur du contenu {contenu} n’est pas correcte.")
    else:
        cellule[const.CONTENU] = contenu

def setVisibleCellule(cellule : dict, visible : bool) -> None:
    """Fonction qui modifie la visibilité de la cellule"""
    if not type_cellule(cellule):
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    elif type(visible) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")
    else:
        cellule[const.VISIBLE] = visible

def contientMineCellule(cellule : dict) -> bool:
    """Fonction qui dit si la cellule contient une mine ou non"""
    res = False
    if not type_cellule(cellule):
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule.")
    if cellule[const.CONTENU] == const.ID_MINE:
        res = True
    return res

def isAnnotationCorrecte(annotation : str) -> bool:
    return annotation in [None, const.DOUTE, const.FLAG]

def getAnnotationCellule(cellule : dict) -> str:
    if not type_cellule(cellule):
        raise TypeError(f"getAnnotationCellule : le paramètre {cellule} n’est pas une cellule")
    elif const.ANNOTATION not in cellule:
        return None
    elif isAnnotationCorrecte(cellule[const.ANNOTATION]):
        return cellule[const.ANNOTATION]

def changeAnnotationCellule(cellule : dict) -> None:
    if not type_cellule(cellule):
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule")
    else:
        annotations = [None, const.DOUTE, const.FLAG]
        if cellule[const.ANNOTATION] == None:
            cellule[const.ANNOTATION] = const.FLAG
        elif cellule[const.ANNOTATION] == const.FLAG:
            cellule[const.ANNOTATION] = const.DOUTE
        else:
            cellule[const.ANNOTATION] = None
    return None


def reinitialiserCellule(cellule : dict) -> None:
    cellule[const.CONTENU] = 0
    cellule[const.VISIBLE] = False
    cellule[const.ANNOTATION] = None
    return None

