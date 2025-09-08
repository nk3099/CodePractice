#https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?page=1&category=Hash,Map&difficulty=Medium&sortBy=submissions&selectedLang=python3

class Solution:
    def longestSubarray(self, arr, k):  
        
        #complexity O(N^2)
        """
        sum=0
        l=-1
        for i in range(len(arr)):
            sum=0
            for j in range(i,len(arr)):
                sum+=arr[j]
                if sum==k:
                    l=max(l,j-i+1)
            
        return l
        """
            
        
        #Optimized O(N) Solution Using Prefix Sum + Hash Map 
        #YT TakeUForward: https://www.youtube.com/watch?v=frf7qxiN2qU

        
        hashmap={}
        prefixsum=0
        l=0
        for i in range(len(arr)):
            prefixsum+=arr[i]
            if prefixsum==k:
                l=max(l,i+1)
            
            rem=prefixsum-k
            if rem in hashmap:
                l=max(l,i-hashmap[rem])
            
            #hashmap[prefixsum]=i
            #But, should only set hashmap[sum] if sum is not already in hashmap, 
            #to keep the earliest index for that prefix sum. (consider [2,0,0,0,3])
             
            if prefixsum not in hashmap:
                hashmap[prefixsum]=i
            
            
            
        return l
