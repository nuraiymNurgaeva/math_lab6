from sympy import *

x = Symbol('x')
y = Symbol('y')

f1 =sin (y+1)+1
f2 =1.5-sin(x-1)

f1_primeX = f1.diff(x)
f1_primeY = f1.diff(y)

f2_primeX = f2.diff(x)
f2_primeY = f2.diff(y)

f_primeX_sum = abs(f1_primeX) + abs(f2_primeX)
f_primeY_sum = abs(f1_primeY) + abs(f2_primeY)

f_primeX_sum = lambdify(x, f_primeX_sum)
f_primeY_sum = lambdify(y, f_primeY_sum)


def solve_by_simple_iterations(f1, f2, x0, y0, e):
    f1 = lambdify(y, f1)
    f2 = lambdify(x, f2)

    x1 = f1(y0)
    y1 = f2(x0)

    counter = 0
    print('%-3s %-7s %-7s %-7s %-7s' % ('n', 'xn', 'yn', 'eX', 'eY'))
    print('%-3d %-7.3f %-7.3f' % (counter, x0, y0))
    while True:
        counter += 1
        eX = abs(x1 - x0)
        eY = abs(y1 - y0)

        if eX < e and eY < e:
            break

        x0 = x1
        y0 = y1
        print('%-3d %-7.3f %-7.3f %-7.3f %-7.3f' % (counter, x0, y0, eX, eY))

        x1 = f1(y0)
        y1 = f2(x0)


x0 = 2.0
y0 = 0.5
e = 0.001

if (f_primeX_sum(x0) < 1) and (f_primeY_sum(y0) < 1):
    solve_by_simple_iterations(f1, f2, x0, y0, e)