class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        # virheellinen tilavuus nollataan
        self.tilavuus = max(tilavuus, 0.0)
        # negatiivinen saldo nollataan, ylimäärä menee hukkaan
        self.saldo = min(max(alku_saldo, 0.0), self.tilavuus)

    #huom: voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")
        print("test")

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
