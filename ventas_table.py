import pandas as pd 
import random 
from datetime import datetime,timedelta
import os 


Raw_path="data/raw"
os.makedirs(Raw_path, exist_ok = True)


productos = ["Pencil","Paper","Blackboard","Book","Notebook"]

data=[]

for i in range (5):
 fecha_archivo = datetime.now() -timedelta(days = i)
 data=[]
 for i in range(50):
    data.append({
     "fecha":fecha_archivo,
     "producto":random.choice(productos),
     "cantidad":random.randint(1,10),
     "precio":round(random.uniform(100,1500),2)

     })

df = pd.DataFrame(data)


timestamp= fecha_archivo.strftime("%Y-&m-%d_%H-%M-%S")
filename=f"ventas_{timestamp}.csv"
filepath = os.path.join(Raw_path,filename)
df.to_csv(filepath, index = False)

print(f"Generado{filename}")




