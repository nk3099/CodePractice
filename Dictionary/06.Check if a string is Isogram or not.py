#https://www.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/1?page=1&category=Hash,Map&difficulty=Basic&sortBy=submissions&selectedLang=python3

class Solution:
    def isIsogram(self,s):
        #Your code here
        
        counter={}
        
        for i in s:
            if counter.get(i) == None:
                counter[i]=1
            else:
                return False #is an isogram --> Isogram is a string in which no letter occurs more than once.
         
        return True
                
