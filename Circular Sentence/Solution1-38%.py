class Solution(object):
    def isCircularSentence(self, sentence):
        sen_list = sentence.split()

        if len(sen_list) == 1:
            if sen_list[0][0] == sen_list[0][-1]:
                return True
            return False

        for i in range(0, len(sen_list)-1):
            if sen_list[i][-1] != sen_list[i + 1][0]:
                return False

        return sentence[0] == sentence[-1]
