from sympy import *

a1, b1, a2, b2 = symbols(r'\alpha_1 \beta_1 \alpha_2 \beta_2')
c1 = (a1 ** 2 + b1 ** 2) / 2
c2 = (a2 ** 2 + b2 ** 2) / 2
m1 = Matrix([[1, 0, -a1, a1],
             [0, 1, -b1, b1],
             [a1, b1, 1 - c1, c1],
             [a1, b1, -c1, 1 + c1]])
m2 = Matrix([[1, 0, -a2, a2],
             [0, 1, -b2, b2],
             [a2, b2, 1 - c2, c2],
             [a2, b2, -c2, 1 + c2]])
m3=factor(simplify(m1*m2))
pprint(m3)
print(latex(m3))
