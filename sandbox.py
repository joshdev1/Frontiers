import pandas as pd

my_dict = {}
my_data = {"articles": "71", "sections": "4"}
my_dict.update({"Frontiers in webscraping": my_data})
data_frame = pd.DataFrame.from_dict(my_dict, orient="index")
print(data_frame)


journal_metrics = ["12 sections", "10 articles", "33,620,681 article views",
                   "82,277 citations", "5.702 IF", "6.4 citescore", None]

