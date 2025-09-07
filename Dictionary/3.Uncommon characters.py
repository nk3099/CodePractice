#https://www.geeksforgeeks.org/problems/uncommon-characters4932/1?page=1&category=Hash,Map&difficulty=Basic&sortBy=submissions&selectedLang=python3

class Solution:
    # Function to find uncommon characters between two strings.
  def uncommonChars(self, s1, s2):
    dict1={}
    ans=set()

    for i in range(len(s1)):
        if dict1.get(s1[i]) is None:
            dict1[s1[i]] = 1
        else:
            dict1[s1[i]] += 1

    # Find characters in s2 not in s1
    for j in range(len(s2)):
        if dict1.get(s2[j]) is None:
            ans.add(s2[j])
    
    # Find characters in s1 not in s2        
    for key in dict1:
        if key not in s2:
            ans.add(key)
            
    ans2=sorted(ans) #as set doesn't have set.sort()
    
    str=""
    for s in ans2:
        str+=s
        
    
    return str
