from passlib.context import CryptContext

password_context = CryptContext(schemes="bcrypt", deprecated="auto")


def bcrypt(password: str):
    return password_context.hash(password)


def verify(hashed_password, given_password: str):
    return password_context.verify(given_password, hashed_password)
