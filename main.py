first_lvl = int(input('Начальный уровень: '))
last_lvl = int(input('Требуемый уровень: '))


def count_lvl_before_12(lvl):
    return 0.0068 * lvl ** 3 - 0.06 * lvl ** 2 + 17.1 * lvl + 639


def count_lvl_after_12(ass):
    return 0.02 * ass ** 3 + 3.06 * ass ** 2 + 105.6 * ass - 895


def is_lvl(lvl):
    if lvl < 0 or lvl > 1000:
        print("Уровень должен быть меньше 0 и больше 1000")
        exit(1)


is_lvl(first_lvl)
is_lvl(last_lvl)

_sum = 0

for i in range(first_lvl + 1, last_lvl + 1):
    if i < 12:
        _sum += (round(count_lvl_before_12(i)))
    else:
        _sum += (round(count_lvl_after_12(i)))

print(_sum)

