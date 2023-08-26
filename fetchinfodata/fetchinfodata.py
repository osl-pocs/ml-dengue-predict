import pandas as pd
from settings import get_sqla_conn, ROOT_DIR, ESTADOS
from typing import Tuple

# Define the database engine
DB_ENGINE = get_sqla_conn(database="dengue")

def get_notif_by_year(disease: str, start_year: str, end_year: str) -> Tuple[str, pd.DataFrame]:
    """
    Retrieves notifications by year and disease.

    Args:
        disease (str): The disease name (e.g., "dengue", "chikungunya", "zika").
        start_year (str): The start year.
        end_year (str): The end year.

    Returns:
        Tuple containing the file name and a DataFrame with the data.
    """
    CID10 = {"dengue": "A90", "chikungunya": "A92.0", "zika": "A928"}
    
    # SQL query to retrieve notification data
    SQL = f"""
        SELECT
            n.dt_notific,
            n.ano_notif,
            n.se_notif,
            n.municipio_geocodigo,
            m.nome AS nome_municipio,
            m.uf AS estado_sigla
        FROM
            "Municipio"."Notificacao" AS n
        JOIN
            "Dengue_global"."Municipio" AS m
        ON
            n.municipio_geocodigo = m.geocodigo
        WHERE
            n.ano_notif BETWEEN {start_year} AND {end_year}
        AND cid10_codigo = '{CID10[disease]}'
        ORDER BY
            n.ano_notif,
            n.se_notif,
            n.dt_notific,
            n.municipio_geocodigo;            
        """

    with DB_ENGINE.connect() as conn:
        print("Fetching Notification data for: ", disease)
        df = pd.read_sql_query(SQL, conn)

    fname = f"notification_{disease}_{start_year}_{end_year}"

    return fname, df

def df_to_csv(df: pd.DataFrame, fname: str) -> None:
    """
    Saves a DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to be saved.
        fname (str): The file name.

    Returns:
        None
    """
    df.to_csv(f"{ROOT_DIR}/dataset/{fname}.csv")

def fetch_weather(uf: str, start_date: str, end_date: str) -> Tuple[str, pd.DataFrame]:
    """
    Retrieves weather data for a specific state and date range.

    Args:
        uf (str): The state abbreviation (UF).
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        Tuple containing the file name and a DataFrame with the data.
    """
    
    state = ESTADOS.get(uf.upper(), None)  # Get the state name from the abbreviation

    if state is None:
        raise ValueError("Invalid state abbreviation.")

    # SQL query to retrieve weather data
    SQL = f"""
    SELECT m.uf, w.*
    FROM weather.copernicus_brasil w
    JOIN "Dengue_global"."Municipio" m
    ON w.geocodigo = m.geocodigo
    WHERE
        w.date BETWEEN '{start_date}' AND '{end_date}'
    AND m.uf = '{state}';
    """

    with DB_ENGINE.connect() as conn:
        print("Fetching climate data for: ", state)
        df = pd.read_sql_query(SQL, conn)

    fname = f"weather_{uf}_{start_date}_{end_date}"

    return fname, df

def weather_notific(uf: str, start_date: str, end_date: str) -> Tuple[str, pd.DataFrame]:
    """
    Retrieves weather and notification data for a specific state and date range.

    Args:
        uf (str): The state abbreviation (UF).
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.

    Returns:
        Tuple containing the file name and a DataFrame with the data.
    """

    state = ESTADOS.get(uf.upper(), None)  # Get the state name from the abbreviation

    if state is None:
        raise ValueError("Invalid state abbreviation.")

    # SQL query to retrieve weather and notification data with JOIN
    SQL = f"""
    SELECT
        m.uf,
        w.geocodigo,
        m.nome AS nome_municipio,
        n.dt_notific,
        n.se_notif,
        n.ano_notif,
        w.temp_med,
        w.precip_med,
        w.pressao_med,
        w.umid_med
    FROM weather.copernicus_brasil w
    JOIN "Dengue_global"."Municipio" m
    ON w.geocodigo = m.geocodigo
    JOIN "Municipio"."Notificacao" n
    ON w.date = n.dt_notific AND w.geocodigo = n.municipio_geocodigo
    WHERE
        w.date BETWEEN '{start_date}' AND '{end_date}'
    AND m.uf = '{state}';
    """

    with DB_ENGINE.connect() as conn:
        print("Fetching climate and notification data for: ", state)
        df = pd.read_sql_query(SQL, conn)

    fname = f"weather_notification_{uf}_{start_date}_{end_date}"

    return fname, df

if __name__ == "__main__":
    choice = input('Choose the dataset you want to export; W for weather data, N for notification data, or WN for combined data: ')

    if choice == 'N':
        # Get notification data and save to CSV
        disease = input("Disease (e.g., dengue, chikungunya, zika): ")
        start_year = input('Start year: ')
        end_year = input('End year: ')

        fname, data = get_notif_by_year(disease, start_year, end_year)
        df_to_csv(data, fname)

    elif choice == 'W':
        # Prompt user for state, start date, and end date to fetch weather data
        uf = input('State abbreviation (e.g., RJ): ')
        start_date = input('Start date (YYYY-MM-DD): ')
        end_date = input('End date (YYYY-MM-DD): ')

        fname, data = fetch_weather(uf, start_date, end_date)
        df_to_csv(data, fname)

    elif choice == 'WN':
        # Prompt user for state, start date, and end date to fetch combined weather and notification data
        uf = input('State abbreviation (e.g., RJ): ')
        start_date = input('Start date (YYYY-MM-DD): ')
        end_date = input('End date (YYYY-MM-DD): ')

        fname, data = weather_notific(uf, start_date, end_date)
        df_to_csv(data, fname)
