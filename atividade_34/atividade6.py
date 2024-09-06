# Função para verificar se um número é primo
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Lista de números de 1 a 20
numbers = list(range(1, 21))

# Verifica quais números são primos
primes = [num for num in numbers if is_prime(num)]

print("Números primos de 1 a 20:", primes) 
