import secrets
import hashlib


class CapabilityService:
    @staticmethod
    def generate_code() -> str:
        return secrets.token_urlsafe(24)

    @staticmethod
    def hash_code(code: str) -> str:
        return hashlib.sha256(code.encode()).hexdigest()

    @staticmethod
    def verify_code(code: str, stored_hash: str) -> bool:
        return CapabilityService.hash_code(code) == stored_hash