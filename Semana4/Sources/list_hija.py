class sublista(list):

    def promedio(self):
        pro=sum(self)/len(self)
        return pro

    def append(self, valor):
        super().append(valor)
        return len(self)


milista1=sublista([1,2,3,6])
longitud=milista1.append(13)
longitud=milista1.append(4)
print(longitud)