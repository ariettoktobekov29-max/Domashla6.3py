from datetime import date
from rest_framework.serializers import ValidationError


def validate_user_age_from_token(request):



    token_payload = getattr(request, 'auth', None)
    
    birthdate_str = None
    if isinstance(token_payload, dict):
        birthdate_str = token_payload.get('birthdate')
    elif hasattr(token_payload, 'payload'):
        birthdate_str = token_payload.payload.get('birthdate')


        if not birthdate_str:
            raise ValidationError("Укажите дату рождения, чтобы создать продукт.")
    
    try:
        birthdate = date.fromisoformat(birthdate_str)
    except (ValueError, TypeError):
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")



    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")