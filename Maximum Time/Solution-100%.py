class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        t = []
        for i in range(len(time)):
            t.append(time[i])
            if time[i] == "?":
                if i == 0:
                    if time[i+1] == "?":
                        t[i] = "2"
                    elif int(time[i+1]) <= 3:
                        t[i] = "2"
                    else:
                        t[i] = "1"
                elif t[i - 1] == "2" and i - 1 == 0:
                    t[i] = "3"
                elif time[i-1] == ":":
                    t[i] = "5"
                else:
                    t[i] = "9"

        return ''.join(t)
