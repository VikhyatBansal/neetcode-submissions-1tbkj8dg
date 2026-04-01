class Solution:
    def isValid(self, s: str) -> bool:
        st = ['']
        for i in s:
            if i == "(" or i == '[' or i == "{":
                st.append(i)
            elif (i == ")" and st[-1] == "(") or (i == "]" and st[-1] == "[") or (i == "}" and st[-1] == "{"):
                st.pop()
            else:
                return False
        return len(st)==1