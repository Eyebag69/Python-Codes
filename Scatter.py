import pandas as pd
import matplotlib.pyplot as plt
data = {
  "Name":["Aashish","Piyush","Raj","Aayush","Gunjita","Kartikeya","Sneha","Golu","Aditya","Rohit","Priyanshu"],
  "Marks":[85,89,90,91,80,81,95,93,78,82,98],
  "Age":[20,20,19,18,21,18,22,21,20,19,20]
}
df = pd.DataFrame(data)
plt.scatter(df["Age"], df["Marks"])
plt.title("Age and Marks")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.show()
