class Sample:
    def Display(self):
        print("Hello")
class Derived(Sample):
    def Display(self):
        print("World")
ob=Derived()
ob.Display()