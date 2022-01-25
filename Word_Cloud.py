from wordcloud import wordcloud
import matplotlib.pyplot as plt
import pandas as pd
import csv

file = open("test.csv")

reader_contents = pd.read_csv(file, header = 1)

print(reader_contents)
