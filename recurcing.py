from copy import deepcopy

def fact(n):
    while n > 1:
        return n * fact(n-1)
    return 1


def fill_list(spisok, turn) -> list:
    symbol = 'X' if turn else '0'
    if len(spisok) > 1:
        free_cells = get_free_cells(spisok)

        for i in free_cells:
            tmp_spisok = deepcopy(spisok)
            tmp_spisok.pop(i)
            tmp_lst = []
            tmp_lst = fill_list(tmp_spisok, not turn)
            tmp_lst.insert(i, symbol)
            if len(tmp_lst) == len(lst):
                print(tmp_lst)
        return tmp_lst

    return [symbol]


def get_free_cells(lst):
    cells = []
    for i in range(len(lst)):
        if lst[i] == ' ':
            cells.append(i)
    return cells


lst = [' ', ' ', ' ', ' ']

print(fill_list(deepcopy(lst), True))
