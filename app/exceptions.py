class AppException(Exception):
    """Base exception for all business logic errors"""
    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code
        super().__init__(message)

class UserNotFound(AppException):
    """Raised when a user is not found"""
    def __init__(self, username: str):
        super().__init__(f"User {username} not found", code=404)

class UserAlreadyExists(AppException):
    """Raised when a user already exists"""
    def __init__(self, username: str):
        super().__init__(f"User {username} already exists", code=409)