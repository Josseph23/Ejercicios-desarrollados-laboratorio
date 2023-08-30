def calcular_fibonacci(n):
    fibonacci_series = []
    
    if n <= 0:
        return fibonacci_series
    
    if n == 1:
        fibonacci_series.append(0)
        return fibonacci_series
    
    fibonacci_series = [0, 1]  
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    
    return fibonacci_series

numero = int(input("Ingrese el valor de n para calcular la serie de Fibonacci: "))
fibonacci_resultado = calcular_fibonacci(numero)
print("La serie de Fibonacci hasta el", numero, "-ésimo término es:", fibonacci_resultado)
