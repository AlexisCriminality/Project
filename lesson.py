print('Задача 6. Маятник ')


# Известно, что амплитуда качающегося маятника с каждым разом затухает
# на 8,4% от амплитуды прошлого колебания.
# Если качнуть маятник,
# то, строго говоря, он не остановится никогда,
# просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Напишите программу,
# определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход
# начальную амплитуду колебания в сантиметрах
# и конечную амплитуду его колебаний,
# которая считается остановкой маятника.

# Обеспечьте контроль ввода.

# Пример:

# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1

# Маятник считается остановившимся через 27 колебаний
def pendulum_stop(ampl_start, ampl_finish):
    count = 0
    while ampl_start > ampl_finish:
        count += 1
        ampl_start -= ampl_start * 0.084
    return count


ampl_start = float(input('Введите начальную амплитуду: '))
ampl_finish = float(input('Введите амплитуду остановки: '))

frequency = pendulum_stop(ampl_start, ampl_finish)
print(f'Маятник считается остановившимся через {frequency} колебаний')