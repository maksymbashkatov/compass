# def direction(facing, turn):
#     directions = {'N': 0, 'NE': 45, 'E': 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315}
#     # К стартовой точке прибавить шаг в градусах, тем самым получить финальные градусы.
#     final_degrees = directions[facing] + turn
#
#     # Количество оборотов от нулевого градуса.
#     turns_amount = final_degrees // 360
#
#     # Поскольку 1 оборот = 360, то отнять от финальной точки столько градусов сколько оборотов.
#     return (k for k, v in directions.items() if v == final_degrees - (360 * turns_amount)).__next__()
def direction(facing, turn):
    if turn % 45 != 0:
        raise ValueError(f'{turn} не делится на 45')
    elif not (-1080 < turn < 1081):
        raise ValueError(f'{turn} выходит за пределы от -1080 до 1080')

    directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    start_index = directions.index(facing)

    # Поскольку 1 шаг на компасе равен 45, чтобы выяснить сколько шагов было сделано от начальной точки,
    # нужно поворот в градусах разделить на 45.
    step_from_start_index = turn // 45

    # Чтобы выяснить конечный индекс, нужно к статовому прибавить количество шагов.
    final_index = (start_index + step_from_start_index) % 8
    return directions[final_index]


# tests
print(direction('S', 180))  # N
print(direction('SE', -45))  # E
print(direction('W', 495))  # NE
print(direction('N', -675))  #
# print(direction('N', -4500))
# print(direction('N', 46))
