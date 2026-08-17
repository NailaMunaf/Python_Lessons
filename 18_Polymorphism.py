class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNum(self):
        print("complex number is:", self.real, "i +" , self.img, "j" )

    def AddNum(self, c2):
        newReal = self.real + c2.real
        newImg = self.img + c2.img
        return Complex(newReal, newImg)
        

c1 = Complex(3,5)
c1.showNum()

c2 = Complex(4,6)
c2.showNum()

c3 = c1.AddNum(c2)
c3.showNum()
