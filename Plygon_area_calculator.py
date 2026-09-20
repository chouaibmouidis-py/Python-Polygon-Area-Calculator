import math


class Rectangle:
    """
    Classe représentant un rectangle.
    Permet de calculer l'aire, le périmètre, la diagonale et de générer une représentation visuelle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, w):
        """Modifie la largeur du rectangle."""
        self.width = w
        return self.width

    def set_height(self, h):
        """Modifie la hauteur du rectangle."""
        self.height = h
        return self.height

    def get_area(self):
        """Calcule l'aire du rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Calcule le périmètre du rectangle."""
        return (self.width + self.height) * 2

    def get_diagonal(self):
        """Calcule la diagonale du rectangle en utilisant le théorème de Pythagore."""
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        """Génère une représentation visuelle du rectangle avec des étoiles."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        result = ""
        for i in range(self.height):
            result += ("*" * self.width) + "\n"
        return result

    def get_amount_inside(self, other):
        """Calcule combien de fois une autre forme (Rectangle ou Square) rentre dans celle-ci."""
        width_fit = self.width // other.width
        height_fit = self.height // other.height
        return width_fit * height_fit


class Square(Rectangle):
    """
    Classe représentant un carré.
    Hérite de la classe Rectangle car un carré est un rectangle avec des côtés égaux.
    """

    def __init__(self, side):
        # On initialise le parent avec la même valeur pour la largeur et la hauteur
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, value):
        """Définit la longueur du côté pour la largeur et la hauteur."""
        self.width = value
        self.height = value
        return value

    def set_width(self, w):
        """Surcharge la méthode du parent pour maintenir la forme carrée."""
        self.width = w
        self.height = w
        return self.width

    def set_height(self, h):
        """Surcharge la méthode du parent pour maintenir la forme carrée."""
        self.height = h
        self.width = h
        return self.height
