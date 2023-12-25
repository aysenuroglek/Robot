

class VacuumCleaner:
   def __init__(self, initial_state):
        self.state = initial_state  

   def clean(self):
        for i in range(len(self.state)):
            if self.state[i] == 1:  # Eğer halı kirliyse
                print(f"Kirli halı bulundu! Halı {i+1} temizleniyor.")
                self.state[i] = 0  # Halıyı temizle
            else:
                print(f"Halı {i+1} zaten temiz.")

   def display_state(self):
        print(f"Şu anki durum: {self.state}")

initial_state = [0, 1, 0]  # İlk durum: [temiz, kirli, temiz]
vacuum = VacuumCleaner(initial_state)

print("Başlangıç durumu:")
vacuum.display_state()

print("\nTemizleme işlemi başlıyor...")
vacuum.clean()

print("\nSon durum:")
vacuum.display_state()






