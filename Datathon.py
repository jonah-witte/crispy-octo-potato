import pandas as pd 
df = pd.read_csv("/Users/jonahwitte/Desktop/Datathon/file_3_Mar18_Output_1.csv")
floor_df = df[df['resolved'] == "floor"]
print(floor_df.head())