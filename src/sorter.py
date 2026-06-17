def sort_descending(arr):
    """
    Сортирует список по убыванию.
    Возвращает отсортированный список (не изменяет исходный)
    """
    if not isinstance(arr, list):
        raise TypeError("Ошибка: входное значение должно быть списком")
    
    if not arr:
        return []
    
    try:
        return sorted(arr, reverse=True)
    except TypeError:
        raise TypeError("Ошибка: все элементы списка должны быть одного типа и сравнимы")


def is_sorted_descending(arr):
    """
    Проверяет, отсортирован ли список по убыванию.
    Возвращает True, если список отсортирован по убыванию, иначе False
    """
    if not isinstance(arr, list):
        return False
    
    if len(arr) <= 1:
        return True
    
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            return False
    return True
