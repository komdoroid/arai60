class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = deque()
        open_to_close = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for ch in s:
            if ch in open_to_close:
                open_brackets.append(ch)
            
            elif ch in open_to_close.values():
                if not open_brackets or open_to_close[open_brackets.pop()] != ch:
                    return False
        
        if len(open_brackets) != 0:
            return False
        return True
