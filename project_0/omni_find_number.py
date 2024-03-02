import numpy as np
"""Игра угадай число.
Компьютер сам загадывает и угадывает число за минимальное количество попыток
"""

def random_predict(number:int=1) -> int:
    """угадываем число в интевале от 1 до 100 с учётом информацию о том, больше или меньше случайное число нужного нам числа.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0  # счётчик попыток
    # задаём начальное значение нижней границы для выбора чисел
    start_point=1
    # задаём начальное значение верхней границы для выбора чисел
    end_point=101

    while True:
        count += 1
        # угадываем предполагаемое число в интервале [start_point, end_point-1]
        predict_number = np.random.randint(start_point, end_point) 
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number>predict_number:
            # предполагаемое число оказалось меньше загаданного, снижаем нижнюю границу для выбора чисел на текущее predict_number+1
            start_point=predict_number+1
        else:
            # предполагаемое число оказалось больше загаданного, снижаем верхнюю границу для выбора чисел на текущее predict_number
            end_point=predict_number
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)