from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        paths = defaultdict(list)

        for s, d in relations:
            paths[s].append(d)

        mtime = {}
        def dfs(course):
            if course in mtime:
                return mtime[course]

            result = time[course - 1]
            for n in paths[course]:
                result = max(result, time[course - 1] + dfs(n))
                print('course: ', course, ' neighbors: ', n, ' time: ', result)
            mtime[course] = result
            return result

        for i in range(1, n + 1):
            dfs(i)
        
        # print(max(mtime.values()))
        return max(mtime.values())

if __name__ == "__main__":
    x = Solution()
    """ n = 5
    relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
    time = [1,2,3,4,5] """
    
    n = 9
    relations = [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]]
    time = [9,5,9,5,8,7,7,8,4]
        
    x.minimumTime(n, relations, time)        