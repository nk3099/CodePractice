#https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1?page=1&category=Hash,Map&difficulty=Easy&sortBy=submissions&selectedLang=python3

class Solution:
    def frequencyCount(self, arr):
        
        n = len(arr)
        counter={}
        ans=[]
        
        for i in arr:
            if i in counter:
                counter[i]+=1
            else:
                counter[i]=1
        
        # for i in range(1,n+1):
        #     if i in counter:
        #         ans[i].append(counter[i])
        #     else:
        #         ans[i].append(0)
                
        # Fill answer list with counts for numbers from 1 to n
        for i in range(1, n + 1):
            ans.append(counter.get(i, 0))  # Use .get() to avoid key errors
        
        return ans
        
        """
        trying to assign a value at index i of ans, 
        but ans is currently an empty list, so this raises an IndexError.
        So, should append values to the list ans, rather than assign 
        to an index that doesn't yet exist.
        
        IndexError: list index out of range
        This means you're trying to access ans[i] before it exists, 
        which happens when you use ans[i] = ... or ans[i].append(...) 
        on an empty or short list.

        AttributeError: 'int' object has no attribute 'append' => as .append() only works on lists
        """
