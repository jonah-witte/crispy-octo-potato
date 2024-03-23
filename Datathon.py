import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df1 = pd.read_csv("/Users/jonahwitte/Desktop/Datathon/file_3_Mar18_Output_1.csv")
df2 = pd.read_csv("/Users/jonahwitte/Desktop/Datathon/file_4_Mar18_Output_1.csv")
merged_df = pd.concat([df1, df2], ignore_index=True)
merged_df.to_csv('combined_dataset.csv', index=False)
floor_df = merged_df[merged_df['resolved'] == "floor"]
#hello testing 2
print(floor_df.head())


# df_mos_seq = floor_df['mos'].str.split("-", expand=True)

# # count the frequency of each option
# options_flat = df_mos_seq.apply(pd.Series.value_counts).sum(axis=1).drop('TR', errors="ignore")

# # sort options by frequency
# options_sorted = options_flat.sort_values(ascending=False)

# # bar graph for calls based on "digitally active" & "account date" & "resolved"
# # looking at whether digital literacy (wanting to be active online) impacts wanting to talk to agent

# df_eservice_resolved_group = df.groupby(['eservice_ind_13_march', 'resolved']).size().unstack(fill_value=0)
# df_eservice_resolved_group.plot(kind='bar', stacked=True)
# plt.title('Call Resolution by E-Service Enrollment Status')
# plt.xlabel('E-Service Enrollment Status')
# plt.ylabel('Number of Calls')
# plt.xticks(rotation=0)  
# plt.legend(title='Resolution Status')
# plt.tight_layout()  
# plt.show()

# transferred_counts = df_eservice_resolved_group['resolved']
# print(transferred_counts)
# # diff = transferred_counts['1'] - transferred_counts['0']
# # print(diff)