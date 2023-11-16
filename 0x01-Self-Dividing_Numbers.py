class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = [] 
        for num in range(left, right + 1):
            if num == 0:
                continue
            isSelfDividing = True 
            currNum = num  
            while currNum > 0:
                digit = currNum % 10 
                if digit == 0 or num % digit != 0:
                    isSelfDividing = False
                    break
                currNum //= 10  
            if isSelfDividing:
                result.append(num)  
        return result  
left = 1
right = 22
print(Solution().selfDividingNumbers(left, right)) 
