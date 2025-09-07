#https://www.geeksforgeeks.org/problems/find-unique-element2632/1?page=1&category=Hash,Map&difficulty=Basic&sortBy=submissions&selectedLang=python3

class Solution:
    def find_unique(self, k, arr):
        
        counter={}
        
        for i in arr:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        for i in counter:
            if counter[i]!=k:
                return i
