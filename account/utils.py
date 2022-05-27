from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    activation_url = f'http://127.0.0.1:5000/api/v1/account/activate/{activation_code}'
    message = f"""
    Thank you for signing up.
    Please, activate your account.
    Activation link: {activation_url}
    """
    send_mail(
        'Activate your account',
        message,
        'test@test.com',
        [email, ],
        fail_silently=False
    )
