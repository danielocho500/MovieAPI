import re
import bcrypt

def has_uppercase_letter(password: str) -> bool:
    return bool(re.search(r'[A-Z]', password))

def has_symbol(password: str) -> bool:
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def has_number(password: str) -> bool:
    return bool(re.search(r'\d', password))

def is_secure_psd(password: str) -> bool:
    return (has_uppercase_letter(password) and
            has_symbol(password) and
            has_number(password))

def hash_password(ps: str) -> str:
    ps_bytes = ps.encode('utf-8')
    hashed_bytes = bcrypt.hashpw(ps_bytes, bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')

def check_password(ps: str, expected:str) -> bool:
    ps_bytes = ps.encode('utf-8')
    expected_bytes = expected.encode('utf-8')
    return bcrypt.checkpw(ps_bytes, expected_bytes)
    