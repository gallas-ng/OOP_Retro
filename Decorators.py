import functools

user = {"username" : "John", "access_level" : "guest"}

def make_secure(func):
    @functools.wraps(func) # To keep the name n description of the decorated function
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return "Access denied"

    return secure_function

@make_secure
def  get_admin_password():
    return "1234"

print(get_admin_password())

# ---------------- Decorators with parameters
def make_secure_bis(access_level):
    def decorator(func):
        @functools.wraps(func)  # To keep the name n description of the decorated function
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return "Access denied"

        return secure_function

    return decorator

@make_secure_bis("admin")
def get_admin_password():
    return "1234"

@make_secure_bis("user")
def get_user_password():
    return "1230"