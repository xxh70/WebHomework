import pandas as pd
a=pd.read_csv("cities.csv")
alist=a.values.tolist()
html=''
for row in alist:
    html+='<tr>'
    html+='<td>'
    html+=str(row[0])
    html+='</td>'
    html+='<td>'
    html+=str(row[1])
    html+='</td>'
    html+='<td>'
    html+=str(row[2])
    html+='</td>'
    html+='<td>'
    html+=str(row[3])
    html+='</td>'
    html+='<td>'
    html+=str(row[5])
    html+='</td>'
    html+='<td>'
    html+=str(row[6])
    html+='</td>'
    html+='<td>'
    html+=str(row[7])
    html+='</td>'
    html+='<td>'
    html+=str(row[8])
    html+='</td>'
    html+='</td>'
    html+='<td>'
    html+=str(row[9])
    html+='</td>'
    html+='</tr>'


    
