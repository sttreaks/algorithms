def bubble_sort_mod(array):
    """ Реалізує алгоритм сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    a = array
    n = len(a)
    i = 0
    while i < n:
        bl = True
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                bl = False
        if bl:
            break
        i += 1