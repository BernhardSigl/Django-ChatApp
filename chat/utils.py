from django.contrib.auth.models import User

def check_username_exists(username, context):
    """
    Checks if a username exists. If it does, updates the context accordingly.

    Args:
        username (str): The username to check.
        context (dict): The context to update.

    Returns:
        bool: True if the username already exists, False otherwise.
    """
    if User.objects.filter(username=username).exists():
        has_error = True
        context["usernameExists"] = True
    else:
        has_error = False
    context['username'] = username
    return has_error

def check_email_exists(email, context):
    """
    Checks if an email address already exists. If it does, updates the context accordingly.

    Args:
        email (str): The email address to check.
        context (dict): The context to update.

    Returns:
        bool: True if the email already exists, False otherwise.
    """
    if User.objects.filter(email=email).exists():
        has_error = True
        context["emailExists"] = True
    else:
        has_error = False
    context['email'] = email
    return has_error

def check_password_match(password, repeat_password, context):
    """
    Checks if the password matches its repeat value. If they don't match, updates the context and indicates an error.

    Args:
        password (str): The password.
        repeat_password (str): The repeated password.
        context (dict): The context to update.

    Returns:
        bool: True if the passwords don't match, False otherwise.
    """
    if password != repeat_password:
        context["wrongRepeatPassword"] = True
        has_error = True
    else:
        has_error = False
    
    return has_error