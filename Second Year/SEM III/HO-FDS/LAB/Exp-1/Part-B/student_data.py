import pandas as pd
 
# intialise data of lists.
Student = {'Name':['Tom', 'nick', 'krish', 'jack','ajay','vijay','satish'],
        'Physics':[20, 21, 19, 18,21, 19, 18],
        'Chemistry':[20, 21, 19, 18,21, 19, 18],
        'Math':[20, 21, 19, 18,21, 19, 18],
        'English':[20, 21, 19, 18,21, 19, 18],
        'Computer':[20, 21, 19, 18,21, 19, 18]
        }
 
# Create DataFrame
df = pd.DataFrame(Student)
 
# Print the output with index.
# print(df)
#A. saving the dataframe
df.to_csv('Mark.csv', header=False, index=False)
# saving the dataframe
df.to_csv(r'D:Mark.csv')

#B. save the DataFrame without index
print('Student Data with Indexes')
df.to_csv("file2.csv", index=False)
print(df)
# C. set index as Name column
df.set_index("Name", inplace=True)
# save the DataFrame (here we don't need to set index attribute)
df.to_csv("file.csv")
print("Without Index")
print(df)
# D. Read data of 5 student from Mark.csv and Display it
print('Five rows')
#print(df.to_string()) 
Five_df = pd.read_csv("file.csv", nrows=5)
print(Five_df)