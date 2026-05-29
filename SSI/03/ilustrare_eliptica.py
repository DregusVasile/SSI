p = 17

def inverse_mod(a, p):
    return pow(a, -1, p)


def add_points(P, Q, a, p):
    x1, y1 = P
    x2, y2 = Q

    if P != Q:
        m = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p
    else:
        m = ((3 * x1 * x1 + a) * inverse_mod(2 * y1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)


P = (0, 6)
Q = (1, 9)
a = 2

R = add_points(P, Q, a, p)

print("P + Q =", R)