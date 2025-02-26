# til_numb = int(input("enter the number"))
# list = []

# for i in range(1,til_numb+1):
#     if(i%3==0):
#         list.append("fizz")
#     elif(i%5==0):
#         list.append("buzz")
#     elif(i%3==0 and i%5==0):
#         list.append("fizzbuzz")
#     else:
#         list.append(i)      
# print(list)


# import pandas as pd; # type: ignore
# # pd.set_option('display.max_columns', None)
# data = pd.read_csv("employees.csv")
# # print(data)

# dataEm = data[data["Salary"] >100000]
# salaries_above_50000 = data[data["Salary"] > 50000]["Salary"]
# print(salaries_above_50000)

# A simple dictionary
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# print(person)

# # Iterate through the dictionary keys and print each key-value pair
# for key in person.keys():
#     print("Key is", key, "Value is", person[key])

# # Update the "name" key to "Jane"
# person["name"] = "Jane"
# print(person)

# num = int(input("enter number"))
# def prime(num):

#  count = 1
#  for i in range(2,num):  
#   count= i*count
#  print(count) 
# prime(num)

# import pandas as pd;

# data=pd.read_csv('employees.csv')
# print(data)
# print(data['Gender'].to_string(index=False))   
# min_salary_row = data[data['Salary'] == data['Salary'].min()]
# min_salary_row = data[data['Salary'] == data['Salary'].max()]['First Name']
# salary_above10k = data[data['Salary']>10000]['Gender'].fillna("Unkown")
# print(salary_above10k)




# num = int(input("Enter number"))

# def prime(num):   
#     count=0
#     for  i in range(2,num):
#         if(num%i==0):
#             count=count+1
#     if(count>0):
#         print("its not prime")
#     else:
#         print("its prime")    
    
# prime(num)



# def prime(num):
#     count = 0
#     for i in range(2,num):
#         if(num%i==0):
#             count= count+1
#     if(count<=0):
#      print("its prime number")
#     else:
#        print("its not prime")

# prime()


# import pandas as pd

# data = pd.read_csv("employees.csv")
# # print(data.info())
# # print(data['Salary'])
# salaries_above_50000 = data[data["Salary"] > 50000]["Salary"]
# salaryUptp = data[data['Salary']>80000]["Salary"]
# print(salaries_above_50000.to_string(index='false'))
 
class A :
    def show(self):
        print("welcome")
    def show(self, firstname=""):
        print("welcome",firstname) 

obj = A()
obj.show("Danish")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ")