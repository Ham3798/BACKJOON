
def convert_to_decimal(number, base):
    result, multiplier = 0, 1

    for i in number[::-1]:
        result += multiplier * int(i)
        multiplier *= base
    
    return result

def convert_from_decimal(number, base):
    result = ""

    while True:
        result += str(number%base)
        number = int(number/base)

        if number == 0:
            break
    
    return result[::-1]

num, base = map(int, input().split(' '))
print(convert_from_decimal(num, base))
