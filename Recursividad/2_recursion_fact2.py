def factorial(fact):
    if fact>0:
        valor = fact * factorial(fact-1)
        return valor
    else:
        return 1;

print("El factorial de 5 es",factorial(5))