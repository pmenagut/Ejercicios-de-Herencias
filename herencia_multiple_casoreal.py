

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_acristalada(self):
        superficie_total = 0
        for pared in self.paredes:
            if isinstance(pared, ParedCortina):
                superficie_total += pared.superficie
            else:
                for ventana in pared.ventanas:
                    if not ventana.proteccion:
                        raise Exception("Protección obligatoria")
                    superficie_total += ventana.superficie
        return superficie_total


class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []


class ParedCortina(Pared):
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie = superficie


class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        self.proteccion = proteccion
        pared.ventanas.append(self)


# Instanciación de las paredes
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

# Instanciación de las ventanas
ventana_norte = Ventana(pared_norte, 0.5, "Persiana")
ventana_oeste = Ventana(pared_oeste, 1, "Persiana")
ventana_sur = Ventana(pared_sur, 2, "Persiana")
ventana_este = Ventana(pared_este, 1, "Persiana")

# Instanciación de la casa con las 4 paredes
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])

print(casa.superficie_acristalada())  # Salida esperada: 4.5
