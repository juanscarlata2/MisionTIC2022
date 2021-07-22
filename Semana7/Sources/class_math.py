class matematica:
    def __init__(self, A, B):
        self.A=A
        self.B=B

    def suma(self):
        return self.A+self.B

    def resta(self):
        return self.A-self.B

    def dividir(self):
        if self.B == 0:
            return False
        else:
            return self.A/self.B



