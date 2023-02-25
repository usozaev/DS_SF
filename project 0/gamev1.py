import numpy as np
number = np.random.randint(1, 5) # генерация рандомного числа от 1 до 100

#считаем кол-ов попыток угадывания
count = 0

while True:
    count= count+1
    predict_number = int(input("Угадай число от 1 до 100:  "))
    
    if predict_number > number:
        print("Число должно быть меньше")
    elif predict_number < number:
        print("Число должно быть больше")
    
    else:
        print(f"Вы угадали число! Это число = {number} за  {count} попыток")
        break #конец игры и выход из игры 