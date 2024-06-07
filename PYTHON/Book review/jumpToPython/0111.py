class FourCal :
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(45,3)
print(a.add())
print(a.div())
class MoreFourCal(FourCal) :
    def pow(self):
        result = self.first **self.second
        return result
    def div(self):
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second

b = MoreFourCal()
b.setdata(10, 5)
print(b.pow())
print(b.add())
print(b.div())

c = MoreFourCal()
c.setdata(10, 0)
print("=")
print(b.add())
print(b.div())#0일 때, 리턴 값 없음.

d = FourCal()
d.setdata(10,0)
print(d.add())
print(d.div())