import numpy as n
import pandas as p
import matplotlib.pyplot as m
import seaborn as s
data=p.read_csv("C:/Users/vishnu prasath.N/Desktop/New folder/IMDB Dataset.csv")
data.head(121230)
data.columns
data.tail(100)
data.describe()
s.histplot(data["sentiment"],bins=30,kde=True)
m.title("Histogram")
m.xlabel("reviews")
m.ylabel("sentiment")
m.show()
data["sentiment"].value_counts().plot(kind='bar')
m.title("Bardiagram")
m.xlabel("Reviews")
m.ylabel("Sentiment")
m.show()
m.pie(data["sentiment"].value_counts(),labels=data["sentiment"].unique(),autopct="%.1f%%")
m.title("Piechart")
m.xlabel("Reviews")
m.ylabel("Sentiment")
m.show()
