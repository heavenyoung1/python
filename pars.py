from typing import Optional

class SessionEngine:
    '''Класс для управления сессией браузера с поддержкой кук и заголовков'''
    def __init__(
            self,
            headless: bool = False,
            user_agent: Optional[str] = None,
            proxy: Optional[str] = None,
    ):
        self.headless = headless
        self.user_agen = user_agent,
        self.proxy = proxy,

