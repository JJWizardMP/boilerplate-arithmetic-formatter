'''
@File    :   arithmetic_arranger.py
@Time    :   2023/10/16 13:38:01
@Author  :   JJwizardMP
@Version :   1.0.2
@License :   GLP v.2
@Desc    :   Solution to FCC Python Project: Arithmetic Formatter
'''


def arithmetic_arranger(*problems):
  return arithForm(problems[0]).build_operation(len(problems) > 1)


class operFormat:

  def __init__(self, string):
    self.a, self.s, self.b = string.split()
    self.lmax = max(len(self.a), len(self.b))
    self.res = str(
        int(self.a) + int(self.b) if self.s == "+" else int(self.a) -
        int(self.b))


class arithForm:

  def __init__(self, problems):
    self.dict_err = {
        1: "Error: Too many problems.",
        2: "Error: Operator must be '+' or '-'.",
        3: "Error: Numbers must only contain digits.",
        4: "Error: Numbers cannot be more than four digits."
    }
    self.problems = problems.copy()

  def build_operation(self, flag=False):
    try:
      self.validate_problems()
      return self.create_output(flag)
    except ValueError as e:
      return str(e)

  def validate_problems(self):
    if len(self.problems) > 5:
      raise ValueError(self.dict_err[1])
    for problem in self.problems:
      A, S, B = problem.split()
      if S not in ("+", "-"):
        raise ValueError(self.dict_err[2])
      if not (A.isdecimal() and B.isdecimal()):
        raise ValueError(self.dict_err[3])
      if len(A) > 4 or len(B) > 4:
        raise ValueError(self.dict_err[4])

  def create_output(self, flag=False):
    list_format = [operFormat(problem) for problem in self.problems]
    m1 = [f'{obj.a:>{obj.lmax + 2}}' for obj in list_format]
    m2 = [f'{obj.s:<2}{obj.b:>{obj.lmax}}' for obj in list_format]
    dash = ['-' * (obj.lmax + 2) for obj in list_format]
    rs = [f'{obj.res:>{obj.lmax + 2}}' for obj in list_format] if flag else []
    arith_format = '\n'.join(map((' ' * 4).join, (m1, m2, dash, rs)))
    return arith_format.rstrip()
