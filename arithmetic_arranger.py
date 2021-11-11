def arithmetic_arranger(*problems):
  OF = arithForm(problems[0])
  flag = True if (len(problems)>1) else False
  arranged_problems = OF.build_operation(flag)
  return arranged_problems

class operFormat:
    def __init__ (self, string):
        self.a, self.s, self.b = string.split()
        self.lmax = max(len(self.a), len(self.b))
        self.res = str(int(self.a) + int(self.b)) if self.s == "+" else str(int(self.a) - int(self.b))

class arithForm:
    def __init__(self, problems):
        self.dict = {
            1: "Error: Too many problems.",
            2: "Error: Operator must be '+' or '-'.",
            3: "Error: Numbers must only contain digits.",
            4: "Error: Numbers cannot be more than four digits."
        }
        self.problems = problems
        self.lsformt = []
    
    def build_operation(self, flag=False):
        err = self.test_errors()
        return self.dict[err] if(err) else self.create_output(flag)

    def test_errors(self):
        if (len(self.problems) > 5):
            return 1
        for problm in self.problems:
            A, S, B = problm.split()
            if (not (S == "+" or S == "-")):
                return 2
            elif (not (A.isdecimal() and B.isdecimal())):
                return 3
            elif (len(A) > 4 or len(B) > 4):
                return 4
            else:
                pass
        return 0

    def create_output(self, flag=False):
        m1, m2, rs, dash = ("", "", "", "")
        self.lsformt = [ operFormat(probl) for probl in self.problems ]
        for obj in self.lsformt:
            m1 += " "*(2 + (obj.lmax - len(obj.a))) + obj.a + " "*4
            m2 += obj.s + " "*(1 + (obj.lmax - len(obj.b))) + obj.b + " "*4
            dash += "-"*2 + "-"*obj.lmax + " "*4
            if (flag):
                rs += " "*(2+(obj.lmax - len(obj.res))) + obj.res + " "*4
        m1 = m1.rstrip().replace("-", " ")
        m2 = m2.rstrip()
        dash = dash.rstrip()
        if (flag):
            rs = "\n" + rs.rstrip()
        return m1 + "\n" + m2 + "\n" + dash + rs