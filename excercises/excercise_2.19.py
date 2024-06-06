from datetime import datetime

datetime_str = '28/04/15 04:54:14'

converted_datetime = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')

print('The type of the date is now', type(converted_datetime))
print('The date is', converted_datetime)