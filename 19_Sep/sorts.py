import time
import random


def benchmark(f):
    def _benchmark(*args, **kw):
        t = time.clock()
        rez = f(*args, **kw)
        t = time.clock() - t
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez
    return _benchmark


@benchmark
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
        if i % 2 == 0:
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    bl = False
        if i % 2 == 1:
            for j in range(n - i, 0, -1):
                if a[j] < a[j - 1]:
                    a[j], a[j - 1] = a[j - 1], a[j]
                    bl = False
        if bl:
            print(a)
            break
        i += 1


@benchmark
def bubble_sort(array):
    """ Реалізує алгоритм сортування "Бульбашкою"

    :param a: Масив (список однотипових елементів)
    :return: None
    """
    a = array
    n = len(a)
    for pass_num in range(n - 1, 0, -1):
        for i in range(pass_num):
            # Якщо наступний елемент менший за попередній
            if a[i] > a[i + 1]:
                # Міняємо місцями елементи, тобто
                # виштовхуємо більший елемент нагору
                a[i], a[i + 1] = a[i + 1], a[i]


@benchmark
def selection_sort(array):
    """ Реалізує алгоритм сортування вибором

    :param a: Масив (список однотипових елементів)
    :return: None
    """
    a = array
    n = len(a)
    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if a[maxpos] < a[j]:
                maxpos = j

        a[i], a[maxpos] = a[maxpos], a[i]


@benchmark
def insertion_sort(array):
    """ Реалізує алгоритм сортування вставкою

    :param a: Масив (список однотипових елементів)
    :return: None
    """
    a = array
    n = len(a)
    for index in range(1, n):
        currentValue = a[index]
        position = index

        # пошук позиції для вставки поточного елемента
        while position > 0:
            if a[position - 1] > currentValue:
                # зсув елементу масиву вправо
                a[position] = a[position - 1]
            else:
                # знайдено позицію
                break
            position -= 1

        # Вставка поточного елемента у знайдену позицію
        a[position] = currentValue


@benchmark
def merge(array):
    merge_sort(array)


def merge_sort(array):
    """ Реалізує алгоритм сортування злиттям

    :param a: Масив (список однотипових елементів)
    :return: None
    """
    a = array
    if len(a) > 1:
        # Розбиття списку навпіл
        mid = len(a) // 2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        # Рекурсивний виклик сортування
        # для кожної з половин
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # Злиття двох відсортованих списків
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a[k] = lefthalf[i]
                i += 1
            else:
                a[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            a[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            a[k] = righthalf[j]
            j += 1
            k += 1


@benchmark
def quick_sort(array):
    """ Реалізує алгоритм швидкого сортування

    :param a: Масив (список однотипових елементів)
    :return: None
    """
    a = array
    quick_sort_helper(a, 0, len(a) - 1)


def quick_sort_helper(array, first, last):
    """ Допоміжний рекурсивний метод,
        що реалізує сортування фрагменту списку обмеженого заданими позиціями

    :param array: Масив (список однотипових елементів)
    :param first: Ліва межа списку
    :param last: Права межа списку
    :return: None
    """
    if first < last:
        # Визанчення точки розбиття спику
        splitpoint = partition(array, first, last)
        # Рекурсивний виклик функції швидкого сортування
        # для отриманих частин списку
        quick_sort_helper(array, first, splitpoint - 1)
        quick_sort_helper(array, splitpoint + 1, last)


def partition(array, first, last):
    """ Визначає точку розбиття списку

    :param array: Масив (список однотипових елементів)
    :param first: Ліва межа списку
    :param last: Права межа списку
    :return: Позицію розбиття списку
    """
    pivot = array[first]
    left = first + 1
    right = last
    done = False
    while not done:
        # Рухаємося зліва на право,
        # поки не знайдемо елемент, що більший за опорний
        while left <= right and array[left] <= pivot:
            left += 1

        # Рухаємося справа на ліво,
        # поки не знайдемо елемент, що менший за опорний
        while array[right] >= pivot and right >= left:
            right -= 1

        # Якщо індекс правого елемента менший за індекс лівого
        if right < left:
            # то розбиття списку завершено
            done = True
        else:
            # міняємо знайдений елементи місцями
            array[left], array[right] = array[right], array[left]

    # ставимо опорний елемент на його позицію
    array[first], array[right] = array[right], array[first]
    return right


if __name__ == "__main__":
    a = [random.randrange(1000) for i in range(10000)]
    print(a)
    bubble_sort(a)
    bubble_sort_mod(a)
    selection_sort(a)
    insertion_sort(a)
    merge(a)
    print(a)
