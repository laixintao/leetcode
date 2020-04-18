# -*- coding: utf-8 -*-

class Solution(object):
    def atry(self, left, right):
        answer = int((left + right) / 2)
        guess_result = guess(answer)
        if guess_result == -1:
            return self.try(left, answer)
        elif guess_result == 1:
            return self.try(answer+1, right)
        else:
            return answer
    
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.atry(0, n)
            
