class Mobile:
    #construtor
    def __init__(self, ram, processor, price): #special method 
#self-> parameter refer to objects
 #attributes
        self.__ram=ram #public
        self.__processor= processor #protected
        self.__price=price #private
    
    
    def __str__(self):
        return f'RAM: {self.__ram}\nProcessor:{self.__processor}\nPrice:{self.__price}'
    #getter or accessor
    def get_ram(self):
        return self.__ram
    def get_processor(self):
        return self.__processor
    def get_price(self):
        return self.__price
    #setters
    def set_ram(self,ram):
        self.__ram=ram
    def set_processor(self,processor):
        self.__processor=processor
    def set_price(self,price):
        self.__price=price

m1= Mobile('18GB','8Gen1',90000)
m2= Mobile('12GB','865+',55000)
m3= Mobile('8GB','85S',35000)
print(m1)
print(m2)
print(m3)
#print(m1.ram)
#print(m2.data())
#print(Mobile.data(m1))
print(m1.get_price)
#print(m2._processor)
#m1.__price=1
#print(m1._Mobile__price)
#obj1="KA"
#print(obj1)
#print("Hurray!")
