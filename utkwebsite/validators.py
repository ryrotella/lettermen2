from django.core.exceptions import ValidationError

def validate_name(value):
    if len(value) < 3:
        raise ValidationError("Woopsie! You forgot your legal name there, bucko!! Give it another go there, pal.")
    elif len(value) > 20:
        raise ValidationError("Whoa! Easy on the name there, pal. Shorten it up and try again.")
    else:
        return value

def validate_email(value):
    if not '@' in value:
        raise ValidationError("Hey, sport! Throw an '@' in there. Come on now...")
    if not '.' in value:
        raise ValidationError("Hey, mack! Throw an '.' in there. Come on now...")
    else:
        return value

def validate_dates(value):
    if not value:
        raise ValidationError("Hey, bucko! You forgot to pick a date! Or 2! Or 3! Get Greedy!")
    else:
        return value

def validate_brand(value):
    brandList = list(value.split(" "))
    if len(brandList) > 5:
        raise ValidationError("Hey! That's more than 5 words! Cut it out!")
    else:
        return value