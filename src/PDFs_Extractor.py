import camelot
import pandas as pd
import os
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

pdf_dir = '../PDFs/'
for file_name in os.listdir(pdf_dir):
    if file_name.endswith('.pdf'):
        path = os.path.join(pdf_dir, file_name)

        # Ler as tabelas do PDF
        tables = camelot.read_pdf(
            path,
            pages='1',
            flavor='stream',
            table_areas=['53,497,570,353'],
            columns = ['53,158,244,320,393,468,570']
        )
        
        
# print(tables[0].parsing_report)
# camelot.plot(tables[0], kind="contour")
# plt.show()

df_raw = pd.concat([table.df for table in tables], ignore_index=True)

# Renomear as colunas
df_raw.rename(
    columns={
        1: 'Produto', 
        2: 'Min/Máx ATAC./SUPER - SÃO PAULO', 
        3: 'Min/Máx REVENDEDOR - SÃO PAULO', 
        4: 'Min/Máx - RIO DE JANEIRO', 
        5: 'Min/Máx REVENDEDOR - RIO DE JANEIRO',
        6: 'Min/Máx ATAC./SUPER - NORDESTE'
    }, 
    inplace=True
)

# Remover colunas desnecessárias
df_raw.drop(columns=[0,7], inplace=True)

df_raw.to_excel('Boletim_de_Precos.xlsx', index=False)