class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []  # Initialize an empty list to store self-dividing numbers
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
                currNum //= 10  # Divide the number by 10 to move to the next digit
            if isSelfDividing:
                result.append(num)  # Add the self-dividing number to the result list
        return result  # Return the list of self-dividing numbers

left = 1
right = 22
print(Solution().selfDividingNumbers(left, right))  # Call the method using an instance of the class
