import inspect

def introspection_info(obj):
    info = {}

# Тип объекта
    info['type'] = type(obj).__name__

# Атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes

# Методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

# Модуль, к которому объект принадлежит
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None

# Дополнительные свойства
    if isinstance(obj, (int, float)):
        info['value'] = obj

    return info


number_info = introspection_info(42)
print(number_info)
