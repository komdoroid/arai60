class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = deque('0')
        open_to_close = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
            '0' : ''
        }

        for ch in s:
            if ch in open_to_close:
                open_brackets.append(ch)
            else:
                if open_to_close[open_brackets.pop()] != ch:
                    return False
        
        if len(open_brackets) != 1:
            return False
