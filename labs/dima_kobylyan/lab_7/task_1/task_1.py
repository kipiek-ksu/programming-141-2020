import reguests
import cvs
r=reguests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=65&exp=json')
universities:list=r.json()
with open('Test.csv',mode='w',encoding ='UTF-8'as f:
    writer=csv.DictWriter(f,fieldnames=universities[0].keys())
    writer.writeheader()
    writer.writerows(universities)