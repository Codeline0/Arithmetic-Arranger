def arithmetic_arranger(lst_operations, output=False):
    available_operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    arranged = ''
    top_line = ''
    mid_line = ''
    dash_line = ''
    output_line = ''

    if len(lst_operations) > 5:
        return 'Error: Too many problems.'

    for operation in lst_operations:
        operator = operation.split()[1]
        digits = operation.split(operator)
        first_operand = digits[0].strip()
        second_operand = digits[1].strip()
        len_of_line = len(max(digits, key=len).strip()) + 2

        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        try:
            int(first_operand)
            int(second_operand)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        
        try:
            result = available_operators[operator](int(first_operand), int(second_operand))
        except KeyError:
            return 'Error: Operator must be \'+\' or \'-\'.'

        separator = ' ' * 4
        top_line += ' ' * (len_of_line - len(first_operand)) + first_operand + separator
        mid_line += operator + ' ' * (len_of_line - 1 - len(second_operand)) + second_operand + separator
        dash_line += '-'* len_of_line + separator
        output_line += ' ' * (len_of_line - len(str(result))) + str(result) + separator

    if output == True:
        all_lines = [top_line, mid_line, dash_line, output_line]    

        for lines in all_lines:  
            arr_func = lambda x: x.rstrip() + '\n'
            arranged += arr_func(lines)

    else:
        all_lines = [top_line, mid_line, dash_line]   
        
        for lines in all_lines:  
            arr_func = lambda x: x.rstrip() + '\n'
            arranged += arr_func(lines)

    return arranged
        