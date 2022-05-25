def arithmetic_arranger(problems, result=False):
    row_0 = ''
    row_1 = ''
    row_2 = ''
    in_between = ''
    row_3 = ''

    arranged_problems = []
    for prob in problems:
      operands = find_operands(prob)
      length_prob = max_length(operands)
      
      row_0 += in_between + add_digits(operands[0], length_prob + 2)
      op = find_operator(prob)
      row_1 += in_between + op + " " +  add_digits(operands[1], length_prob)
      
      row_2 += in_between + add_dashes(length_prob + 2)
      if (result):
        row_3 += in_between + add_digits(str(calc(operands, op)), length_prob + 2)
      in_between = ' ' * 4

      arranged_problems = [row_0, row_1, row_2, row_3]

    print_grid(arranged_problems) 

    return arranged_problems

def calc(operands, op):
  if (op == '+'):
    return int(operands[0]) + int(operands[1])
  return int(operands[0]) - int(operands[1])



def check_operator(problem, operator):
    if problem.find(operator) == -1:
        return False
    return True

def add_digits(operand, length):
  spaces = length - len(operand)
  return ' ' * spaces + operand
  

def add_dashes(length):
  return '-' * length
    

def max_length(operands):
    return max([len(operand) for operand in operands])

def find_operands(problem):
    if check_operator(problem, '+'):
        op = '+'
    elif check_operator(problem, '-'):
        op = '-'

    delimiter = " {} ".format(op)
    operands = problem.split(delimiter)
    return operands

def find_operator(problem):
  if check_operator(problem, '+'):
        return '+'
  elif check_operator(problem, '-'):
      return '-'

def print_grid(arranged_problems):
  for row in arranged_problems:
    print(row)

# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

# arithmetic_arranger(["32 + 698"], True)

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)