class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in: # if the attribute of User is True
            func(args[0])
        else:
            print("Please log in first.")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post!")

new_user = User("Zamir")
# new_user.is_logged_in = True
create_blog_post(new_user)