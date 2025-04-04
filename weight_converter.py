weight = int(input('Input your weight: '))
unit = input("K(g) or L(bs): ")
if unit.lower() == 'l':
    converted = weight * 0.45
    print(f'You are {converted} kilos')

else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')