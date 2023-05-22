# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0

def construireCoordonnee(num_ligne : int,  num_colonne : int) -> tuple:
    """Fonction qui crée une coordonnée avec un numéro de ligne et un numéro de colonne"""
    if type(num_ligne) == int and type(num_colonne) == int:
        return (num_ligne,num_colonne)
    elif type(num_ligne) != int or type(num_colonne) != int:
        raise TypeError(f"construireCoordonnee : Le numéro de ligne {type(num_ligne)} ou le numéro de colonne {type(num_colonne)} ne sont pas des entiers")
    else:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne  {num_ligne} ou de colonne {num_colonne} ne sont pas positifs")

def getLigneCoordonnee(coordonnee : tuple) -> int:
    """Fonction qui récupère la ligne de la coordonnée"""
    if type(coordonnee) == tuple:
        return coordonnee[0]
    else:
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")

def getColonneCoordonnee(coordonnee : tuple) -> int:
    """Fonction qui récupère la colonne de la coordonnée"""
    if type(coordonnee) == tuple:
        return coordonnee[1]
    else:
        raise TypeError("getColonneCoordonnee : Le paramètre n’est pas une coordonnée")

