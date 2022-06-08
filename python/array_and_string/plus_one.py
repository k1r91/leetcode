from typing import List


class Frank:

    def fly(self):
        print("💩")


f = Frank()
f.fly()


def plus_one(digits: List[int]) -> List[int]:
    if digits[-1] < 9:
        digits[-1] += 1
        return digits
    else:
        i = -1
        while abs(i) <= len(digits) and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if abs(i + 1) == len(digits):
            digits = [1] + digits
        else:
            digits[i] += 1
        return digits


# print(plus_one([1, 2, 3]))
print(plus_one([4, 0, 9]))
