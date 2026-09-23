# Question 2

def kToF(k):
    fahrenheit = (k - 273.15) * 9 / 5 + 32
    return fahrenheit

def main():
    for k in range(0, 301, 20):
        f = kToF(k)
        print(k, f)

main()