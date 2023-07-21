class OzonExceptions(Exception):
    """Исключения в URL Озона"""

    @staticmethod
    def request_error_message(exception):
        """Ошибка при обращении к API Озона"""
        return f"Ошибка при обращении к API Озона: {exception}"

    @staticmethod
    def json_processing_error_message(exception):
        """Ошибка при обработке JSON-ответа"""
        return f"Ошибка при обработке JSON-ответа: {exception}"

    @staticmethod
    def authorization_error_message():
        """Ошибка авторизации."""
        return "Ошибка авторизации в API Озона"
