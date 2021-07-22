from data_csv import dataClients

class filtro:
    def __init__(self, file_name):
        self.file=file_name
        self.datos=dataClients(file_name=self.file)
        self.tabla=[]
        self.load_data() #cargamos los datos


    def load_data(self):
        self.datos.read()
        self.tabla=self.datos.tabla
        
    def filtrar_por(self, registro, valor):
        datos_filtrados=[]
        for fila in self.tabla:
            keys=list(fila.keys())
            if registro in keys:
                dato=fila[registro]
                if dato==valor:
                    datos_filtrados.append(fila)
        return datos_filtrados
    