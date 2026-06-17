def convert_to_int(s):
    """
    Конвертирует строку в целое число.
    Возвращает кортеж (успех, значение, сообщение)
    """
    if not isinstance(s, str):
        return (False, None, "Ошибка: входное значение должно быть строкой")
    
    if not s:
        return (False, None, "Ошибка: пустая строка")
    
    # Удаляем пробелы в начале и конце
    s = s.strip()
    
    if not s:
        return (False, None, "Ошибка: строка состоит только из пробелов")
    
    # Проверяем наличие знака
    sign = 1
    start_idx = 0
    if s[0] == '-':
        sign = -1
        start_idx = 1
    elif s[0] == '+':
        start_idx = 1
    
    # Проверяем, что после знака есть цифры
    if start_idx >= len(s):
        return (False, None, "Ошибка: после знака отсутствуют цифры")
    
    # Проверяем, что все символы являются цифрами
    for ch in s[start_idx:]:
        if not ch.isdigit():
            return (False, None, f"Ошибка: недопустимый символ '{ch}'")
    
    # Преобразуем в число
    try:
        result = int(s)
        return (True, result, "Успешно")
    except ValueError:
        return (False, None, "Ошибка: число вне допустимого диапазона")
