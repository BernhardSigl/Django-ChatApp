from django.contrib.auth.models import User

def check_username_exists(username, context):
    """
    Überprüft, ob ein Benutzername existiert. Wenn ja, wird der Kontext entsprechend angepasst.

    Args:
        username (str): Der zu überprüfende Benutzername.
        context (dict): Der Kontext, der angepasst wird.

    Returns:
        bool: Gibt an, ob der Benutzername bereits existiert.
    """
    if User.objects.filter(username=username).exists():
        context["usernameExists"] = True
        context['username'] = username
        has_error = True
    else:
        has_error = False
    
    return has_error

def check_email_exists(email, context):
    """
    Überprüft, ob eine E-Mail-Adresse bereits existiert. Passt den Kontext entsprechend an.

    Args:
        email (str): Die zu überprüfende E-Mail-Adresse.
        context (dict): Der Kontext, der angepasst wird.

    Returns:
        bool: Gibt an, ob die E-Mail-Adresse bereits existiert.
    """
    if User.objects.filter(email=email).exists():
        context["emailExists"] = True
        context['email'] = email
        has_error = True
    else:
        has_error = False
    
    return has_error

def check_password_match(password, repeat_password, context):
    """
    Überprüft, ob das Passwort und das wiederholte Passwort übereinstimmen.
    Wenn nicht, passt es den Kontext an und gibt an, ob ein Fehler vorliegt.

    Args:
        password (str): Das Passwort.
        repeat_password (str): Das wiederholte Passwort.
        context (dict): Der Kontext, der angepasst wird.

    Returns:
        bool: Gibt an, ob das Passwort nicht übereinstimmt.
    """
    if password != repeat_password:
        context["wrongRepeatPassword"] = True
        has_error = True
    else:
        has_error = False
    
    return has_error