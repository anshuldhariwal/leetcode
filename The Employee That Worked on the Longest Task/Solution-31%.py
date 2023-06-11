class Solution(object):
    def hardestWorker(self, n, logs):
        longest_pair = [0,0]
        for i in range(0,len(logs)):
            
            if i == 0:
                longest_pair = logs[0]
            elif logs[i][1] - logs[i-1][1] > longest_pair[1]:
                longest_pair[0] = logs[i][0]
                longest_pair[1] = logs[i][1] - logs[i-1][1]
            elif logs[i][1] - logs[i-1][1] == longest_pair[1] and logs[i][0] < longest_pair[0]:
                longest_pair[0] = logs[i][0]

        return longest_pair[0]
