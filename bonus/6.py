weight = input("Введите свой вес (в килограммах): ")
height = input("Введите свой рост (в сантиметрах): ")

if weight == '' or height == '':
    print("Упс, кажется что-то пошло не так. Проверьте введенные Вами данные!")
else:
    weight = float(weight)
    height = float(height)
    height = height/100
    index = weight / (height**2)

    if index <= 16:
        print("у Вас выраженный дефицит массы тела.")
    elif index > 16 and index <= 18.5:
        print("У Вас недостаточная (дефицит) масса тела.")
    elif index > 18.5 and index <= 25:
        print("У Вас всё в норме")
    elif index > 25 and index <= 30:
        print("У Вас избыточная масса тела (предожирение).")
    elif index > 30 and index <= 35:
        print("У Вас ожирение первой степени.")
    elif index > 35 and index <= 40:
        print("У Вас ожирение второй степени.")
    elif index > 40:
        print("У Вас ожирение третьей степени (морбидное).")

