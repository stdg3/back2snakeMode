class Cat:
    def __init__(self, color, cat_type):
        self.size = None
        self.color = color
        self.cat_type = cat_type
    
    def set_size(self):
        if(self.cat_type == 'indoor'):
            self.size = 'small'
        
        else:
            self.size = 'undefined'
    
    def printSelf(self):
        print(self.size, self.color, self.cat_type)
    
xCat = Cat("black", cat_type="indoor")
xCat.set_size()
xCat.printSelf()


class Tiger(Cat):
    def set_size(self):
        if(self.cat_type == 'wild'):
            self.size = 'big'
        
        else:
            self.size = 'undefined'

print('+' * 8)

tCat = Tiger(cat_type='wild', color='orange')
tCat.set_size()
tCat.printSelf()
