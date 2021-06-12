class SumaVectoarial(list):
    def __add__(self, x):

        suma=[]

        for i in range(len(self)):
            suma.append(self[i]+x[i])

        return suma

v1=SumaVectoarial([1,4,10])
v2=SumaVectoarial([0,-2,-10])

print(v1 + v2)
