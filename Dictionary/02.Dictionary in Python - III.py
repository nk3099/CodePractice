#https://www.geeksforgeeks.org/problems/dictionary-in-python-iii/1&selectedLang=python3

# insert into dictionary
def insert_dict(query, dict):
    dict[query[1]] = int(query[2])

# deleting from dictionary
def del_dict(query, dict):
    if query[1] in dict:
        del dict[query[1]]
        return True
    return False
    

# print marks of required name
def print_dict(key, dict):
    flag = False
    if(key in dict):
        flag = True
        print ("Marks of " + key + " is "+ str(dict[key]))
        
    return True if flag is True else False
    
    
#my code: as i wrongly assumed _dict(query, dict) 
# --> query as array having list of items
# def print_dict(key, dict):
#     for s in query:
#         if s[0] == 'i':
#                 dict[s[1]] = s[2]
#                 print('Inserted')
#             elif s[0] == 'd':
#                 del dict[s[1]]
#                 print('Deleted')
#             else:
#                 print('Marks of ' + s[1] + ' is ' + str(dict[s[1]]))
    
    
    
