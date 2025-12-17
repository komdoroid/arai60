class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []

        for ch in s:
            if ch is '(' or ch is '{' or ch is '[':
                stack_list.append(ch)
            elif not stack_list:
                return False
            elif ch is ')':
                bracket = stack_list.pop()
                if bracket != '(':
                    return False
            elif ch is '}':
                bracket = stack_list.pop()
                if bracket != '{':
                    return False
            elif ch is ']':
                bracket = stack_list.pop()
                if bracket != '[':
                    return False
        
        if len(stack_list) != 0:
            return False
        return True
