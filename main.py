from geometry_square import GeometrySquare
from figures import Triangle


def execute_application():
    a = float(input("Введите сторону треугольника A: "))
    b = float(input("Введите сторону треугольника B: "))
    c = float(input("Введите сторону треугольника C: "))
    try:
        triangle = Triangle.is_triangle(a, b, c)
        triangle.h_a = triangle.height("a")
        triangle.square = GeometrySquare.triangle_square_1(triangle.a, triangle.h_a)
        print(triangle)
        print(f"Площадь: {triangle.square} м.кв")
    except Exception as e:
        print(e)




if __name__ == "__main__":
    execute_application()