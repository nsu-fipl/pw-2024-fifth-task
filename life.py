def dead():
    return '.'


def alive():
    return 'o'


def show_field(field):
    for row in field:
        for cell in row:
            print(cell, end='')
        print()


def alive_neighbours(field, i, j):
    assert len(field) != 0 and len(field[0]) != 0
    assert 0 <= i < len(field)
    assert 0 <= j < len(field[0])
    shifts = [-1, 0, 1]
    ns = []
    n_alive = 0
    for s1 in shifts:
        ni = i + s1
        if ni < 0 or ni >= len(field):
            continue
        for s2 in shifts:
            nj = j + s2
            if nj < 0 or nj >= len(field[0]):
                continue
            is_dead = field[ni][nj] == dead()
            if not is_dead:
                n_alive += 1
    return n_alive


def next_gen(field):
    assert len(field) != 0 and len(field[0]) != 0
    new_field = []
    for i in range(len(field)):
        new_field.append([dead()] * len(field[i]))
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            n_alive = alive_neighbours(field, i, j)
            is_dead = cell == dead()
            if is_dead:
                if n_alive == 3:
                    new_field[i][j] = alive()
            elif n_alive != 2 and n_alive != 3:
                new_field[i][j] = dead()
    return new_field


def life(field):
    if not field:
        print('Field should contain at least one row and column!')
        return
    while True:
        show_field(field)
        input()
        field = next_gen(field)


if __name__ == '__main__':
    life([['o', 'o', '.', '.', 'o'],
          ['o', 'o', '.', '.', 'o'],
          ['o', 'o', '.', '.', 'o'],
          ['o', 'o', '.', '.', 'o']])
