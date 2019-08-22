class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
  
    def prt(self):
        print((self.x,self.y))
        return self # useful because you can insert prt anywhere...
            
    def __lt__(self,other):
        return self.x<other.x or (self.x==other.x and self.y<other.y)        
    def __gt__(self,other):
        return self.x>other.x or (self.x==other.x and self.y>other.y)    
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y    
    def __le__(self,other):
        return self.x<other.x or (self.x==other.x and self.y<=other.y)    
    def __ge__(self,other):
        return self.x>other.x or (self.x==other.x and self.y>=other.y)   
    def __ne__(self,other):
        return not (self==other)