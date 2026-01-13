import pandas as pd
data = {
  "Name":["Aashish","Piyush","Raj","Aayush","Gunjita","Kartikeya","Sneha","Golu","Aditya","Rohit","Priyanshu"],
  "Marks":[85,89,90,91,80,81,95,93,78,82,98],
  "Age":[20,20,19,18,21,18,22,21,20,19,20]
}
df = pd.DataFrame(data)
print(df.head(),"\n")
print(df.tail(),"\n")
print(df.shape,"\n")
print(df.columns,"\n")
