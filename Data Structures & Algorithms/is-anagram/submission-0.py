class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        for i in s:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
        for j in t:
            if j in store and store[j]>0:
                store[j]-=1
            else:
                return False
        if sum(store.values())==0:
            return True
        return False