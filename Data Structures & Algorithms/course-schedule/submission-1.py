class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [Outgoing:Incoming]
        adjList = {}
        for course in prerequisites:
            if course[0] not in adjList:
                adjList[course[0]] = [course[1]]
            else:
                adjList[course[0]].append(course[1])
        for rem in range(numCourses):
            if rem not in adjList:
                adjList[rem] = []
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if adjList[crs]==[]:
                return True
            visit.add(crs)
            for prereq in adjList[crs]:
                if not dfs(prereq):
                    return False
            visit.remove(crs)
            adjList[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        # print(adjList)

        return True