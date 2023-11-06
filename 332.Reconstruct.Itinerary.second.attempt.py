class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        result = ['JFK']
        total = len(tickets) + 1
        visited = []
        path = []
        curr = result
        locs = {}
        rotate_list = {}
        templocs = locs
        keys = set()
        values = set()
        dest = ''

        for l in tickets:
            keys.add(l[0])
            values.add(l[1])
            if l[0] not in locs:
                locs[l[0]] = []
            locs[l[0]].append(l[1])
            locs[l[0]] = sorted(locs[l[0]])

        dest = list(values - keys)
        if dest:
            dest = dest[0]
        
        for key in keys:
            rotate_list[key] = len(templocs[key])



        while len(curr) < total:
            if templocs[curr[-1]] and templocs[curr[-1]][0] != dest:
                if len(templocs[curr[-1]]) > 1:
                    path.append([curr[-1], 0])
                curr.append(templocs[curr[-1]][0])
                templocs[curr[-1]].remove(templocs[curr[-1]][0])

            else:
                templocs = locs
                if not path:
                    path.append(['JFK', 0])
                for idx in range(len(curr) - 1, -1, -1):
                    if curr[idx] == path[-1][0]:
                        curr = curr[:idx + 1]
                        path = path[:-1]



        # print(len(curr))
        # print('-----------')
        return result

if __name__ == "__main__":
    x = Solution()
    
    t = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    # y = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    # q = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    w = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
    
    x.findItinerary(t)
    # x.findItinerary(y)
    # x.findItinerary(q)
    x.findItinerary(w)