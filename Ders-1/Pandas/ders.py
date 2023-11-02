import numpy as np
import pandas as pa

sales2017=pa.Series([10,20,30,40],["Benzin","Dizel","Eko","Gaz"])

sales2018=pa.Series([15,25,32,20],["Benzin","Dizel","Eko","Gaz"])


print("****2017 Sales*** \n")

print(sales2017)

print("****2018 Sales*** \n")

print(sales2018)

print("****Report Sales*** \n")

report=sales2017+sales2018

print(report)


