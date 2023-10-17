import random
def headder():
    print(" n     vDinamic   tDimanic   vGreedy   tGreedy     %")
    print("______________________________________________________")


def generate_prices(size):
    return [random.randint(1, 10) for _ in range(size)]

