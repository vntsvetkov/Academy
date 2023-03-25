from geometry_square import GeometrySquare
from figures import Triangle


def execute_application():

    triangle = Triangle()
    while True:
        triangle.a = float(input("Введите сторону треугольника A (м): "))
        triangle.b = float(input("Введите сторону треугольника B (м): "))
        triangle.c = float(input("Введите сторону треугольника C (м): "))
        if Triangle.is_triangle(triangle.a, triangle.b, triangle.c):
            break
        else:
            print("Треугольника с такими сторонами не существует")

    triangle.h_a = triangle.height("a")
    triangle.square = GeometrySquare.triangle_square_by_side_and_height(triangle.a, triangle.h_a)
    print(f"Площадь: {triangle.square} (м.кв)")


if __name__ == "__main__":
    execute_application()