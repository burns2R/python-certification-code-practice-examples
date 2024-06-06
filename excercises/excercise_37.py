def validate_user_age(age):
    try:
        if age < 0 or age > 120:
            raise ValueError("Invalid age, age should be between 0 and 120")
        else:
            return f'Valid age: age entered is {age}'
    except ValueError as error:
        return f'An error occured: {error}. Please try again.'
# Correct!! the error should be ValueError since there was an
# error with the value, plus it matches expected output.    
print(validate_user_age(130))
     