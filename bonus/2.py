celsi = input("Введите градусы Цельсия (дробную часть - через точку): ")

if celsi == "":
    print("Вы ввели не число, попробуйте ещё раз")
else:
    celsi = float(celsi)
    farenh = celsi * 1.8 + 32
    kelvin = celsi + 273.15
    print(round(farenh, 2), "градусов Фаренгейта")
    print(round(kelvin, 2), "градусов Кельвина")
