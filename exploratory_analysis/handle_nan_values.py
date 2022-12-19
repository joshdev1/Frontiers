import pandas as pd

df = pd.read_excel("journal_data.xlsx")

# df.columns = ["journal title", 'sections', 'articles', 'article views', 'citations', 'IF', 'citescore']
# is_new = ["yes", "no"]
# df["is new"] = is_new
print(df.columns)
