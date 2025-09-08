#https://www.geeksforgeeks.org/problems/first-element-to-occur-k-times5150/1?page=1&category=Hash,Map&difficulty=Easy&sortBy=submissions&selectedLang=python3

class Solution:
    def firstElementKTime(self, arr,k):
        counter = {}
        
        for i in arr:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
            
            if counter[i]==k: #If there are multiple answers, please return the first one.
                return i
                
        return -1
    
