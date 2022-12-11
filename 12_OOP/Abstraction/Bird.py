from  Animal import Animal

class Bird(Animal):

    def drink(self, a):
        print(f"Değer {a}")

    def walk(self):
        print("Yürüyebilir")

    def sleep(self):
        print("Uyuyabilir")
