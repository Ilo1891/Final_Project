from django.conf import settings


def save_feedback(name, phone, message):
    with open(
            settings.FEEDBACK_FILE_PATH, 'wt', encoding='utf-8'
    ) as f:
        f.write(f'Ваше сообщение: {name}, {phone}, {message}')