# https://www.codewars.com/kata/a-chain-adding-function/train/python
# adding function: add(1)(2)(3)
class add(int):
    def __call__(self,n):
        return add(self+n)
