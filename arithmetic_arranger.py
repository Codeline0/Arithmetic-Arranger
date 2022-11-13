
def arithmetic_arranger(lst_operations, output=False):
    arranged = ''

    if len(lst_operations) > 5:
        return print('Error: Too many problems.')

    operators = list(map(lambda x: x.split()[1], lst_operations))

    if set(operators) != {'-', '+'}:
        return print('Error: Operator must be \'+\' or \'-\'.')

    for operation in lst_operations:
        operator = operation.split()[1]
        digits = operation.split(operator)
        # print(digits)
        for digit in digits:
            digit = digit.strip()
            if len(digit) > 4:
                return print('Error: Numbers cannot be more than four digits.')
            try:
                digit = int(digit)
                # print(digit)
            except ValueError:
                return print('Error: Numbers must only contain digits.')
            

arithmetic_arranger(['3 + 5', '223 - 5', '224 - 6233'])
arithmetic_arranger(['3 + 5', '223 - 5', '224 - 6', '3 + 5', '223 / 5', '224 - 6'])
    