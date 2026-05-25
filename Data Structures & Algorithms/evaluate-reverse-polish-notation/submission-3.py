class Solution:
    def isNum(self, x):
        try:
            int(x)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        for s in tokens:
            print(lst)
            if(self.isNum(s)):
                lst.append(int(s))
            elif(s == "+"):
                lst.append(lst.pop() + lst.pop())
            elif(s == "*"):
                lst.append(lst.pop() * lst.pop())
            elif(s == "-"):
                second_param = lst.pop()
                lst.append(lst.pop() - second_param)
            elif(s == "/"):
                second_param = lst.pop()
                lst.append(int(lst.pop() / second_param))

        return lst[-1]