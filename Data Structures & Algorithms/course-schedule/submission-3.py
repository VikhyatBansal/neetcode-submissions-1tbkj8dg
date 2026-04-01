class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for i in prerequisites:
            if i[0] not in adjList:
                adjList[i[0]] = [i[1]]
            else:
                adjList[i[0]].append(i[1])
        for j in range(numCourses):
            if j not in adjList:
                adjList[j] = []

        visit = set()
        def dfs(pending):
            if pending in visit:
                return False
            if adjList[pending]==[]:
                return True
            visit.add(pending)
            for pre in adjList[pending]:
                if not dfs(pre):
                    return False
            visit.remove(pending)
            adjList[pending] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True