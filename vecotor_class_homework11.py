class Vector3D :
    def __init__(self,Vx=0,Vy=0,Vz=0):
        self._Vx = Vx
        self._Vy = Vy
        self._Vz = Vz
    #get
    def get_Vx (self):
        return self._Vx
    def get_Vy (self):
        return self._Vy
    def get_Vz (self):
        return self._Vz
    #set
    def set_Vx(self,x) :
        self._Vx = x
        return self._Vx
    def set_Vy(self,x) :
        self._Vy = x
        return self._Vy
    def set_Vz(self,x) :
        self._Vz = x
        return self._Vz

    def __add__(self, b):
        resultVx = self._Vx + b._Vx
        resultVy = self._Vy + b._Vy
        resultVz = self._Vz + b._Vz
        return resultVx,resultVy,resultVz

    def __sub__(self, b):
        resultVx = self._Vx - b._Vx
        resultVy = self._Vy - b._Vy
        resultVz = self._Vz - b._Vz
        return resultVx,resultVy,resultVz

    def __rsub__(self,b):
        resultVx =  b._Vx - self._Vx 
        resultVy =  b._Vy - self._Vy 
        resultVz =  b._Vz - self._Vz 
        return resultVx,resultVy,resultVz
    def __eq__(self,b):
        if self._Vx == b._Vx and self._Vy == b._Vy and self._Vz == b._Vz :
            return True
        else :
            return False
    def __ne__(self,b):
        if self._Vx != b._Vx or self._Vy != b._Vy or self._Vz != b._Vz :
            return True
        else :
            return False
    def __mul__(self,b):
        resultVx =  self._Vx * b
        resultVy =  self._Vy * b
        resultVz =  self._Vz * b
        return resultVx,resultVy,resultVz
    def __rmul__(self,b):
        resultVx =  b * self._Vx 
        resultVy =  b * self._Vy 
        resultVz =  b * self._Vz 
        return resultVx,resultVy,resultVz
    def __xor__(self,b):
        result = self._Vx * b._Vx + self._Vy * b._Vy + self._Vz * b._Vz
        return result
    def __str__(self):
        return 'Vector`s x = {self._Vx} , y = {self._Vy} , z = {self._Vz}'.format(self = self)
    def __truediv__(self,b):
        resultVx =  self._Vx / b
        resultVy =  self._Vy / b
        resultVz =  self._Vz / b
        return resultVx,resultVy,resultVz
    def __rtruediv__(self,b):
        resultVx =  b / self._Vx 
        resultVy =  b / self._Vy 
        resultVz =  b / self._Vz 
        return resultVx,resultVy,resultVz
    def __neg__(self):
        return  -self._Vx,-self._Vy,-self._Vz



#testing
def vector_3d_test() : 
    v = Vector3D(-1,2,3) 
    v2 = Vector3D(6,7,8)
    v.set_Vx(2)
    v2.set_Vz(9)
    v.set_Vy(-3)
    print(v.get_Vx())
    print(v2.get_Vy())
    print(v.get_Vz())
    print(v2==v)
    print(v2!=v)
    print(v2+v)  
    print(v2*3,0.5*v)
    print(v^v2) 
    print(str(v))
    print(v/1.5) 
    print(3/v2) 
    print(-v)

if __name__ == '__main__' :
    vector_3d_test()


