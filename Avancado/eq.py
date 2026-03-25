import math

def bashkara (a1, b1 ,c1):

    delta = b1**2 -4*a1*c1
    if delta < 0:
        return 'Sem solucao real!! '
    else:
        x1 = (-b1 + math.sqrt(delta)) / (2 * a1)
        x2 = (-b1 - math.sqrt(delta)) / (2 * a1)
        return f'O valor de x1 e {x1:.2f} e o valor de x2 e {x2:.2f}'
    
resultado = bashkara
print('{}'.format(resultado))

def rq(x):
        if x < 0:
            return "Error, nao existe raiz quadrada negativa"
        return math.sqrt(x)

def rc(x):
    
    if x >= 0:
        return x ** (1/3)
    else:
        return -((-x) ** (1/3))

def ptc(base, expoente):
     return base ** expoente

def callog (num, base):
     if num > 0 and base > 0 and base != 1:
          return math.log(num, base)
     return 'Error: valores invalidos'