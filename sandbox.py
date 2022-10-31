import pandas as pd

df = pd.read_excel("journal_data.xlsx")

print(df.describe())


# print("citescore =", np.mean(df["citescore"]))
# print("article views =", np.mean(df["article views"]))
# print("most views", np.max(df["article views"]))




