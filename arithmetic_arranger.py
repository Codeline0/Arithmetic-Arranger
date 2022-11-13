def arithmetic_arranger(lst_operations, output=False):
    arranged = ''

    if len(lst_operations) > 5:
        return print('Error: Too many problems.')

    for operation in lst_operations:
        if '+' in operation:
            digits = operation.split('+')
            for digit in digits:
                digit = digit.strip()
                if len(digit) > 4:
                    return print('Error: Numbers cannot be more than four digits.')
                try:
                    digit = int(digit)
                    # print(digit)
                except ValueError:
                    return print('Error: Numbers must only contain digits.')
            
        elif '-' in operation:
            digits = operation.split('-')
            for digit in digits:
                digit = digit.strip()
                if len(digit) > 4:
                    return print('Error: Numbers cannot be more than four digits.')
                try:
                    digit = int(digit)
                    # print(digit)
                except ValueError:
                    return print('Error: Numbers must only contain digits.')
        else:
            return print('Error: Operator must be \'+\' or \'-\'.')
            

arithmetic_arranger(['3 + 5', '223 - 5', '224 - 6233'])
arithmetic_arranger(['3 + 5', '223 - 5', '224 - 6', '3 + 5', '223 / 5', '224 - 6'])
    