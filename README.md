# Brief-4-Rachid-Karbiche
Le rêve américain

Data Cleaning : les deux databases sont incomplètes sur les données aberrantes. Sinon, toutes les databases ont été intégrées dans les tables.
Data Visualization : les trois premières questions ont été faites pour la première database

Sur les notebooks, on communique avec les fichiers create_database (où les tables ont été créées) et integrate_data (fonction pour intégrer la donnée dans ces tables).

Il y a deux fichiers data_jobs.db dans le projet. Il faut prendre en compte celui présent dans le dossier notebook. J'ai cru voir passer une erreur en supprimant celui présent dans le dossier 02_intermediate.

Chemin de mon projet :

.
├── Data
│   ├── 01_raw
│   │   ├── 2020_Data_Professional_Salary_Survey_Responses.xlsx
│   │   └── DataAnalyst.csv
│   └── 02_intermediate
│       └── data_jobs.db
├── notebook
│   ├── cleaning_datas.ipynb
│   ├── data.jobs.db
│   └── visualizing_datas.ipynb
├── src
│   ├── d01_data
│   │   ├── __init__.py
│   │   └── create_database.py
│   ├── d02_intermediate
│   │   ├── __init__.py
│   │   └── integrate_data.py
│   └── __init__.py
├── .gitignore
├── README.md
└── requirements.txt