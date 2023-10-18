class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        h = 0
        for i in range(1,len(citations)+1):
            count = 0
            flag = 0
            for j in range(len(citations)):
                if i <= citations[j] and i<= len(citations)-j+count:
                    count+=1
                    h = i
                if count == i:
                    flag = 1
                    break
            if flag == 0: break
        return h
        
