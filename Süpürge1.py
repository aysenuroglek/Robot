
import random

class SupurgeRobotu:
    def __init__(self, oda_boyutu):
        self.oda_boyutu = oda_boyutu
        self.kirli_halılar = set((random.randint(0, oda_boyutu-1), random.randint(0, oda_boyutu-1)) for _ in range(oda_boyutu))

        #  başlangıç konumu
        self.x, self.y = random.randint(0, oda_boyutu-1), random.randint(0, oda_boyutu-1)

    def temizle(self):
        if (self.x, self.y) in self.kirli_halılar:
            print(f"Kirli halı temizlendi: ({self.x}, {self.y})")
            self.kirli_halılar.remove((self.x, self.y))
        else:
            print(f"Bu halı zaten temiz: ({self.x}, {self.y})")

    def hareket_et(self):
        yeni_x, yeni_y = random.randint(0, self.oda_boyutu-1), random.randint(0, self.oda_boyutu-1)
        print(f"Hareket ediliyor: ({self.x}, {self.y}) -> ({yeni_x}, {yeni_y})")
        self.x, self.y = yeni_x, yeni_y


oda_boyutu = 5
robot = SupurgeRobotu(oda_boyutu)

while robot.kirli_halılar:
    robot.temizle()
    robot.hareket_et()





 