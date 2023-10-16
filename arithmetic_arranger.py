'''
@File    :   arithmetic_arranger.py
@Time    :   2023/10/16 13:38:01
@Author  :   JJwizardMP
@Version :   1.0.2
@License :   GLP v.2
@Desc    :   Solution to FCC Python Project: Arithmetic Formatter
'''


def arithmetic_arranger(*problems):
  OF = arithForm(problems[0])
  flag = len(problems) > 1
  arranged_problems = OF.build_operation(flag)
  return arranged_problems


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
    self.list_format = []

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
    m1, m2, dash, rs, sep = ("", "", "", "\n", " " * 4)
    self.list_format = [operFormat(problem) for problem in self.problems]
    for obj in self.list_format:
      m1 += f'{obj.a:>{obj.lmax + 2}}{sep}'
      m2 += f'{obj.s:<2}{obj.b:>{obj.lmax}}{sep}'
      dash += f"{'-' * (obj.lmax + 2)}{sep}"
      if (flag):
        rs += f'{obj.res:>{obj.lmax + 2}}{sep}'
    # Elimnate white spaces to right side
    m1, m2, dash, rs = [s.rstrip() for s in (m1, m2, dash, rs)]
    arith_format = f"{m1}\n{m2}\n{dash}{rs}"
    return arith_format
