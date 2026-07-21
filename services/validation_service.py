import re


class ValidationService:
    EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    @staticmethod
    def validate_username(username: str) -> bool:
        return bool(username and 3 <= len(username.strip()) <= 80)

    @staticmethod
    def validate_email(email: str) -> bool:
        return bool(re.match(ValidationService.EMAIL_PATTERN, email or ""))

    @staticmethod
    def validate_password(password: str) -> bool:
        if not password or len(password) < 8:
            return False

        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)

        return has_upper and has_lower and has_digit