class Arm:
    def Armstrong(self,n):
        a=n
        sum=0
        while n>0:
            r=n%10
            sum+=(r*r*r)
            n=n//10
        if a==sum:
            print("Armstrong Number")
        else:
            print("Not Armstrong")
        print(sum)
class Main(Arm):
    def jhghggh(self):
        pass
ob=Main()
n=int(input("Enter a number"))
ob.Armstrong(n)