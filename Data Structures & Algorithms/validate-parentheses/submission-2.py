class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack and (i==']' or i==')' or i=='}'):
                return False
            elif (i==')' and stack[-1]=='(') or (i==']' and stack[-1]=='[') or (i=='}' and stack[-1]=='{'):
                stack.pop()
            elif (i==')' and stack[-1]!='(') or (i==']' and stack[-1]!='[') or (i=='}' and stack[-1]!='{'):
                return False
            else:
                stack.append(i)
        # print(stack)
        return len(stack)==0