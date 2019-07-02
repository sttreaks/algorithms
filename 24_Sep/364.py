def sequences(lst : list, k, n):
    """
    :param lst: підсписок перестановок
    :param k:   елемент для вставки
    :param n:   найбільший елемент послідовності
    :return:    None
    """
    if k > n:  # Якщо всі елементи вже вичерпано
        return

    # Вставляємо елемент k у всі можливі позиції списку
    # отриманого на попередніх ітераціях
    for pos in range(k):
        lst_next = lst[:]              # Копіюємо список
        lst_next.insert(pos, k)        # вставляємо елемент
        sequences(lst_next, k + 1, n)  # Запускаємо рекурсивно додавання наступного члена послідовності.

# Головна програма
if __name__ == "__main__":
    k = int(input())
    lst = []
    sequences(lst, 1, 12)
    print(lst)
    dict = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l'}
