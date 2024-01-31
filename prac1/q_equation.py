import cmath

def solve_quadratic_equation(a, b, c):
    discriminant = cmath.sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)
    return x1, x2