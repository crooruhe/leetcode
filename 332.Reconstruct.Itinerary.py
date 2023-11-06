class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        ticketList = tickets[:]
        ticketStack = []
        tempList = []
        tempLoc = []
        result = ['JFK']

        while (len(ticketList) > 0):
            print(ticketList)
            print('result: ', result)
            
            counter = 0
            if (len(ticketList) == 1):
                result.append(ticketList[0][1])
                break

            for ticket in ticketList:
                if ticket[0] == result[-1]:
                    tempList.append(ticket)

            if (len(tempList) > 1):
                tempList.sort()
                for item in tempList:
                    for ticket in ticketList:
                        if (item[1] == ticket[0]):
                            tempLoc.append(item[1])

                if (len(tempLoc) > 0):
                    ticketList.remove([result[-1], tempLoc[0]])
                    result.append(tempLoc[0])

            elif (len(tempList) == 1):
                result.append(tempList[0][1])
                ticketList.remove(tempList[0])

            else:
                if (len(ticketList) > 0 and len(tempList) == 0):



            print('templist ', tempList)
            print('-------------')

            tempList = []
            tempLoc = []
            tempSort = []
            # ticketStack.append(ticketList)

        print('final: ', result)
        return result

if __name__ == "__main__":
    # t = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    # y = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    # q = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    w = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
    x = Solution()
    # x.findItinerary(t)
    # x.findItinerary(y)
    # x.findItinerary(q)
    x.findItinerary(w)