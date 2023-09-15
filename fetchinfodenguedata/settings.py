####db
import os
from pathlib import Path
from typing import Optional
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# PATHS
# ---------------------------
load_dotenv()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
ROOT_DIR = Path(__file__).resolve(strict=True).parent


# DATABASES VARIABLES
# ------------------------------------------------------------------------------
PSQL_DB = os.getenv("PSQL_DB")
PSQL_USER = os.getenv("PSQL_USER")
PSQL_HOST = os.getenv("PSQL_HOST")
PSQL_PASSWORD = os.getenv("PSQL_PASSWORD")
PSQL_PORT = os.getenv("PSQL_PORT")

def get_sqla_conn(database: Optional[str] = PSQL_DB):
    """
    Returns:
        DB_ENGINE: URI with driver connection.
    """
    try:
        connection = create_engine(
            f"postgresql://{PSQL_USER}:{PSQL_PASSWORD}@{PSQL_HOST}:{PSQL_PORT}/{database}"
        )
    except ConnectionError as e:
        print("[ERR:] Database connection error!")
        raise e
    return connection

# STATES ABBREVIATIONS AND NAMES
# ------------------------------------------
ESTADOS = {
    'RJ': 'Rio de Janeiro', 'ES': 'Espírito Santo', 'PR': 'Paraná', 'CE': 'Ceará',
    'MA': 'Maranhão', 'MG': 'Minas Gerais', 'SC': 'Santa Catarina', 'PE': 'Pernambuco', 
    'PB': 'Paraíba', 'RN': 'Rio Grande do Norte', 'PI': 'Piauí', 'AL': 'Alagoas',
    'SE': 'Sergipe', 'SP': 'São Paulo', 'RS': 'Rio Grande do Sul','PA': 'Pará',
    'AP': 'Amapá', 'RR': 'Roraima', 'RO': 'Rondônia', 'AM': 'Amazonas', 'AC': 'Acre',
    'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul', 'GO': 'Goiás', 'TO': 'Tocantins',
    'DF': 'Distrito Federal', 'BA': 'Bahia'
    }
