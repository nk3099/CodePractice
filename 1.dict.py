cust_raw="""id,fname,lname,addr,city,state,pincode
11599,mary,aone,8708 highway,hickory,NC,28601
256,david,roriguez,7605 falls,chicago,IL,60625
12111,amber,franco,8766 prairie,santa cruz,CA,95060
8827,Brian,wilson,8396 corners,San Antonio,TX,78240
11318,Mary,Henry,3047 maze, Caguas,PR,00725"""

cust_header=cust_raw.split("\n")[0]
cust_data=cust_raw.split("\n")[1:]
print("cust_header\n",cust_header)
print("cust_data\n",cust_data)

"""
cust_dict = {}

print("\ncust_dict\n")
for x in cust_data:
	cust_dict[x.split(",")[0]]=tuple(x.split(",")[1:])

print(cust_dict)

print("for 11599: \n",cust_dict["11599"])
"""

cust_dict={x.split(",")[0]:tuple(x.split(",")[1:])for x in cust_data}
print("\ncust_dict\n",cust_dict)

nested_dict={}

for key,value in cust_dict.items():
	nested_dict[key]={
	   "fname":value[0],
	   "lname":value[1],
	   "addr":value[2],
	   "city":value[3],
	   "state":value[4],
	   "pincode":value[5]
	}

print("\nnested_dict\n",nested_dict)

print(nested_dict["12111"]["pincode"])
#or
print(nested_dict["12111"].get("pincode"))
#but print(nested_dict["12111"][2]) ==> error

cust_header=cust_raw.split("\n")[0]
cust_header=cust_raw.split("\n")[0].split(",") #==> will be a list

for key,value in cust_dict.items():
	nested_dict[key]={
	   cust_header[1]:value[0],
	   cust_header[2]:value[1],
	  cust_header[3]:value[2],
	   cust_header[4]:value[3],
	   cust_header[5]:value[4],
	   cust_header[6]:value[5]
	}

print("\nnested_dict\n",nested_dict)

orders_raw="""
1,2013-07-24 00:0:00.0,11599,closed
2,2013-07-24 00:0:00.0,256,payment
3,2013-07-24 00:0:00.0,12111,complete
4,2013-07-24 00:0:00.0,8827,closed
5,2013-07-24 00:0:00.0,11318,complete"""

orders_data=orders_raw.split("\n")

combine_result=[]

for x in orders_data:
	order=x.split(",")
	combine_result.append((order[0],order[1],order[2],order[3],cust_dict(order[2])) #to attach tuple

print(combine_result)

