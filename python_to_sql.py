import pandas as pd 
import pyodbc
import os 
import shutil
Raw_path="data/raw"
Processed_path="data/processed"

os.makedirs(Processed_path, exist_ok = True)
            
conn =  pyodbc.connect(
    "DRIVER={----------------------};"
    "SERVER=---------------;"
    "DATABASE=-------------;"
    "Trusted_Connection=yes;"
    "Encrypt=no;"
)

cursor = conn.cursor()

for file in os.listdir(Raw_path):
    if file.endswith(".csv"):
        filepath = os.path.join(Raw_path, file)
        df = pd.read_csv(filepath)

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO ventas (fecha, producto, cantidad, precio)
                VALUES (?, ?, ?, ?)
            """, row.fecha, row.producto, row.cantidad, row.precio)

        # commit UNA sola vez por archivo
        conn.commit()

        # mover SOLO cuando el archivo terminó
        shutil.move(filepath, os.path.join(Processed_path, file))
        print(f"Procesado y movido {file}")


cursor.close()
conn.close()

