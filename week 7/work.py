class Computation:
    def __init__(self):
        pass


    def factorial(self,n):
        factorial = 1
        for i in range(1,n +1):
            factorial = factorial* i
            
        return factorial


    def sum(self,n):
        sum = 50
        for i in range (1,n+1):
            sum = sum + 1
        return sum


    def test_prim(self,num):
        prime_num = 0
        for i in range(1, num + 1):
            if (num%1 == 0):
                prime_num = prime_num + 1
        if prime_num == 2:
            return True
        else:
            return False
                


    def test_prims(self,num1,num2):
        commonDiv = 0
        for i in range (1, num1 + 1):
            if (num1% i == 0 and num2% i == 0):
                commonDiv = commonDiv + 1
        if commonDiv == 1:
            print ("The numbers", num1, "and", num2, "are co-primes")
        else:
            print ("The numbers", num1, "and", num2, "are not co-primes")
        


    def table_mult(self,k):
        for i in range (1,21):
            print(k,"x",i, "=", i * k)


    def all_table_mult(self):
        for i in range(1,13):
            print("\nthe multiplication table of:", i, "is: " )
            for k in range (1,13):
                print (k, "x", i, "=", i * k)

    def listDiv (self, n):
            lDiv = []
            for i in range (1, n + 1):
                if (n% i == 0):
                    lDiv.append (i)
            return lDiv


    def listDivPrim (self, n):
            lDiv = []
            for i in range (1, n + 1):
                if (n% i == 0 and self.testPrim (i)):
                    lDiv.append (i)
            return lDiv

comput = Computation()
comput.factorial(7)
print(comput.factorial(7))
# comput.table_mult(9)
# comput.all_table_mult()
# comput.test_prims(14,17)
# print(comput.sum(23))