def stringify(data):
    # для простых типов данных возвращаем строковое представление
    if isinstance(data, str):
        return f'{data}'
    elif isinstance(data, bool):
        return str(data).lower()
    elif isinstance(data, (int, float)):
        return str(data)
    # для списка используем рекурсию
    elif isinstance(data, list):
        result = []
        for item in data:
            result.append(stringify(item))
        return "[" + ", ".join(result) + "]"
    # для словаря используем рекурсию
    elif isinstance(data, dict):
        result = []
        for key, value in data.items():
            result.append(f'{key}: {stringify(value)}')
        return "{" + ", ".join(result) + "}"
    # для остальных типов данных возвращаем пустую строку
    else:
        return ""

data = {
    "name": "John",
    "age": 30,
    "is_active": True,
    "pets": [
        "dog",
        "cat"
    ],
    "address": {
        "city": "New York",
        "state": "NY"
    }
}

print(stringify(data))