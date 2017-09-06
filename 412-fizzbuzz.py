class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.count = 0
        self.three = 3
        self.five = 5
        self.n = n
        return list(self.get_num())
        
    def get_num(self):
        while self.n > 0:
            self.n -= 1
            self.count += 1
            self.three -= 1
            self.five -= 1
            is_three = False
            is_five = False
            if self.three == 0:
                is_three = True
                self.three = 3
            if self.five == 0:
                is_five = True
                self.five = 5
            if is_three and is_five:
                yield "FizzBuzz"
            elif is_three:
                yield "Fizz"
            elif is_five:
                yield "Buzz"
            else:
                yield str(self.count)


if __name__ == '__main__':
    print Solution().fizzBuzz(15)
