 class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 37% and 83%
        # value = ""
        # for i in digits:
        #     value += str(i)

        # value = int(value) + 1
        # final = []
        # for i in str(value):
        #     final.append(int(i))

        # return final

        # 46% and 16%
        # carry = 0
        # digits[-1] += 1
        # for i in range(len(digits)-1, -1, -1):
        #     value = digits[i] + carry
        #     carry = 0
        #     if value // 10 == 1:
        #         digits[i] = 0
        #         carry = 1
        #     else:
        #         digits[i] = value

        # if carry == 1:
        #     digits = [1] + digits

        # return digits
        
        final = [0] + digits
        x = 0
        for i in final:
            pos = len(final) - x - 1
            final[pos] += 1
            if final[pos] == 10:
                final[pos]=0
            elif pos != 0:
                final.pop(0)
                return final
            else:
                return final
            
            x += 1


            
