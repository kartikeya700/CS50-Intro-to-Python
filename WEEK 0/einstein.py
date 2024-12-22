def main():
    # Take mass input from user
    mass = input("Enter mass in kilograms(kg) - ")

    # Energy calculation
    c_square = pow(300000000, 2)
    Energy = int(mass) * c_square
    print(Energy, "Joules(J)")


main()
