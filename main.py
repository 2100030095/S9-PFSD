class Pld:
    def palindrome(self,n):
        temp=n
        sum=0

        while(n>0):
            d=n%10
            sum=(sum*10)+d
            n=n//10
        if(temp==sum):
            print(temp,"is a palindrome")
        else:
            print(temp," not a palindrome")
class Main(Pld):
    def dfsd(self):
        pass
ob=Main()
a=int(input("Enter number"))
ob.palindrome(a)



