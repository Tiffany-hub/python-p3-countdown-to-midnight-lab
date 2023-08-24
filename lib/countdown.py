import time

def countdown(number):
    output = ""
    while number > 0:
        output += f'{number} SECOND(S)!\n'
        number -= 1
    output += 'HAPPY NEW YEAR!'
    return output

def countdown_with_sleep(number):
    output = ""
    while number > 0:
        output += f'{number} SECOND(S)!\n'
        time.sleep(1)
        number -= 1
    output += 'HAPPY NEW YEAR!'
    return output

print(countdown(5))
print(countdown_with_sleep(5))
