def double(number):
    return number * 2

def increment(number, step=1):
    try:
        result = number + step
    except TypeError:
        print('Caught type error')

        try:
            result = int(number) + step
        except ValueError as e:
            print("Caught value error, 'number' is not a number")
            raise e

    return result

