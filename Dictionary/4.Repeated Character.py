#https://www.geeksforgeeks.org/problems/repeated-character2058/1?page=1&category=Hash,Map&difficulty=Basic&sortBy=submissions&selectedLang=python3

class Solution:
    def firstRep(self, s):
        
        pos={}
        str=set()
        
        for index,char in enumerate(s):
            if pos.get(char)==None:
                pos[char]=index
            else:
                str.add(char)
        
        ans=""
        min=float('inf')
        for i in str:
            if i in pos:
                if pos[i]<min:
                    min=pos[i]
                    ans=i
        
        if min==float('inf'):
            return -1
        else:
            return ans
            
#float('inf')
#This represents infinity, which is guaranteed to be greater 
#than any integer value in the string indices.


#---OR----

class Solution:
    def firstRep(self, s):
        
        pos={}
        
        for i in s:
            if i in pos:
               pos[i]+=1
            else:
                pos[i]=1
        
        # iterating over the string again
        for i in s:
            # checking if the frequency of the character is greater than 1
            if pos[i]>1: 
                # if yes, return the character
                return i
                        # creating an empty dictionary to store the frequency of each character
      

        # if no repeated characters found, return -1
        return -1
        
                
                

            
                    
        
                
                

            
