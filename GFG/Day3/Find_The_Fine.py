class Solution:
    def totalFine(self, n, date, car, fine):
        fine_Total = 0
        if date % 2 == 0:       #fine to odd cars when date is even 
            for i in range(n):
                if car[i]%2 != 0:
                    fine_Total += fine[i] 
        
        else:                   #fine to evrn cars when date is odd
            for i in range(n):
                if car[i]%2 == 0:
                    fine_Total += fine[i]
                    
        return  fine_Total
        

instance_class = Solution()        
result = instance_class.totalFine(4, 12, [2375, 7682, 2325, 2352], [250, 500, 350, 200]) 
print(result)