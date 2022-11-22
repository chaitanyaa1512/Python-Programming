class Mobile:
    shape= 'Cuboid'
    def __init__(self):
        self.ram='6GB'
        self.storage='128GB'
        self.price=72000
    def call(self, number):
        return f'calling {number}'
    def capture(self):
        return 'Photo captured'
    def record(self, type):
        return f'recording {type}'
class AppleMobile(Mobile):
    os='ios'
    def __init__(self):
        # Mobile.__init__(self)
        super().__init__()
        self.display='retina'
        self.camera='13MP'

iPhone = AppleMobile()
print(iPhone.shape, iPhone.ram, iPhone.storage, iPhone.price)
print(iPhone.record('audio'))
print(iPhone.os, iPhone.display, iPhone.camera)


class AndroidMobile(Mobile):
    pass
class AsusMobile(AndroidMobile):
    pass
class NothingMobile(AndroidMobile, AppleMobile):
    pass
nothing_phone_1 = NothingMobile()
print(nothing_phone_1.display)
print(nothing_phone_1.camera)
# single level inheritance=> 1 parent --> 1 child
# multilevel => parent -->child--> grandchild
# multiple => multi parents, 1 child
# heirarchical=> 1 parent--> many childrenc