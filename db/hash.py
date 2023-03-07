from passlib.context import CryptContext

password_txt = CryptContext(schemes="bcrypt", deprecated="auto")


def bcrypt(password: str):
    return password_txt.hash(password)
