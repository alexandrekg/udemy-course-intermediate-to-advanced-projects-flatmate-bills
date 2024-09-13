from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
            and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


# Criar objeto retângulo
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

# Printar coordenadas do retângulo
print("Coordenadas do retângulo: ",
      rectangle.point1.x, ", ",
      rectangle.point1.y, "and",
      rectangle.point2.x, ", ",
      rectangle.point2.y)


# Pegar ponto e área do usuário
user_point = Point(float(input("Adivinhe X: ")), float(input("Advinhe Y:")))
user_area = float(input("Advinhe a área do retângulo: "))

# Mostrar o resultado do jogo
print("Seu ponto estava dentro do retângulo: ", user_point.falls_in_rectangle(rectangle))
print("Sua área estava fora por: ", rectangle.area() - user_area)