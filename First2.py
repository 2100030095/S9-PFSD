class Prime:
    def findPrime(self,n):
    #n=int(input("Enter number"))
        i=2
        flag=0
        while i<n:
            if n%i==0:
                flag=1
            i=i+1

        if flag==1:
            print("Not a prime number")
        else:
            print(n,"is a prime number")

class Main(Prime):
    def hghg(self):
        pass

    ob = Main()
    ob.findPrime(10)

