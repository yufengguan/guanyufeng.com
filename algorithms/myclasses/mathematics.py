"""
In mathematics, 
the Fibonacci numbers are the numbers in the following integer sequence, called the Fibonacci sequence, 
and characterized by the fact that every number after the first two is the sum of the two preceding ones
 { 0,1,1,2,3,5,8,13,21,34,55,89,144 ...}
"""

class MyFibonacci:
    def __init__(self, n):
        self.n = n     # instance variable unique to each instance
    
    def calculate(self):
        if type(self.n) != int: 
           raise TypeError ("n must be a positive int")

        result1 = "Recursion: "
        for i in range(0, self.n ):
            result1 += str( self.fibonacci_recursion(i))
            if (i !=self.n-1):
                result1 += ","  

        result2="Loop: "        
        for i in range(0,self.n):
            result2 += str( self.fibonacci_loop(i))
            if (i !=self.n-1):
                result2 += ","  
      
        result3 = ""
        for i in range(0,self.n):
            result3 += str( self.fibonacci_while(i))
            if (i !=self.n-1):
                result3 += ","  

        return result1 + "----" + result2 + "----" + result3


    #recurrence, recursive

    def fibonacci_recursion(self,n):
        if n<2: 
            return n
        else:
          return self.fibonacci_recursion(n-1) + self.fibonacci_recursion(n-2)

    def fibonacci_loop(self,n):
        if n<2: 
            return n
        else:                
            a,b=0,1
            for i in range(n-1):
                #a,b = b, a+b
                temp = a
                a = b
                b += temp
            return b

    def fibonacci_while(self,n):
        if n<2: 
            return n
        else:
            a,b = 0,1
            i = 0
            while i < n-1:
                a,b = b, a+b
                i += 1
            return b

    #n=0
    #for i in fibonacci_generator():
    #     if n>10:
    #         break;
    #         print (i)
    #         n +=1

    # def fibonacci_generator()  
    #     a,b=1,1
    #     while True:
    #         yield a
    #         a,b=b, a+b

              
                  