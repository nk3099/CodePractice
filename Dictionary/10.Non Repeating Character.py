#https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1?page=1&category=Hash,Map&difficulty=Easy&sortBy=submissions&selectedLang=python3

class Solution:
    def nonRepeatingChar(self,s):
        counter={}
        for i in s:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        for i in s:
            if i in counter:
                if counter[i]==1:
                    return i
        
        return '$'


#---OR---
class Solution:
    def nonRepeatingChar(self,s):
     
     freq = [0 for i in range(256)] #List Comprehension
     #creates a list named freq with 256 elements, all initialized to 0.
     #or freq = [0]*256
     
     for i in s:
         freq[ord(i)]+=1
     
     # for i in s:                 #iterating characters
     #     if freq[ord(i)]==1:
     #         return i
             
     for i in range(len(s)):     #iterating length(numbers)
         if freq[ord(s[i])]==1:
             return s[i]
             
             
     return '$'
            
    
    
