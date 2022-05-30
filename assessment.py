# class
# function that holds the calculations
# area of a circle or square

# area of a rectangle= length * width

# python



Class Calculation:
    def __init__(self,length,width):
        self.lenth=length
        self.width=width
        
    def area(self):
        myCal=self.length*self.width
        return myCal
cal=Calculation(4,6)
print(cal)



