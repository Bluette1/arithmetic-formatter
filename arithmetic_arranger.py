def arithmetic_arranger(problems):
    num_probs = len(problems)
    rows = 4
    cols = 0
    for prob in problems:
        operands = find_operands(prob)
        length_prob = max_length(operands)
        cols += length_prob
    num_spaces = num_probs - 1
    cols += 4 * num_spaces

    formatting_grid = [rows][cols]

    end = 0

    for prob in problems:
      length_prob = max_length(operands)
      start = end + length_prob
      operands = find_operands(prob)
      add_digits(operands[0], start, 0, formatting_grid)
      op = find_operator(prob)
      formatting_grid[end][1] = op
      add_digits(operands[1], start, 1, formatting_grid)
      add_dashes(formatting_grid, start + end, start)
      end = start + 5

    print_grid(formatting_grid)

    return formatting_grid

def check_operator(problem, operator):
    if problem.find(operator) == -1:
        return False
    return True

def add_digits(operand, start, row, formatting_grid):
  i = start
  for digit in operand:
    formatting_grid[row][i] = digit
    i -= 1

def add_dashes(formatting_grid, start, end):
  i = start
  for i in range(start, end):
    formatting_grid[2][i] = '-'
    i -= 1

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

def print_grid(formatting_grid):
  for row in formatting_grid:
    print ("{}\n", row.join())