def divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input('Ingrese un numero: '))
        print(divisor(num))
        if num < 0:
            raise ValueError('Invalid, solo pueden ser numeros positivos')
        print('Termino mi programa')
    except ValueError as ev:
        print(ev)
            

    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    run()
    