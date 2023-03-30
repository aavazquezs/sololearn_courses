import math
w1, w2, b, x1, x2 = [float(x) for x in input().split()]
entrada = w1*x1+w2*x2+b
y = 1 / (1 + math.exp(-1*entrada))
print(round(y,4))