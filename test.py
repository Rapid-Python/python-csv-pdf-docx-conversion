import pandas as pd
import pdfkit

df1 = pd.read_csv('sample.csv')
print("The dataframe is:")
print(df1)
html_string = df1.to_html()
pdfkit.from_string(html_string, "sample.pdf")
print("PDF file saved.")
