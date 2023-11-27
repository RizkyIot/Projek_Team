import time

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_engine_started = False
    
    def start_engine(self):
        if self.is_engine_started:
            print("Mesin mobil sudah menyala!\n")
        else:
            print(f"Menyalakan mesin mobil: {self.make} {self.model} ({self.year})...")
            time.sleep(2)
            self.is_engine_started = True
            print("Vroom! Mesin mobil menyala!\n")

    def stop_engine(self):
        if not self.is_engine_started:
            print("Mesin mobil sudah mati!\n")
        else:
            print(f"Mematikan mesin mobil: {self.make} {self.model} ({self.year})...")
            time.sleep(2)
            self.is_engine_started = False
            print("Mesin mobil dimatikan!\n")


class Motorcycle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_engine_started = False
    
    def start_engine(self):
        if self.is_engine_started:
            print("Mesin motor sudah menyala!\n")
        else:
            print(f"Menyalakan mesin motor: {self.make} {self.model} ({self.year})...")
            time.sleep(2)
            self.is_engine_started = True
            print("Vroom! Mesin motor menyala!\n")

    def stop_engine(self):
        if not self.is_engine_started:
            print("Mesin motor sudah mati!\n")
        else:
            print(f"Mematikan mesin motor: {self.make} {self.model} ({self.year})...")
            time.sleep(2)
            self.is_engine_started = False
            print("Mesin motor dimatikan!\n")


print("Objek yang sudah dibuat:")
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2023)
car3 = Car("Honda", "Civic", 2022)

motorcycle1 = Motorcycle("Honda", "CBR500R", 2021)
motorcycle2 = Motorcycle("Yamaha", "MT-07", 2021)
motorcycle3 = Motorcycle("Suzuki", "GSX-R600", 2023)

print(f"Mobil: {car1.make} {car1.model} ({car1.year}), {car2.make} {car2.model} ({car2.year}), {car3.make} {car3.model} ({car3.year})")
print(f"Motor: {motorcycle1.make} {motorcycle1.model} ({motorcycle1.year}), {motorcycle2.make} {motorcycle2.model} ({motorcycle2.year}), {motorcycle3.make} {motorcycle3.model} ({motorcycle3.year})")
print()

if __name__ == "__main__":
    while True:
        print("Selamat datang di Aplikasi Kendaraan!") 
        
        print("Pilih opsi kendaraan:")
        print("1. Mobil")
        print("2. Motor")
        print("0. Keluar")

        choice = input("Masukkan pilihan Anda: ")

        if choice == "1":
            print("Pilih opsi mobil:")
            print("1. Toyota Camry")
            print("2. Ford Mustang")
            print("3. Honda Civic")
            print("4. Merek dan model lainnya")
            
            car_choice = input("Masukkan pilihan mobil Anda: ")
            
            if car_choice == "1":
                make = "Toyota"
                model = "Camry"
                year = 2022
            elif car_choice == "2":
                make = "Ford"
                model = "Mustang"
                year = 2023
            elif car_choice == "3":
                make = "Honda"
                model = "Civic"
                year = 2022
            elif car_choice == "4":
                make = input("Masukkan merk mobil: ")
                model = input("Masukkan model mobil: ")
                year = input("Masukkan tahun mobil: ")
            else:
                print("Pilihan mobil tidak valid. Silakan pilih opsi yang sesuai.\n")
                continue
            
            car = Car(make, model, year)
            car.start_engine()
            car.stop_engine()
        
        elif choice == "2":
            print("Pilih opsi motor:")
            print("1. Honda CBR500R")
            print("2. Yamaha MT-07")
            print("3. Suzuki GSX-R600")
            print("4. Merek dan model lainnya")

            motorcycle_choice = input("Masukkan pilihan motor Anda: ")

            if motorcycle_choice == "1":
                make = "Honda"
                model = "CBR500R"
                year = 2021
            elif motorcycle_choice == "2":
                make = "Yamaha"
                model = "MT-07"
                year = 2021
            elif motorcycle_choice == "3":
                make = "Suzuki"
                model = "GSX-R600"
                year = 2023
            elif motorcycle_choice == "4":
                make = input("Masukkan merk motor: ")
                model = input("Masukkan model motor: ")
                year = input("Masukkan tahun motor: ")
            else:
                print("Pilihan motor tidak valid. Silakan pilih opsi yang sesuai.\n")
                continue

            motorcycle = Motorcycle(make, model, year)
            motorcycle.start_engine()
            motorcycle.stop_engine()

        elif choice == "0":
            print("Terima kasih telah menggunakan Aplikasi Kendaraan. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang sesuai.\n")
