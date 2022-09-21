import math

def square_eq_solver(a, b, c):
    if math.isclose(a, 0)and math.isclose(b, 0) and math.isclose(c, 0):
        print('any x is a solution')
        return
    if math.isclose(a, 0):
        if not math.isclose(b, 0):
            return (-c / b)
        else:
            print(f'incorrect input data: {c} != 0')
            return
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        return None
    elif math.isclose(discr, 0):
        return (-b / (2 * a), -b / (2 * a))
    else:
        return ((-b + discr ** 0.5) / (2 * a), (-b - discr ** 0.5) / (2 * a))
    

if __name__ == '__main__':
    assert (square_eq_solver(0, 0, 0) is None)
    assert (square_eq_solver(0, 0, 1) is None)
    assert (square_eq_solver(1, 1, 1) is None)
    assert (square_eq_solver(1, 2, 1) == (-1, -1))
    assert (math.isclose(square_eq_solver(1, 5, 1)[1], -4.79, rel_tol = 0.001) 
            and math.isclose(square_eq_solver(1, 5, 1)[0], -0.208, rel_tol = 0.01)) # just for fun
