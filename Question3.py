# Question 3
# This program calculates monthly mortgage payments 

def calcPmt(P0, r, k, N):
    d = P0 / ((1 - (1 + r/k) ** (-N * k)) / (r / k))
    return d

def main():
    P0 = float(input("What is the amount to finance? "))
    r = float(input("What is the annual interest rate? ")) / 100
    k = int(input("Number of times interest is compounded in a year: "))
    N = int(input("Number of years: "))

    d = calcPmt(P0, r, k, N)
    print("Monthly payment:", d)

main()