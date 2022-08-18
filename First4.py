class PrimeNo:

    #n=int(input("Enter number"))
    def PrimeToN(self,n):

        i=1
        while i<=n:
            flag=0
            j=2
            while j<=i//2:
                if i%j==0:
                    flag=flag+1
                    break
                j=j+1
            if flag==0 and i!=1:
                print(i,"prime")
            i=i+1

class Main(PrimeNo):
    def jhgjg(self):
        pass
n=int(input("Enter the Number"))
ob=Main()
ob.PrimeToN(n)