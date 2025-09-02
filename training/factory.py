def get_db_session():
    """Функция, которая создает сессию"""
    print("Создаю сессию...")
    return "🔵 Новая сессия БД"


# Вариант 1: НЕПРАВИЛЬНО - создаем сессию сразу в конструкторе
class BadUOW:
    def __init__(self):
        self._session = get_db_session()  # ❌ Сессия создалась СРАЗУ!
        # Даже если мы не будем использовать UOW!


# Вариант 2: ПРАВИЛЬНО - передаем фабрику
class GoodUOW:
    def __init__(self, session_factory):
        self._session_factory = session_factory  # ✅ Сохраняем РЕЦЕПТ
        self._session = None  # Сессии еще нет!

    def __enter__(self):
        self._session = self._session_factory()  # ✅ Создаем когда НУЖНО!
        return self