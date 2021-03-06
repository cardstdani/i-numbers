import math

class complexNumber(object):
    def __init__(self, real, im):
        self.r = real
        self.i = im
        self.m = math.sqrt((self.r*self.r)+(self.i*self.i))
        self.a = math.atan(self.i / self.r) / ((2*math.pi)/360)

    def outputFormat(self):
        return (str(self.r) + ("+" if self.i >= 0 else "") + str(self.i) + "i")

    def sum(self, num2):
        return complexNumber(self.r + num2.r, self.i + num2.i)

    def sub(self, num2):
        return complexNumber(self.r - num2.r, self.i - num2.i)
    
    def mul(self, num2):
        return complexNumber((self.r * num2.r) - (self.i * num2.i), (self.r * num2.i) + (self.i * num2.r))
    
    def div(self, num2):
      result = complexNumber(self.r, self.i).mul(complexNumber(num2.r, -num2.i))
      divisor = (num2.r * num2.r) + (num2.i * num2.i)
      return complexNumber(result.r / divisor, result.i / divisor)
    
    def pow(self, exp):
      temp = complexNumber(self.r, self.i)
      num = temp

      for i in range(exp - 1):
        num = num.mul(temp)
      return num
    
    def root(self, index):
      modulus =  self.m**(1/index)
      numbers = []
      
      for i in range(index):
        angle = ((self.a + (360*i)) / index) * ((2*math.pi)/360)
        numbers.append(complexNumber(modulus * math.cos(angle), modulus * math.sin(angle)))
      return numbers


a = complexNumber(3, 4)
b = complexNumber(1, 8)
print(a.sum(b).outputFormat())
print(a.sub(b).outputFormat())
print(a.mul(b).outputFormat())
print(a.div(b).outputFormat())
print(a.pow(2).outputFormat())
print(b.root(3)[0].outputFormat())
