#https://www.geeksforgeeks.org/problems/map-operations/1?page=1&category=Hash,Map&difficulty=Basic&sortBy=submissions&selectedLang=python3

class Solution:
    def process_map(self, arr, x):
        mp = {}
        
        # Insert elements with their last index
        for i in range(len(arr)):
            mp[arr[i]] = i
        #or
        # for index,value in enumerate(arr):
        #   mp[value]=index
          
        # Print the map sorted by keys
        for key in sorted(mp.keys()):
            print(key, mp[key])
        
        # Erase element x if present
        if x in mp:
            mp.pop(x)
            print(f"erased {x}")
        else:
            print("not found")
        
        # Print the map after erasure
        for key in sorted(mp.keys()):
            print(key, mp[key])
