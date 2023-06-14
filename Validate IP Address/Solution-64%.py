class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """

        if "." in queryIP:
            ipList = queryIP.split(".")
            if len(ipList) != 4:
                return "Neither"
            else:
                for digit in ipList:
                    if not digit.isdigit() or  (int(digit) < 0 or int(digit) >255) or (len(digit) > 1 and digit[0] == "0"):
                        return "Neither"
                return "IPv4"
        elif ":" in queryIP:
            ipList = queryIP.split(":")
            if len(ipList) != 8:
                return "Neither"
            else:
                for hex in ipList:
                    if len(hex) > 4 or len(hex) < 1:
                        return "Neither"
                    else:
                        for l in hex:
                            if l not in string.hexdigits:
                                return "Neither"

                return "IPv6"
        
        return "Neither"
