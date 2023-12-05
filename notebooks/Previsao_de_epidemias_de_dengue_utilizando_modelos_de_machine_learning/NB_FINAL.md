<div style="text-align:center"><img src="https://hackmd.io/_uploads/H1ZOOXMRh.png" /></div>


---

# Projeto I - Aplicação de Métodos de Aprendizagem de Máquina

| Matrícula   | Nome do Acadêmico          |
| ----------- | -------------------------- |
| **1975660** | Felipe Paes de Lima        |
| **3972217** | Marlon Luciano da Silva    |
| **4469827** | Nazaré Aline Sá de Azevedo |
| **4518087** | Roger da Rosa Szortyka     |
| **4525523** | Sandro Loch                |

## Previsão de Epidemias de Dengue Utilizando Modelos de Aprendizado de Máquina: Um Estudo com Dados do Sistema Infodengue


  A **dengue** é a doença viral urbana mais prevalente nas Américas, principalmente no Brasil. É uma doença febril que tem se mostrado de grande importância em saúde pública nos últimos anos[[**4**]](#Referências-Bibliográficas).  Segundo a Organização Mundial da Saúde (OMS), o Brasil é o país mais afetado[[**5**]](#Referências-Bibliográficas). Nesse contexto, a aplicação de técnicas de Machine Learning pode ser uma ferramenta valiosa para a previsão e prevenção de surtos de dengue.


Este projeto de ML aborda a influência do clima na transmissão de arboviroses, destacando a sazonalidade dessas doenças durante os períodos mais quentes e úmidos. De acordo com estudos, a umidade relativa do ar pode influenciar a presença de recipientes positivos para a reprodução do mosquito Aedes aegypti, que transmite o vírus da dengue. Além disso, a umidade relativa do ar pode favorecer o desenvolvimento larvário do mosquito em determinadas faixas de temperatura. A relação entre temperatura, umidade e a incidência de dengue pode variar de acordo com o local e as condições climáticas específicas[[**7**]](#Referências-Bibliográficas).


### Objetivo

O objetivo deste projeto é desenvolver modelos de aprendizado de máquina capazes de **prever incidências de dengue** com base em dados históricos do Sistema Infodengue e tem como foco a análise e previsão de notificações de casos de dengue no estado do Ceará.

É importante destacar que, dada a relevância do estado do **Ceará** em termos de incidência da doença, optou-se por concentrar a análise nessa região. Durante o período selecionado para esta pesquisa, o Ceará registrou uma quantidade considerável de casos de dengue, justificando a escolha por esse estado como o principal objeto de estudo.


<small>*Nota*: *A previsão de surtos de doenças como a dengue envolve vários fatores, incluindo vigilância epidemiológica, monitoramento de vetores e intervenções de saúde pública. Portanto, modelos de previsão devem ser usados em conjunto com outras informações para tomar decisões informadas sobre medidas de controle e prevenção*</small>


### Especificação Técnica

**Dataset:**  Utilizou-se o banco de dados do Sistema Infodengue, que contém informações sobre notificações de dengue. Os dados foram formatados em um arquivo CSV e incluem campos como geocódigo do município, nome do município, estado do município, semana epidemiológica e ano de notificação.

**Formato:**  A base de dados encontra-se em **formato CSV**. Possui **10 colunas**, **1.425.240  observações**, em que cada observação corresponde à uma notificação no estado do **Ceará** (CE).

**Descrição das Features:** A tabela abaixo descreve mais detalhadamente a composição do conjunto de dados.

| **Coluna**     | **Tipo**         | **Descrição**                                                           | **Exemplo**  |
|----------------|------------------|-------------------------------------------------------------------------|--------------|
| uf             | texto (str)      | Nome da unidade federativa do Brasil                                    | Minas Gerais |
| geocodigo      | número (int64)   | Código IBGE associado aos município brasileiros composto por 7 digitos  | 4209102      |
| nome_municipio | texto (str)      | Nome do município                                                       | Joinville    |
| dt_notific     | data (Timestamp) | Data da notificação em format ISO 8601                                  | 2020-07-22   |
| se_notif       | número (int64)   | Semana em que ocorreu a notificação                                     | 18           |
| ano_notif      | número (int64)   | Ano em que ocorreu a notificação                                        | 2022         |
| temp_med       | número (float64) | Temperatura média em graus Celsius                                      | 20.466202    |
| precip_med     | número (float64) | Precipitação média                                                      | 0.035414     |
| pressao_med    | número (float64) | Pressão atmosférica média                                               | 1.005391     |
| umid_med       | número (float64) | Umidade relativa do ar média                                            | 87.35066     |

**Métodos de Pré-processamento:** Um dos principais destaques nas tarefas de pré-processamento deste projeto foi a extração e transformação necessárias para obtenção deste conjunto de dados (detalhes na seção *Metodologia para Extração de Dados*). Em posse dos dados, outras operações de pré-processamento foram necessárias, destacando-se:
  - Extração de dados (mais detalhes podem ser encontrados em [**Metodologia para Extração de Dados**](##Metodologia-para-Extração-de-Dados))
  - Agrupamento e/ou categorização dos dados, gerando uma nova coluna com nossa variável de saída (quantidade total de notificações ou ocorrências).
  - Agrupamento dos dados em intervalos semanais (semanas epidemiológicas).
  
**Modo de Aprendizado**: Supervisionado.

**Tarefa de Aprendizado:** Será aplicada a tarefa de Regressão.

**Algoritmos Avaliados:** Random Forest, Decision Tree, Gradient Boosting e Ada Boost .

**Métricas Utilizadas:** Raiz do erro quadrático médio (RMSE, do inglês Root Mean Squared Error) e R². ([**Nogueira, 2020**](#Referências-Bibliográficas). p. 132)

### Metodologia para Extração de Dados

#### 1. Extração, Transformação e Inserção de Dados de Notificações de Casos no Banco de Dados do Infodengue
##### Sistema Infodengue usando a API do PySUS por meio do script AlertaDengue

Nesta seção, descreveremos detalhadamente o processo de pré-processamento de dados realizado pelo script *pysus.py* do [AlertaDengue](https://github.com/AlertaDengue/AlertaDengue/blob/main/AlertaDengue/dbf/pysus.py), Os dados são coletados do [DataSUS](https://datasus.saude.gov.br/) por meio da  biblioteca [PySUS](https://github.com/AlertaDengue/pysus), abordando a coleta, tratamento e inserção dos dados, passando por várias transformações que são, por fim, inseridos no banco de dados da dengue no sistema [Infodengue](https://info.dengue.mat.br/informacoes/), utilizando o PostgreSQL como mecanismo de gerenciamento de banco de dados.

- **Coleta de Dados** : O script inicia o processo de pré-processamento coletando dados do DataSUS. Isso envolve a aquisição de informações sobre casos de doenças específicas, como dengue, chikungunya e zika, para um determinado ano.
- **Cálculo de Campos Relevantes** : Os dados coletados não estão prontos para serem inseridos no banco de dados do sistema Infodengue. Portanto, o script executa uma série de cálculos para criar campos adicionais e corrigir dados inconsistentes ou mal formatados. Isso inclui o cálculo da data de nascimento com base na idade do paciente, a adição de dígitos verificadores aos geocódigos municipais e a correção de códigos CID10 de doenças.
- **Transformação de Dados** : O script realiza transformações nos dados para garantir que eles atendam aos requisitos do sistema Infodengue. Isso inclui a padronização de campos, como a representação da semana epidemiológica brasileira.
- **Inserção no Banco de Dados** : Após a coleta e transformação dos dados, o script estabelece uma conexão com o banco de dados PostgreSQL do sistema Infodengue. Ele insere os dados pré-processados no banco de dados, seguindo uma estratégia de inserção que evita a duplicação de registros. Isso garante que os dados estejam prontos para análises futuras e disponíveis para consulta no sistema Infodengue.
- **Registro de Erros**: Durante o processo de pré-processamento e inserção, o script monitora possíveis erros ou exceções. Em caso de erro, ele registra informações detalhadas em um arquivo de log para fins de depuração e auditoria.

#### Os principais componentes e funcionalidades do script [pysus.py](https://github.com/AlertaDengue/AlertaDengue/blob/main/AlertaDengue/dbf/pysus.py) incluem:

- **settings (AlertaDengue.ad_main)** : Essa importação específica refere-se a configurações personalizadas definidas nas conficurações principais do projeto AlertaDengue. Essas configurações incluem detalhes de conexão com o banco de dados PostgreSQL.

- **episem (AlertaDengue.dados.episem)** : A biblioteca episem é utilizada para cálculos relacionados a semanas epidemiológicas, que são cruciais para a análise de dados relacionados à dengue.

- **SINAN (pysus.online_data)** : SINAN é uma ferramenta que permite o acesso a dados online, incluindo a obtenção de dados do DataSUS. Neste contexto, ele é usado para baixar dados relacionados à dengue.

<details><summary><b>Para realizar essas operações, o faz uso das seguintes bibliotecas de terceiros</b></summary>

- **numpy (np)** : Esta biblioteca é amplamente usada para cálculos matemáticos e operações em arrays multidimensionais. No contexto deste script, o numpy é utilizado para efetuar cálculos em campos como idade e geocódigos municipais.

- **pandas (pd)** : O pandas é uma biblioteca poderosa para manipulação e análise de dados. Aqui, o pandas é empregado para estruturar e limpar os dados, incluindo a seleção de colunas relevantes, ajuste de tipos de dados e tratamento de valores ausentes.

- **psycopg2** : Essa biblioteca possibilita a conexão com um banco de dados PostgreSQL. O script a utiliza para se conectar ao banco de dados do sistema Infodengue e inserir os dados processados.

- **pathlib** : A biblioteca pathlib é usada para lidar com caminhos de arquivo e diretório de forma eficiente. Ela auxilia na organização e manipulação de arquivos, incluindo a leitura de arquivos Parquet e a criação de diretórios para armazenamento temporário.

- **datetime e timedelta** : Essas bibliotecas nativas do Python são usadas para manipulação de datas e horários. São fundamentais para calcular datas de nascimento a partir da idade dos pacientes e para calcular datas epidemiológicas.

- **glob** : A biblioteca glob é útil para pesquisa de arquivos em um diretório com base em padrões de nome de arquivo. Aqui, ela é usada para encontrar e processar múltiplos arquivos Parquet com dados do DataSUS.

- **logging** : O módulo de logging é usado para registrar informações relevantes durante a execução do script, auxiliando na depuração e no monitoramento.

</details>


#### 2. Extração, Transformação e Inserção de Dados Climáticos no Banco de Dados do Infodengue
##### Sistema Infodengue usando a API do Copernicus por meio do script [copebr.py](https://github.com/osl-incubator/satellite-weather-downloader/blob/main/satellite/weather/copebr.py) Satellite-Weather-Downloader

O [Satellite-Weather-Downloader](https://github.com/osl-incubator/satellite-weather-downloader) captura os dados meteorológicos da API [Copernicus](https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels). Esta biblioteca oferece funcionalidades para capturar, converter e processar os dados para uso em análises meteorológicas no contexto brasileiro.

#### Os principais componentes e funcionalidades do script [copebr.py](https://github.com/osl-incubator/satellite-weather-downloader/blob/main/satellite/weather/copebr.py#L230) do **Satellite-Weather-Downloader** incluem:

- **CopeBRDatasetExtension** : Esta classe é uma extensão para objetos xr.Dataset que permite adicionar funcionalidades específicas do Brasil para dados meteorológicos.

- **Métodos como to_dataframe e to_sql** : Permitem converter os dados do conjunto de dados xarray em estruturas de dados como DataFrames do Pandas e inseri-los em um banco de dados SQL, respectivamente.

- **Métodos como _geocode_ds e _geocode_to_dataframe** : São usados para processar e extrair dados meteorológicos específicos para uma localização geográfica (identificada pelo IBGE geocode).

- **_convert_to_br_units** : É usado para converter unidades de medidas para padrões brasileiros, como a conversão de Kelvin para Celsius, metros para milímetros e Pascal para ATM.

- **_get_latlons** : Extrai as coordenadas de latitude e longitude para um determinado geocode IBGE de uma cidade brasileira.

*Destaca-se a função [_convert_to_br_units](https://github.com/osl-incubator/satellite-weather-downloader/blob/main/satellite/weather/copebr.py#L230) que é responsável por converter unidades de medidas em um conjunto de dados xarray para padrões brasileiros. Isso é importante porque as unidades de medidas usadas em dados meteorológicos podem variar dependendo da origem dos dados, e é útil padronizá-las para uma análise mais consistente no contexto brasileiro.*

#### Explicação passo a passo do que esta função faz:

  1. Recebe um conjunto de dados xr.Dataset como entrada.
  2. Verifica quais variáveis de dados estão presentes no conjunto de dados (por meio da lista de nomes das variáveis vars).
  3. Para cada variável presente no conjunto de dados, verifica se ela corresponde a alguma variável específica de acordo com seu nome (por exemplo, "t2m" para temperatura em Kelvin, "tp" para precipitação em metros, "msl" para pressão em Pascal).
  4. Se uma variável corresponder a alguma dessas variáveis específicas, a função realiza as seguintes conversões de unidades:
  5. Para "t2m" (temperatura em Kelvin), ela converte para Celsius subtraindo 273.15 e define as unidades e o nome longo apropriados.
  6. Para "d2m" (temperatura do ponto de orvalho em Kelvin), ela realiza o mesmo cálculo de conversão para Celsius e também calcula a umidade relativa do ar em porcentagem usando a fórmula de [Buck](https://es.wikipedia.org/wiki/Ecuaci%C3%B3n_de_Arden_Buck).
  7. Para "tp" (precipitação em metros), ela converte para milímetros multiplicando por 1000 e arredonda para 5 casas decimais. Também define as unidades e o nome longo apropriados.
  8. Para "msl" (pressão ao nível do mar em Pascal), ela converte para ATM multiplicando por um fator específico e define as unidades e o nome longo apropriados.

*A função retorna o conjunto de dados resultante com as unidades convertidas e os nomes convencionados.*

<details><summary><b>Para realizar essas operações, script o faz uso das seguintes bibliotecas de terceiros</b></summary>

- **dask** : Utilizado para computação paralela e assíncrona, útil para processamento eficiente de grandes volumes de dados.

- **dask.array** : Oferece suporte para arrays Dask, que são úteis para computação paralela em dados multidimensionais, como dados climáticos.

- **dask.dataframe** : Usado para trabalhar com estruturas de dados semelhantes a DataFrames em um ambiente Dask.

- **numpy** : Amplamente utilizado para cálculos matemáticos e operações em arrays multidimensionais.

- **xarray** : Essencial para trabalhar com dados multidimensionais, como dados climáticos, de forma eficiente.

- **loguru** : Biblioteca de registro de eventos usada para registrar informações durante a execução do script, auxiliando na depuração e no monitoramento.

- **sqlalchemy.engine.Connectable** : Usado para estabelecer conexões com bancos de dados SQL, como o PostgreSQL, para inserir dados processados.

</details>
</br>

Em resumo, o pré-processamento de dados realizado pelos scripts é uma etapa crítica que visa garantir a qualidade, consistência e integridade dos dados coletados antes de serem incorporados ao banco de dados do sistema Infodengue.


#### Agrupamento e/ou categorização dos dados
##### Consulta no banco de dados Infodengue e exportação do conjunto de dados em formato CSV
Para a obtenção dos dados relevantes necessários para o treinamento dos modelos de machine learning, foi criada uma função **weather_notific** especifica no script do repositório [ml-dengue-predict](https://github.com/osl-pocs/ml-dengue-predict/tree/main) para isso e script [fetchinfodenguedata.py](https://github.com/osl-pocs/ml-dengue-predict/blob/main/fetchinfodenguedata/fetchinfodenguedata.py) é responsável por extrair dados de clima e notificação da dengue para um estado específico em um intervalo de datas fornecido. Ele realiza uma consulta que envolve várias junções de tabelas para combinar dados meteorológicos e de notificação relevantes para análises posteriores.

- Função: [weather_notific](https://github.com/osl-pocs/ml-dengue-predict/blob/main/fetchinfodenguedata/fetchinfodenguedata.py#L162)

```Python
def weather_notific(
        uf: str,
        start_date: str,
        end_date: str
    ) -> Tuple[str, pd.DataFrame]:
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
```

Após a recuperação desses dados, eles são exportados para um arquivo CSV. Esse arquivo CSV contém os dados que serão usados no treinamento dos modelos de machine learning, permitindo análises avançadas e a criação de modelos preditivos relacionados à dengue e outras doenças transmitidas por vetores.

---

### Pré-Processamento

#### Importando Bibliotecas


```python
# Primeiro importamos as bibliotecas e módulos necessários
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) # silence warnings

import numpy as np
import pandas as pd
# !pip install mapclassify
import mapclassify

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
```

#### Conexão com o Dataset utilizado


```python
# Criar um dataframe usando a função `read_csv` do pandas.
data_path = "https://info.dengue.mat.br/datasets/notificacao/csv/weather_notification_CE_2010-01-01_2023-10-21.csv"

df = pd.read_csv(data_path,index_col=[0]).reset_index(drop=True)
print("Exibir informação dos campos e tipos de dados usando a função info() do pandas: \n")
df.info()
```

    Exibir informação dos campos e tipos de dados usando a função info() do pandas: 
    
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1425240 entries, 0 to 1425239
    Data columns (total 10 columns):
     #   Column          Non-Null Count    Dtype  
    ---  ------          --------------    -----  
     0   uf              1425240 non-null  object 
     1   geocodigo       1425240 non-null  int64  
     2   nome_municipio  1425240 non-null  object 
     3   dt_notific      1425240 non-null  object 
     4   se_notif        1425240 non-null  int64  
     5   ano_notif       1425240 non-null  int64  
     6   temp_med        1425240 non-null  float64
     7   precip_med      1425240 non-null  float64
     8   pressao_med     1425240 non-null  float64
     9   umid_med        1425240 non-null  float64
    dtypes: float64(4), int64(3), object(3)
    memory usage: 108.7+ MB



```python
print("Exibir os 5 primeiros registros dos dados usando a função head() do pandas: \n")
df.head()
```

    Exibir os 5 primeiros registros dos dados usando a função head() do pandas: 
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>uf</th>
      <th>geocodigo</th>
      <th>nome_municipio</th>
      <th>dt_notific</th>
      <th>se_notif</th>
      <th>ano_notif</th>
      <th>temp_med</th>
      <th>precip_med</th>
      <th>pressao_med</th>
      <th>umid_med</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ceará</td>
      <td>2309805</td>
      <td>Pacoti</td>
      <td>2020-03-31</td>
      <td>14</td>
      <td>2020</td>
      <td>25.879807</td>
      <td>0.364901</td>
      <td>0.996453</td>
      <td>88.508120</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ceará</td>
      <td>2310852</td>
      <td>Pindoretama</td>
      <td>2020-04-13</td>
      <td>16</td>
      <td>2020</td>
      <td>27.737236</td>
      <td>0.068862</td>
      <td>0.997939</td>
      <td>81.584460</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ceará</td>
      <td>2304400</td>
      <td>Fortaleza</td>
      <td>2020-07-02</td>
      <td>27</td>
      <td>2020</td>
      <td>26.324260</td>
      <td>0.020131</td>
      <td>0.999316</td>
      <td>79.740380</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ceará</td>
      <td>2304400</td>
      <td>Fortaleza</td>
      <td>2020-07-02</td>
      <td>27</td>
      <td>2020</td>
      <td>26.324260</td>
      <td>0.020131</td>
      <td>0.999316</td>
      <td>79.740380</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ceará</td>
      <td>2311801</td>
      <td>Russas</td>
      <td>2020-08-13</td>
      <td>33</td>
      <td>2020</td>
      <td>27.482380</td>
      <td>0.000000</td>
      <td>0.999362</td>
      <td>61.788048</td>
    </tr>
  </tbody>
</table>
</div>



### Análise Exploratória dos Dados

Na **Análise Exploratória dos Dados** realizou-se alguns agrupamentos e visualizacões para uma melhor compreensão do conjunto de dados e, também, investigar as relações entre casos de dengue, temperatura e umidade ao longo do tempo.


```python
# Selecionar as colunas relevantes do DataFrame original
cols = ['uf', 'geocodigo', 'nome_municipio', 'dt_notific', 'se_notif', 'ano_notif', 'temp_med', 'umid_med']

# Agrupar os dados e calcular estatísticas
df_combined = df[cols] \
    .groupby(['uf', 'nome_municipio', 'geocodigo', 'ano_notif', 'se_notif']) \
    .agg(casos_notif=('dt_notific', 'count'),
         temp_med=('temp_med', 'mean'),
         umid_med=('umid_med', 'mean')).reset_index() \
    .sort_values(['ano_notif', 'se_notif'], ascending=[False, False])

```

O código acima realiza uma etapa crucial de pré-processamento, agregando notificações de casos de dengue por semana epidemiológica e ano, calculando métricas climáticas médias e contando o número total de casos em cada semana. Isso prepara os dados para análises posteriores e a construção de modelos de previsão:

1. **Objetivo**:
   - O objetivo principal do projeto de Machine Learning é prever os casos de dengue que ocorrerão na próxima semana com base em informações históricas e variáveis climáticas.
   - Cada linha no conjunto de dados representa um caso de notificação de dengue em um determinado local (geocódigo) e data de notificação (dt_notific). </p>


2. **Seleção de Colunas Relevantes**:
   - No início, é selecionado o subconjunto das colunas do DataFrame original `df`. Essas colunas são consideradas relevantes para a análise e previsão de casos de dengue.
   - As colunas selecionadas incluem:
     - geocodigo: O código que identifica o local
     - nome_municipio: O nome do município
     - dt_notific: A data da notificação
     - se_notif: A semana epidemiológica da notificação
     - ano_notif: O ano da notificação
     - temp_med: A temperatura média
     - umid_med: A umidade relativa média</p>


3. **Agrupamento por Semana Epidemiológica e Ano**:
   - No próximo passo são agrupadas as notificações com base nas colunas geocodigo, se_notif e ano_notif. Isso significa que agregou-se notificações que ocorreram no mesmo local, na mesma semana epidemiológica e no mesmo ano.
   - A função `groupby` é usada para agrupar os dados com base nessas colunas.</p>

4. **Agregação das Variáveis de Interesse**:
   - Agora, o código utiliza a função `agg` para agregar métricas estatísticas das variáveis climáticas (temp_med e umid_med) e também conta o número de notificações em uma semana.
   - Para cada grupo, ele calcula a média das variáveis climáticas e a contagem total de notificações (`casos_notif`).</p>

5. **Ordenação dos Dados**:
   - Após a agregação, os dados são ordenados com base nos anos (`ano_notif`) e semanas epidemiológicas (`se_notif`) em ordem decrescente. Isso permite que os dados sejam organizados de forma temporal, com os registros mais recentes no topo.</p>

6. **Resultado Final**:
   - O resultado final é armazenado no DataFrame `df_combined`.

#### Imprimir o número total de registros e mostrar as primeiras linhas do DataFrame


```python
print('Total de registros: ', len(df_combined), '\n')
df_combined.head()
```

    Total de registros:  62669 
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>uf</th>
      <th>nome_municipio</th>
      <th>geocodigo</th>
      <th>ano_notif</th>
      <th>se_notif</th>
      <th>casos_notif</th>
      <th>temp_med</th>
      <th>umid_med</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3679</th>
      <td>Ceará</td>
      <td>Aracati</td>
      <td>2301109</td>
      <td>2023</td>
      <td>40</td>
      <td>1</td>
      <td>27.781410</td>
      <td>70.681980</td>
    </tr>
    <tr>
      <th>6753</th>
      <td>Ceará</td>
      <td>Barbalha</td>
      <td>2301901</td>
      <td>2023</td>
      <td>40</td>
      <td>2</td>
      <td>27.557560</td>
      <td>40.220620</td>
    </tr>
    <tr>
      <th>8712</th>
      <td>Ceará</td>
      <td>Beberibe</td>
      <td>2302206</td>
      <td>2023</td>
      <td>40</td>
      <td>2</td>
      <td>27.246143</td>
      <td>75.651260</td>
    </tr>
    <tr>
      <th>10231</th>
      <td>Ceará</td>
      <td>Brejo Santo</td>
      <td>2302503</td>
      <td>2023</td>
      <td>40</td>
      <td>1</td>
      <td>29.353947</td>
      <td>38.310005</td>
    </tr>
    <tr>
      <th>13079</th>
      <td>Ceará</td>
      <td>Cariús</td>
      <td>2303303</td>
      <td>2023</td>
      <td>40</td>
      <td>4</td>
      <td>29.976482</td>
      <td>47.771520</td>
    </tr>
  </tbody>
</table>
</div>



---

#### **Municípios com Maior Número de casos**


A seguir, foi efetuado um recorte na série temporal dos dados, concentrando-se no período de 2018 a 2023. O gráfico apresenta os 10 municípios com o maior número de casos de dengue nesse intervalo específico.


```python
# Filtrar dados para o intervalo de 2018 a 2023
df_combined_2018_2023 = df_combined[(df_combined['ano_notif'] >= 2018) & (df_combined['ano_notif'] <= 2023)]
```


```python
# Encontrar o município com o maior número de casos em cada ano.
max_cases_df = df_combined_2018_2023[df_combined_2018_2023['ano_notif'].between(2018, 2023)]  # Filtra para os anos desejados
max_cases_df = max_cases_df.groupby(['ano_notif', 'geocodigo'])['casos_notif'].max().reset_index()
max_cases_df = max_cases_df.sort_values(by=['casos_notif'], ascending=False)

# Filtrar apenas os municípios com mais casos.
top_10_municipios = max_cases_df.head(16)

# Obter os nomes dos municípios correspondentes.
top_10_municipios = top_10_municipios.merge(
    df_combined_2018_2023[['geocodigo', 'nome_municipio']], on='geocodigo', how='left'
)

# Criar o gráfico de barras horizontais.
plt.figure(figsize=(15, 9))
plt.barh(top_10_municipios['nome_municipio'], top_10_municipios['casos_notif'], color='skyblue')
plt.xlabel('Número de Casos')
plt.ylabel('Município')
plt.title('10 Municípios com Maior Número de Casos de Dengue (2018-2023)')
plt.gca().invert_yaxis()  # Inverte o eixo y para que o maior número de casos fique no topo
plt.show()
```


    
![png](output_28_0.png)
    


#### Gráfico de Dispersão dos Casos de Dengue em Relação às Variáveis Climáticas



```python
import matplotlib.pyplot as plt

# Configurar subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico 1: Temperatura Média vs. Casos Notificados
axs[0].scatter(df_combined_2018_2023['temp_med'], df_combined_2018_2023['casos_notif'], alpha=0.5)
axs[0].set_xlabel('Temperatura Média')
axs[0].set_ylabel('Casos de Dengue Notificados')
axs[0].set_title('Relação entre Temperatura e Casos de Dengue')

# Gráfico 2: Umidade Média vs. Casos Notificados
axs[1].scatter(df_combined_2018_2023['umid_med'], df_combined_2018_2023['casos_notif'], alpha=0.5)
axs[1].set_xlabel('Umidade Média')
axs[1].set_ylabel('Casos de Dengue Notificados')
axs[1].set_title('Relação entre Umidade e Casos de Dengue')

# Ajustar layout para evitar sobreposição
plt.tight_layout()

# Exibir os gráficos
plt.show()

```


    
![png](output_30_0.png)
    



```python
# Gráfico de dispersão de casos de dengue e temperatura
plt.figure(figsize=(12, 6))
# sns.color_palette("flare", as_cmap=True
pallete = sns.color_palette("rocket_r", 5, as_cmap=True)
sns.scatterplot(
    data=df_combined.sort_values(by='casos_notif', ascending=True),
       x='se_notif',
       y='temp_med',
       hue='casos_notif',
       palette=pallete,
       size='casos_notif',
       sizes=(20, 200),
       alpha=0.9,
)

# Calcular os quartis da temperatura
Q1 = df_combined['temp_med'].quantile(0.25)
Q3 = df_combined['temp_med'].quantile(0.75)

# Desenhar linhas verticais para dividir os dados em quartis
plt.axhline(Q1, color='grey', linestyle='--', label='Q1')
plt.axhline((Q1 + Q3) / 2, color='grey', linestyle='--', label='Q2 (Mediana)')
plt.axhline(Q3, color='grey', linestyle='--', label='Q3')

# Configurar os rótulos dos quartis
plt.text(df_combined['se_notif'].max() + 1, Q1, 'Q1', color='grey')
plt.text(df_combined['se_notif'].max() + 1, (Q1 + Q3) / 2, 'Q2 (Mediana)', color='grey')
plt.text(df_combined['se_notif'].max() + 1, Q3, 'Q3', color='grey')

plt.xlabel('Semana Epidemiológica')
plt.ylabel('Temperatura Média')
plt.title('Relação entre Casos de Dengue, Semana Epidemiológica e Temperatura')
plt.legend()
plt.show()
# "prism_r",  # Use a paleta personalizada


# Gráfico de dispersão de casos de dengue e temperatura
plt.figure(figsize=(12, 6))
pallete = sns.color_palette("rocket_r", 5, as_cmap=True)
sns.scatterplot(
    data=df_combined.sort_values(by='casos_notif', ascending=True),
    x='se_notif',
    y='umid_med',
    hue='casos_notif',
    palette=pallete,
    size='casos_notif',
    sizes=(20, 200),
    alpha=0.8,
)

# Calcular os quartis da temperatura
Q1 = df_combined['umid_med'].quantile(0.25)
Q3 = df_combined['umid_med'].quantile(0.75)

# Desenhar linhas verticais para dividir os dados em quartis
plt.axhline(Q1, color='grey', linestyle='--', label='Q1')
plt.axhline((Q1 + Q3) / 2, color='grey', linestyle='--', label='Q2 (Mediana)')
plt.axhline(Q3, color='grey', linestyle='--', label='Q3')

# Configurar os rótulos dos quartis
plt.text(df_combined['se_notif'].max() + 1, Q1, 'Q1', color='grey')
plt.text(df_combined['se_notif'].max() + 1, (Q1 + Q3) / 2, 'Q2 (Mediana)', color='grey')
plt.text(df_combined['se_notif'].max() + 1, Q3, 'Q3', color='grey')

plt.xlabel('Semana Epidemiológica')
plt.ylabel('Umidade Média')
plt.title('Relação entre Casos de Dengue, Semana Epidemiológica e Umidade')
plt.legend()
plt.show()
```


    
![png](output_31_0.png)
    



    
![png](output_31_1.png)
    


#### Incidência de Casos Notificados por 100.000 Habitantes em Relação à Temperatura Média e Umidade Média

Os dados foram ajustados para refletir a incidência por 100.000 habitantes, levando em consideração a população total do estado do Ceará, conforme o Censo do IBGE, que abrange os 184 municípios. A visualização busca proporcionar insights sobre como a incidência de casos de dengue varia em relação às condições climáticas, considerando a densidade populacional de cada município.

##### Fórmula Incidência:


\begin{equation}
 \text{Incidência} = \left( \frac{\text{Casos Notificados}}{\text{População Total do Estado}} \right) \times 100000
\end{equation}



O gráfico apresenta uma visualização da incidência de casos notificados de dengue por 100000 habitantes em relação aos níveis de temperatura média e umidade média para os municípios do estado do Ceará. Cada bolha representa um município, onde o tamanho reflete a quantidade de casos notificados, e a cor indica a incidência, indo de tons mais claros a mais escura.


```python
# População total do estado do Ceará Censo 2022
populacao_ceara = 8794957

df_combined_2018_2023 = df_combined.copy()

# Calcular o número de casos notificados por 10000 habitantes em uma nova coluna
df_combined_2018_2023['casos_incid'] = (df_combined_2018_2023['casos_notif'] / populacao_ceara) * 100000
df_combined_2018_2023['log_casos_incid'] = np.log(df_combined_2018_2023['casos_incid'])

# Aplicar a função NaturalBreaks para dividir a variável y em k categorias
y_breaks = mapclassify.NaturalBreaks(df_combined_2018_2023['log_casos_incid'], k=5)

# Adiciona a categoria ao DataFrame
df_combined_2018_2023['incidencia_cat'] = y_breaks.yb

# Ordenar o DataFrame pela incidência
df_combined_2018_2023 = df_combined_2018_2023.sort_values(by='log_casos_incid', ascending=True)

# Calcular a soma total de casos notificados para cada categoria
soma_total = df_combined_2018_2023.groupby(['ano_notif', 'incidencia_cat'])['casos_notif'].sum().reset_index()

colors = ['#228B22', '#FDE725', '#FFA500', '#FF4500', '#8B0000']

cmap = mcolors.ListedColormap(colors)

# Criar uma grade de gráficos (3 linhas, 2 colunas)
fig, axs = plt.subplots(3, 2, figsize=(20, 20), sharey=True)

# Sequência de anos
sequencia_anos = [2018, 2019, 2020, 2021, 2022, 2023]

# Loop pelos anos
for i, ano in enumerate(sequencia_anos):
    df_ano = df_combined_2018_2023[df_combined_2018_2023['ano_notif'] == ano]

    # Calcular a posição na grade (linhas x colunas)
    row = i // 2
    col = i % 2

    # Scatter plot com seaborn e escala logarítmica para o tamanho das bolhas
    scatter = sns.scatterplot(
        x='temp_med',
        y='umid_med',
        hue='incidencia_cat',
        size='log_casos_incid',
        palette=cmap,
        sizes=(20, 300),
        alpha=0.6,
        data=df_ano,
        ax=axs[row, col]
    )

    # Adicionar rótulos das categorias dentro da legenda
    legend_labels = [f'{label:.2f}' for label in y_breaks.bins]
    categorias = ["Incidência muito baixa", "Incidência baixa", "Incidência moderada", "Incidência relativamente alta", "Incidência mais alta"]
    legend_texts = [f'{categorias[i]} - ({int(soma_total[(soma_total["ano_notif"] == ano) & (soma_total["incidencia_cat"] == i)]["casos_notif"].sum()):,}) casos notificados' for i in range(len(y_breaks.bins))]

    # Adicionar a legenda personalizada ao gráfico
    legend_handles = [plt.Line2D([], [], marker='o', color='w', markersize=10, markerfacecolor=cmap(i), alpha=0.8) for i in range(len(legend_labels))]
    scatter.legend(handles=legend_handles, labels=legend_texts, loc='lower left', fontsize='medium')

    axs[row, col].set_xlabel('Temperatura Média')
    axs[row, col].set_title(ano)

# Adicionar rótulos comuns
axs[2, 0].set_ylabel('Umidade Média')
fig.suptitle('Incidência de Casos Notificados por 100k habitantes de 2018 a 2023 \ncom relação à Temperatura Média e Umidade Média')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
```


    
![png](output_37_0.png)
    


---

### Treinando e Testando o Modelo

Realizada a análise exploratória de dados, discutiu-se sobre qual seria a variável dependente (`y`), ou seja, o valor que se deseja predizer através do uso de algoritmos de aprendizado de máquina. Decidiu-se por focar o estudo em predizer o número de casos notificados, representado pela coluna `casos_notif`.

#### O Algoritmo Random Forest

Ao abordar a previsão do número total de casos notificados (casos_notif), escolheu-se o algoritmo Random Forest, amplamente reconhecido para problemas de regressão. Este algoritmo é especialmente eficaz para variáveis contínuas, como no caso deste estudo, onde busca-se prever o valor numérico que representa o total de casos notificados. A escolha do Random Forest para esta tarefa se baseia em sua capacidade comprovada de combinar várias árvores de decisão, resultando em previsões robustas e precisas para variáveis contínuas.

<small>Nota: O Random Forest é um algoritmo amplamente utilizado tanto para tarefas de regressão quanto para classificação. Entretanto, pelo fato de a variável que desejamos predizer com o algoritmo ser contínua (valor numérico representando o total de casos notificados), utilizamos o Random Forest para executar a tarefa de regressão.</small>


#### Particionando os Dados

Aqui é onde selecionou-se os **atributos preditores** (variáveis independentes), aqueles que serão utilizados para encontrar o atributo-alvo (variável dependente), ou seja, o número absoluto de casos notificados de dengue para o Estado do Ceará. Particionou-se os dados com a função `train_test_split` da biblioteca sklearn na proporção **80% para treino** e **20% para teste**, respectivamente.



```python
# Selecionar as colunas relevantes para o modelo
cols = ['ano_notif', 'se_notif', 'casos_notif', 'temp_med', 'umid_med']

# Agregar os dados novamente
df_vis = df_combined[cols].groupby(['ano_notif', 'se_notif']).agg(
    casos_notif=('casos_notif', 'sum'),
    temp_med=('temp_med', 'mean'),
    umid_med=('umid_med', 'mean')).reset_index() \
    .sort_values(['ano_notif', 'se_notif'], ascending=[False, False])

# para gerar o modelo, basta criar uma instância
# da classe RandomForestRegressor da biblioteca sklearn
# Criar os conjuntos de treinamento e teste
X = df_vis[['se_notif', 'ano_notif', 'temp_med', 'umid_med']]
y = df_vis['casos_notif']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

random_forest = RandomForestRegressor(random_state=42)

# Treinando o Modelo com método `fit`
random_forest.fit(X_train, y_train)
```




<style>#sk-container-id-1 {color: black;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>RandomForestRegressor(random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">RandomForestRegressor</label><div class="sk-toggleable__content"><pre>RandomForestRegressor(random_state=42)</pre></div></div></div></div></div>



#### Importância de cada atributo

**feature_importances_** fornece informações sobre a importância relativa de cada recurso (ou variável) no processo de tomada de decisão do modelo. É uma métrica útil para entender quais recursos estão contribuindo mais para a capacidade preditiva do modelo.

Características com importância muito baixa podem ser excluídas do modelo para simplificá-lo, reduzir o overfitting e acelerar o treinamento.


```python
# Obter a importância das características do modelo
feature_importances = random_forest.feature_importances_

# Obter as colunas de características
feature_names = X_train.columns

# Classificar as características por importância
indices = feature_importances.argsort()[::-1]

# Plotar a importância das características
plt.figure(figsize=(10, 6))
plt.title("Importância das Características")
plt.bar(range(X_train.shape[1]), feature_importances[indices], align="center")
plt.xticks(range(X_train.shape[1]), [feature_names[i] for i in indices], rotation=90)
plt.xlabel("Características")
plt.ylabel("Importância")
plt.show()
```


    
![png](output_43_0.png)
    



```python
# Previsão da variável dependente com o conjunto reservado para testes
y_pred = random_forest.predict(X_test)
```

#### Avaliação do Modelo

Definiu-se algumas funções que foram utilizadas para obtenção das métricas (`RMSE` e `R²`)   
como definido nas especificações técnicas. Também utilizou-se o método `score`, o qual retorna o $r^2$, que determina o quanto as variáveis independentes influenciam na variável dependente.

RMSE (Root Mean Square Error): O RMSE é uma métrica que mede a média dos erros quadrados entre as previsões do modelo e os valores reais. Ele fornece uma medida da dispersão dos erros. Quanto menor o valor do RMSE, melhor o modelo está em ajustar-se aos dados.

\begin{equation}
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y-y_j)^2}
\end{equation}


```python
def rmse(y_true, y_pred):
    """Retorna a raiz do erro quadrático médio (RMSE, do inglês Root Mean Squared Error)"""
    return np.sqrt(mean_squared_error(y_true, y_pred))
```

---



R-squared (R²): O R-squared, também conhecido como coeficiente de determinação, é uma métrica que varia de 0 a 1. Ele representa a proporção da variabilidade nos dados que é explicada pelo modelo. Um valor de R² próximo de 1 indica que o modelo explica uma grande parte da variabilidade nos dados, enquanto um valor próximo de 0 significa que o modelo não explica bem os dados.

\begin{equation}
    MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
\end{equation}

\begin{equation}
R^2 = 1 - \frac{MSE_{\text{modelo}}}{MSE_{\text{linha de base}}}
\end{equation}



```python
def r2(y_true, y_pred):
    """Retorna o rsquared"""
    return r2_score(y_true, y_pred)
```

<small>Maiores detalhes sobre as métricas podem ser encontradas no material: [**Machine learning I – Classificação e Regressão**](#Referências-Bibliográficas), página 132.</small>

#### Aplicando as Métricas ao Modelo


Nesta fase, o objetivo principal é medir o desempenho do modelo e determinar quão bem ele está funcionando.  Para obter as métricas (RMSE e MAE), deve-se utilizar o conjunto reservado para testes para obter predições do modelo.




```python
# Calculando RMSE
random_forest_rmse = rmse(y_test, y_pred)

# Calcula o R-squared que  diz o quanto o X determina o y
random_forest_rsquared = r2(y_test, y_pred)

print(f'RMSE: {random_forest_rmse}')
print(f'R-squared: {random_forest_rsquared}')
```

    RMSE: 1131.4160725351978
    R-squared: 0.8868191211237809


#### Análise de Resultados

Aqui sintetizou-se resumidamente os resultados obtidos, evidenciando as conquistas alcançadas com o projeto e indicando limitações, possibilidades e/ou reconsiderações para futuros estudos.

O **RMSE** relativamente baixo e o alto **R²** sugerem que o modelo está fazendo boas previsões e explicando uma grande parte da variabilidade nos dados. Além disso, a análise de importância das variáveis, onde as duas principais variáveis foram `ano_notif` (ano) e `se_notif` (semana epidemológica), reforçam a característica sazonal do vírus.


#### Treinando outros 3 algoritmos de Machine Learning para comparação

Os algoritmos selecionados para comparação com o Random Forest foram:
- Decision Tree
- Gradient Boost
- Ada Boost

#### Decision Tree

Decision Tree (Árvore de Decisão) é um algoritmo que organiza dados em uma estrutura de árvore para fazer previsões, especialmente em tarefas de regressão. Ela divide os dados com base em condições de decisão e fornece previsões nas folhas da árvore. Já o Random Forest (Floresta Aleatória) é uma extensão desse conceito que cria várias árvores de decisão independentes e combina suas previsões para melhorar a precisão e a robustez do modelo, reduzindo o overfitting e aumentando o desempenho geral em tarefas de regressão.

#### Gradient Boosting

O GradientBoost ou Gradient Boosting é um algoritmo de aprendizado de máquina que melhora a precisão das previsões combinando vários modelos de aprendizado fracos, como árvores de decisão simples. Ele funciona construindo sequencialmente novos modelos que corrigem os erros dos modelos anteriores, com foco nas amostras que foram previamente mal previstas. Essa abordagem gradual, impulsionada pelo gradiente, permite a criação de modelos altamente precisos e complexos, tornando-o eficaz em tarefas de classificação e regressão, mas também pode ser sensível a hiperparâmetros e exigir ajustes cuidadosos.

#### Ada Boost

O AdaBoost, ou Adaptive Boosting, é um algoritmo de aprendizado de máquina que melhora a precisão do modelo combinando vários modelos de aprendizado fracos, como classificadores simples. No AdaBoost, cada modelo fraco é atribuído a uma amostra com pesos, de modo que o foco se concentra nas amostras que foram classificadas incorretamente pelos modelos anteriores. Em seguida, ele combina esses modelos fracos ponderados para formar um modelo forte, capaz de fazer previsões precisas. O AdaBoost é especialmente útil em tarefas de classificação, pois pode melhorar o desempenho mesmo em conjuntos de dados complexos e desequilibrados.



```python
# Importamos os algoritmos
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
```

#### Treinando os Modelos

Como anteriormente com o `RandomForestRegressor`, criamos uma instância da classe dos algoritmos, depois treinamos o modelo através do método `fit`, utilizando nossos dados de treino como argumentos. Uma vez que já realizamos este procedimento com o Random Forest, faremos todas as operações com os três algoritmos na célula abaixo:


```python
# Decision Tree
decision_tree = DecisionTreeRegressor(random_state=42)
decision_tree.fit(X_train, y_train)
decision_tree_y_pred = decision_tree.predict(X_test)

# Gradient Boost
gradient_boost = GradientBoostingRegressor(random_state=42)
gradient_boost.fit(X_train, y_train)
gradient_boost_y_pred = gradient_boost.predict(X_test)

# Ada Boost
ada_boost = AdaBoostRegressor(random_state=42)
ada_boost.fit(X_train, y_train)
ada_boost_y_pred = ada_boost.predict(X_test)

# Obtenção das métricas

# Decision Tree
decision_tree_rmse = rmse(y_test, decision_tree_y_pred)
decision_tree_rsquared = r2(y_test, decision_tree_y_pred)

# Gradient Boost
gradient_boost_rmse = rmse(y_test, gradient_boost_y_pred)
gradient_boost_rsquared = r2(y_test, gradient_boost_y_pred)

# Ada Boost
ada_boost_rmse = rmse(y_test, ada_boost_y_pred)
ada_boost_rsquared = r2(y_test, ada_boost_y_pred)

```

#### Comparando Performance dos Algoritmos


```python
# Definiu-se um dataframe com as métricas de cada um
metrics = pd.DataFrame({
    "Random Forest": [random_forest_rmse, random_forest_rsquared],
    "Ada Boost": [ada_boost_rmse, ada_boost_rsquared],
    "Decision Tree": [decision_tree_rmse, decision_tree_rsquared],
    "Gradient Boost": [gradient_boost_rmse, gradient_boost_rsquared],
}, index=["RMSE", "R-Squared"])


# Selecionou-se a linha do RMSE
rmse_metrics = metrics.loc["RMSE"]

# Ordenou-se em ordem descendente
rmse_metrics_sorted = rmse_metrics.sort_values(ascending=False)

# Criou-se o gráfico do RMSE comparando os algoritmos
plt.figure(figsize=(10, 3))
plt.barh(rmse_metrics_sorted.index, rmse_metrics_sorted.values, height=0.4, color='lightcoral', label='RMSE')
plt.xlabel('RMSE')
plt.ylabel('Algoritmo')
plt.title('RMSE (Erro)')
plt.legend(loc='lower right')
plt.show()

# Selecionou-se a linha do R-Squared
rsquared_metrics = metrics.loc["R-Squared"]

# Ordenou-se em ordem ascendente
rsquared_metrics_sorted = rsquared_metrics.sort_values()

# Criou-se o gráfico do R-Squared comparando os algoritmos
plt.figure(figsize=(10, 3))
plt.barh(rsquared_metrics_sorted.index, rsquared_metrics_sorted.values, height=0.4, color='royalblue', label='R-Squared')
plt.xlabel('R-Squared')
plt.ylabel('Algoritmo')
plt.title('R-Squared')
plt.legend(loc='lower right')
plt.show()


metrics.head()
```


    
![png](output_65_0.png)
    



    
![png](output_65_1.png)
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Random Forest</th>
      <th>Ada Boost</th>
      <th>Decision Tree</th>
      <th>Gradient Boost</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>RMSE</th>
      <td>1131.416073</td>
      <td>1740.786893</td>
      <td>1149.596070</td>
      <td>1862.052125</td>
    </tr>
    <tr>
      <th>R-Squared</th>
      <td>0.886819</td>
      <td>0.732071</td>
      <td>0.883153</td>
      <td>0.693442</td>
    </tr>
  </tbody>
</table>
</div>



### Visualização das predições realizadas pelo Random Forest

Como o Random Forest obteve o menor erro (por pouco, comparado ao Decision Tree), criou-se um gráfico comparando as predições do Random Forest para cada semana epidemiológica entre os anos 2018 e 2023.


```python
# Criar um DataFrame com as semanas epidemiológicas de 2018 a 2023
years = [2018] * 52 + [2019] * 52 + [2020] * 52 + [2021] * 52 + [2022] * 52 + [2023] * 52
weeks = list(range(1, 53)) * 6

# Garantir que as listas tenham o mesmo comprimento
if len(years) > len(weeks):
    years = years[:len(weeks)]
elif len(weeks) > len(years):
    weeks = weeks[:len(years)]

# Criar o dataframe com as mesmas características (features) que foram usadas durante o treinamento,
weeks_2018_2023 = pd.DataFrame({'se_notif': weeks, 'ano_notif': years, 'temp_med': 0, 'umid_med': 0 })

# Prever os casos estimados para 2018 a 2023
y_pred_2018_2023 = random_forest.predict(weeks_2018_2023)
weeks_2018_2023['casos_pred'] = y_pred_2018_2023

# Filtrar os casos notificados entre 2018 e 2023
casos_notif_2018_2023 = df_vis[df_vis['ano_notif'].between(2018, 2023)]

# Selecionar colunas relevantes para o dataframe com os casos estimados: weeks_2018_2023
cols =["se_notif",  "ano_notif",  "casos_pred"]

# Mesclar os DataFrames de casos estimados e notificados
merged_2018_2023 = pd.merge(weeks_2018_2023[cols], casos_notif_2018_2023, on=['ano_notif', 'se_notif'], how='left')

```


```python
# Mapear as cores para os anos e os casos estimados
colors = {
    2018: 'rgba(255, 0, 0, 1)',  # Vermelho forte
    'Estimados 2018': 'rgb(205, 97, 85)',  # Vermelho fraco
    2019: 'rgba(255, 165, 0, 1)',  # Laranja forte
    'Estimados 2019': 'rgb(229, 152, 102)',  # Laranja fraco
    2020: 'rgba(0, 128, 0, 1)',  # Verde forte
    'Estimados 2020': 'rgb(130, 224, 170)',  # Verde fraco
    2021: 'rgba(0, 0, 128, 1)',  # Azul forte
    'Estimados 2021': 'rgb(133, 193, 233)',  # Azul fraco
    2022: 'rgba(255, 165, 0, 1)',  # Amarelo forte
    'Estimados 2022': 'rgb(249, 231, 159)',  # Amarelo fraco
    2023: 'rgba(175, 122, 197, 1)',  # Marrom forte
    'Estimados 2023': 'rgb(175, 122, 197)'  # Marrom fraco
}

# Lista para armazenar os gráficos
figs = []

# Configurar o layout de subplots
fig = make_subplots(rows=3, cols=2, subplot_titles=['2018', '2019', '2020', '2021', '2022', '2023'])

# Adicionar cada ano como um gráfico independente
for i, ano in enumerate([2018, 2019, 2020, 2021, 2022, 2023]):
    df_ano = merged_2018_2023[(merged_2018_2023['ano_notif'] == ano) & (merged_2018_2023['se_notif'] <= 52)]

    # Adicionar casos notificados
    trace1 = go.Scatter(x=df_ano['se_notif'], y=df_ano['casos_notif'], mode='lines+markers',
                       name=str(ano) + ' - Notificados',
                       line=dict(color=colors[ano]),
                       text=df_ano["ano_notif"],
                       customdata=df_ano['se_notif'],
                       hovertemplate='Ano: %{text}<br>SE: %{customdata}<br>Casos Notificados: %{y}'"<extra></extra>"
                       )

    # Adicionar casos estimados
    trace2 = go.Scatter(x=df_ano['se_notif'], y=df_ano['casos_pred'].astype(int), mode='lines+markers',
                       name='Preditos ' + str(ano),
                       line=dict(color=colors['Estimados ' + str(ano)]),
                       text=df_ano["ano_notif"],
                       customdata=df_ano['se_notif'],
                       hovertemplate='Ano: %{text}<br>SE: %{customdata}<br>Casos Estimados: %{y}'"<extra></extra>"
                       )

    # Adicionar traces ao subplot correspondente
    fig.add_trace(trace1, row=i // 2 + 1, col=i % 2 + 1)
    fig.add_trace(trace2, row=i // 2 + 1, col=i % 2 + 1)

# Atualizar o layout geral
fig.update_layout(height=900, width=1000, showlegend=True)

# Adicionar rótulos de eixos e título
fig.update_xaxes(title_text='Semana Epidemiológica', tickvals=list(range(1, 53, 10)))
fig.update_yaxes(title_text='Casos', row=2, col=1)
fig.update_layout(title_text="Casos Notificados e Casos Preditos/Esperados nos Últimos 5 Anos no Estado do Ceará",
                  title_x=0.5)

fig.show()

```


        <script type="text/javascript">
        window.PlotlyConfig = {MathJaxConfig: 'local'};
        if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
        if (typeof require !== 'undefined') {
        require.undef("plotly");
        define('plotly', function(require, exports, module) {
            /**
* plotly.js v2.26.0
* Copyright 2012-2023, Plotly, Inc.
* All rights reserved.
* Licensed under the MIT license
*/
/*! For license information please see plotly.min.js.LICENSE.txt */
        });
        require(['plotly'], function(Plotly) {
            window._Plotly = Plotly;
        });
        }
        </script>




<div>                            <div id="54a6c336-40e3-4f7b-bd11-96ac4497d1f8" class="plotly-graph-div" style="height:900px; width:1000px;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("54a6c336-40e3-4f7b-bd11-96ac4497d1f8")) {                    Plotly.newPlot(                        "54a6c336-40e3-4f7b-bd11-96ac4497d1f8",                        [{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Notificados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgba(255, 0, 0, 1)"},"mode":"lines+markers","name":"2018 - Notificados","text":[2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[1100.0,1426.0,1504.0,1498.0,1482.0,1584.0,1145.0,1647.0,1679.0,1671.0,1673.0,1448.0,1466.0,2035.0,1980.0,2078.0,1710.0,1332.0,1351.0,1348.0,1225.0,1043.0,987.0,1033.0,951.0,822.0,533.0,533.0,375.0,293.0,290.0,319.0,311.0,268.0,225.0,198.0,212.0,192.0,205.0,181.0,180.0,148.0,160.0,116.0,160.0,116.0,139.0,133.0,143.0,130.0,142.0,111.0],"type":"scatter","xaxis":"x","yaxis":"y"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Estimados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgb(205, 97, 85)"},"mode":"lines+markers","name":"Preditos 2018","text":[2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0,2018.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[1137,1173,1192,1324,1402,1405,1435,1428,1623,1679,1697,1652,1693,1685,1646,1687,1676,1735,1775,1775,1696,1570,1430,1405,1412,1359,1051,1014,916,953,885,764,729,715,685,576,528,481,430,365,354,327,311,308,310,310,310,304,304,303,300,301],"type":"scatter","xaxis":"x","yaxis":"y"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Notificados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgba(255, 165, 0, 1)"},"mode":"lines+markers","name":"2019 - Notificados","text":[2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[122.0,189.0,241.0,340.0,319.0,434.0,499.0,650.0,614.0,507.0,914.0,881.0,1094.0,1660.0,1993.0,1540.0,1882.0,1618.0,1877.0,1710.0,1601.0,1661.0,1495.0,1379.0,1261.0,1216.0,1047.0,950.0,792.0,724.0,816.0,792.0,691.0,648.0,594.0,533.0,467.0,410.0,373.0,348.0,293.0,225.0,254.0,267.0,274.0,233.0,237.0,220.0,257.0,209.0,202.0,181.0],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Estimados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgb(229, 152, 102)"},"mode":"lines+markers","name":"Preditos 2019","text":[2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0,2019.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[835,902,911,971,1013,1167,1266,1268,1523,1589,1649,1636,1703,1712,1708,1759,1757,1825,1867,1867,1795,1684,1552,1527,1533,1526,1314,1301,1294,1329,1244,1094,1056,1047,987,713,633,553,493,428,404,381,372,369,371,371,372,364,362,358,355,350],"type":"scatter","xaxis":"x2","yaxis":"y2"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Notificados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgba(0, 128, 0, 1)"},"mode":"lines+markers","name":"2020 - Notificados","text":[2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[134.0,308.0,406.0,542.0,646.0,903.0,1140.0,1206.0,1380.0,1725.0,1985.0,1352.0,765.0,1010.0,1091.0,1759.0,1713.0,1944.0,1837.0,1649.0,1492.0,1296.0,1298.0,1122.0,1315.0,1317.0,1362.0,1334.0,1141.0,1174.0,968.0,873.0,789.0,755.0,658.0,534.0,396.0,390.0,370.0,314.0,279.0,246.0,226.0,229.0,249.0,240.0,274.0,253.0,215.0,267.0,247.0,186.0],"type":"scatter","xaxis":"x3","yaxis":"y3"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Estimados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgb(130, 224, 170)"},"mode":"lines+markers","name":"Preditos 2020","text":[2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0,2020.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[797,894,910,994,1062,1203,1316,1319,1593,1707,1744,1705,1771,1779,1778,1829,1823,1895,1935,1933,1866,1751,1619,1598,1610,1612,1400,1398,1358,1410,1296,1145,1105,1084,1045,730,649,572,513,432,409,384,376,373,375,376,376,368,366,363,361,354],"type":"scatter","xaxis":"x3","yaxis":"y3"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Notificados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgba(0, 0, 128, 1)"},"mode":"lines+markers","name":"2021 - Notificados","text":[2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[284.0,577.0,531.0,602.0,816.0,922.0,1063.0,1208.0,1305.0,1514.0,1451.0,1467.0,1418.0,2439.0,2583.0,2907.0,3889.0,4084.0,5332.0,6038.0,6211.0,6422.0,8422.0,8072.0,8116.0,7225.0,7181.0,7189.0,6450.0,5491.0,4821.0,4223.0,3963.0,3508.0,2394.0,2073.0,2197.0,1871.0,1700.0,1434.0,1180.0,1353.0,1223.0,1199.0,1184.0,1050.0,975.0,938.0,959.0,1346.0,841.0,322.0],"type":"scatter","xaxis":"x4","yaxis":"y4"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Estimados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgb(133, 193, 233)"},"mode":"lines+markers","name":"Preditos 2021","text":[2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0,2021.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[761,883,908,982,1099,1236,1538,1543,2282,2739,3111,3837,4388,4576,4978,5313,6132,6612,6973,7149,7219,7140,7061,7159,7130,7015,6555,6303,5656,5090,4079,3597,3133,2801,2227,1618,1603,1472,1282,1141,1017,989,924,890,880,839,834,823,768,747,737,689],"type":"scatter","xaxis":"x4","yaxis":"y4"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Notificados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgba(255, 165, 0, 1)"},"mode":"lines+markers","name":"2022 - Notificados","text":[2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[332.0,706.0,712.0,661.0,1145.0,1648.0,2535.0,3003.0,3035.0,4044.0,4257.0,4487.0,5395.0,6119.0,5936.0,7576.0,8905.0,9485.0,10461.0,11567.0,10884.0,10247.0,10288.0,8042.0,8701.0,7361.0,5883.0,4719.0,4181.0,3532.0,3717.0,2957.0,2657.0,2433.0,1986.0,1599.0,1718.0,1304.0,1023.0,897.0,768.0,744.0,594.0,539.0,693.0,545.0,689.0,603.0,433.0,391.0,341.0,290.0],"type":"scatter","xaxis":"x5","yaxis":"y5"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Estimados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgb(249, 231, 159)"},"mode":"lines+markers","name":"Preditos 2022","text":[2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0,2022.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[788,909,934,1010,1178,1336,1679,1680,2623,3251,3684,4460,5008,5100,5813,6114,7278,7903,8081,8180,8119,8003,7479,7450,7462,7295,6658,6214,5403,4673,3779,3303,2887,2602,2120,1418,1353,1219,1081,990,955,929,910,876,881,871,872,854,786,762,750,741],"type":"scatter","xaxis":"x5","yaxis":"y5"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Notificados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgba(175, 122, 197, 1)"},"mode":"lines+markers","name":"2023 - Notificados","text":[2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[502.0,601.0,613.0,761.0,793.0,962.0,1124.0,1071.0,1918.0,2247.0,2393.0,2439.0,2431.0,1879.0,2305.0,1961.0,1943.0,1793.0,2002.0,1732.0,1796.0,1525.0,1133.0,1487.0,1232.0,1024.0,1036.0,980.0,787.0,725.0,702.0,631.0,529.0,613.0,544.0,423.0,394.0,342.0,254.0,125.0,null,null,null,null,null,null,null,null,null,null,null,null],"type":"scatter","xaxis":"x6","yaxis":"y6"},{"customdata":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"hovertemplate":"Ano: %{text}\u003cbr\u003eSE: %{customdata}\u003cbr\u003eCasos Estimados: %{y}\u003cextra\u003e\u003c\u002fextra\u003e","line":{"color":"rgb(175, 122, 197)"},"mode":"lines+markers","name":"Preditos 2023","text":[2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0,2023.0],"x":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52],"y":[778,894,912,985,1099,1225,1503,1482,1913,2096,2194,2258,2265,2190,2101,2172,2085,2229,2268,2233,2132,1979,1737,1724,1721,1648,1530,1512,1488,1489,1531,1408,1369,1348,1299,1016,967,896,801,774,752,748,758,746,747,755,756,745,703,682,674,665],"type":"scatter","xaxis":"x6","yaxis":"y6"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,0.45],"title":{"text":"Semana Epidemiol\u00f3gica"},"tickvals":[1,11,21,31,41,51]},"yaxis":{"anchor":"x","domain":[0.7777777777777778,1.0]},"xaxis2":{"anchor":"y2","domain":[0.55,1.0],"title":{"text":"Semana Epidemiol\u00f3gica"},"tickvals":[1,11,21,31,41,51]},"yaxis2":{"anchor":"x2","domain":[0.7777777777777778,1.0]},"xaxis3":{"anchor":"y3","domain":[0.0,0.45],"title":{"text":"Semana Epidemiol\u00f3gica"},"tickvals":[1,11,21,31,41,51]},"yaxis3":{"anchor":"x3","domain":[0.3888888888888889,0.6111111111111112],"title":{"text":"Casos"}},"xaxis4":{"anchor":"y4","domain":[0.55,1.0],"title":{"text":"Semana Epidemiol\u00f3gica"},"tickvals":[1,11,21,31,41,51]},"yaxis4":{"anchor":"x4","domain":[0.3888888888888889,0.6111111111111112]},"xaxis5":{"anchor":"y5","domain":[0.0,0.45],"title":{"text":"Semana Epidemiol\u00f3gica"},"tickvals":[1,11,21,31,41,51]},"yaxis5":{"anchor":"x5","domain":[0.0,0.22222222222222224]},"xaxis6":{"anchor":"y6","domain":[0.55,1.0],"title":{"text":"Semana Epidemiol\u00f3gica"},"tickvals":[1,11,21,31,41,51]},"yaxis6":{"anchor":"x6","domain":[0.0,0.22222222222222224]},"annotations":[{"font":{"size":16},"showarrow":false,"text":"2018","x":0.225,"xanchor":"center","xref":"paper","y":1.0,"yanchor":"bottom","yref":"paper"},{"font":{"size":16},"showarrow":false,"text":"2019","x":0.775,"xanchor":"center","xref":"paper","y":1.0,"yanchor":"bottom","yref":"paper"},{"font":{"size":16},"showarrow":false,"text":"2020","x":0.225,"xanchor":"center","xref":"paper","y":0.6111111111111112,"yanchor":"bottom","yref":"paper"},{"font":{"size":16},"showarrow":false,"text":"2021","x":0.775,"xanchor":"center","xref":"paper","y":0.6111111111111112,"yanchor":"bottom","yref":"paper"},{"font":{"size":16},"showarrow":false,"text":"2022","x":0.225,"xanchor":"center","xref":"paper","y":0.22222222222222224,"yanchor":"bottom","yref":"paper"},{"font":{"size":16},"showarrow":false,"text":"2023","x":0.775,"xanchor":"center","xref":"paper","y":0.22222222222222224,"yanchor":"bottom","yref":"paper"}],"height":900,"width":1000,"showlegend":true,"title":{"text":"Casos Notificados e Casos Preditos\u002fEsperados nos \u00daltimos 5 Anos no Estado do Cear\u00e1","x":0.5}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('54a6c336-40e3-4f7b-bd11-96ac4497d1f8');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


---

### Conclusão

#### Explorando Melhorias e Superando Desafios Futuros na Predição

Em suma, a aplicação da técnica de machine learning utilizando o algoritmo Random Forest da biblioteca scikit-learn, revelou-se uma ferramenta eficaz e promissora. Os resultados obtidos sugerem insights valiosos para entender e antecipar padrões sazonais e variações na propagação da dengue. Ao analisar e comparar as previsões obtidas pela ferramenta, observou-se uma consistência notável nos resultados dos anos de 2018, 2019, 2020, 2021, 2022 e 2023, indicando picos, ascensões e declínios da doença muito próximos aos casos notificados. Isso mostra a robustez do modelo Random Forest na abordagem desse desafio de saúde pública. A precisão alcançada nas previsões de longo prazo destaca o potencial dessa abordagem para apoiar estratégias proativas de controle da dengue.

É crucial ressaltar que, embora os resultados sejam encorajadores, o sucesso da aplicação desta ferramenta dependerá de melhorias futuras. Dentro do escopo proposto neste projeto, foi limitado a analisar os dados de maneira ampla, ou seja, sem considerar aspectos específicos de cada município. A consideração cuidadosa de fenômenos naturais e indicadores relacionados é imperativa para fortalecer a pesquisa. Nesse sentido, recomenda-se buscar a orientação de especialistas em Meteorologia e Climatologia, visando adquirir uma compreensão aprofundada do impacto das condições climáticas, especialmente da temperatura, no contexto do estudo. Adicionalmente, a contribuição de profissionais especializados em Entomologia, Ecologia, Ciência Ambiental e Biologia é essencial para um entendimento mais abrangente do comportamento do mosquito em relação ao ambiente proposto. Essa abordagem multidisciplinar garantirá uma análise mais robusta e completa dos fatores que afetam a proliferação do mosquito, aprimorando assim a qualidade e relevância da pesquisa

Em futuros trabalhos, há várias oportunidades para aprimorar o modelo de predição de doenças epidemiológicas. Pode-se investigar como o modelo se comportaria ao ajustar suas variáveis, incluindo ou excluindo novos parâmetros. Além disso, a segmentação dos dados em intervalos temporais distintos, como quinzenais, trimestrais e semestrais, bem como a consideração das variações sazonais relacionadas às estações climáticas. Outra abordagem interessante envolve a inclusão de variáveis meteorológicas adicionais, como sensação térmica, precipitação de chuvas, índices agregados e muito mais. Uma limitação comum nos modelos de previsão de doenças é a complexidade das variáveis relacionadas à disseminação, como a migração entre municípios em regiões metropolitanas, por exemplo. Uma possível abordagem futura é aplicar técnicas de agrupamento para categorizar os dados por municípios, unidades federativa e regionais, permitindo uma análise mais detalhada das tendências epidemiológicas.

Conclui-se, portanto, que a aplicação de modelos de machine learning, como o Random Forest, mostra-se promissora na previsão da incidência de dengue. A contínua pesquisa e aplicação dessas técnicas podem moldar positivamente as estratégias de saúde pública e contribuir para um futuro mais resiliente contra ameaças epidemiológicas.

---

### **Agradecimentos**

Gostaríamos de expressar nossa sincera gratidão a todas as pessoas e instituições que contribuíram para o sucesso deste projeto. Em primeiro lugar, agradecemos à nossa dedicada equipe, cujo comprometimento semanal foi essencial para a realização deste trabalho. A colaboração e o esforço conjunto foram fundamentais para superar desafios e alcançar nossos objetivos.

Um agradecimento especial é devido ao dr. Flávio Codeço Coelho, que não apenas forneceu acesso valioso aos dados utilizados neste estudo, mas também desempenhou um papel crucial ao supervisionar e orientar nosso trabalho. Sua experiência e insights foram inestimáveis para o desenvolvimento deste projeto.

Por último, mas não menos importante, expressamos nossa gratidão ao nosso tutor Alessandro Brassanini, cujo compromisso em compartilhar conhecimento do curso da Uniasselvi foi fundamental para o nosso crescimento acadêmico. Suas orientações e feedbacks foram essenciais para aprimorar nosso entendimento e a qualidade deste trabalho.

A todos os que contribuíram direta ou indiretamente, nosso muito obrigado.

---

### Referências Bibliográficas

1. Nogueira, Rodrigo. **Machine learning I - Classificação e Regressão**. 1ª Edição. Indaial: Centro Universitário Leonardo da Vinci, 2020.

2. Costa, Simone. **Preparação e Análise Exploratória de Dados**. 1ª Edição. Indaial: Centro Universitário Leonardo da Vinci, 2020.

3. Instituto Fio Cruz - [**O mosquito Aedes aegypti faz parte da história e vem se espalhando pelo mundo desde o período das colonizações**](https://www.ioc.fiocruz.br/dengue/textos/longatraje.html)

4. Ministério da Saúde - [**Saúde de A a Z - Dengue**](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/d/dengue)

5. Nações Unidas - [**OMS: Brasil é o país mais afetado em novo surto de dengue nas Américas**](https://news.un.org/pt/story/2023/07/1817882), 21 de Julho de 2023

6. IBGE Instituto Brasileiro de Geografia e Estatística - [População no último censo [2022]](https://cidades.ibge.gov.br/brasil/ce/panorama)

7. [Saúde pública, urbanização e dengue no Brasil - SciELO](https://www.scielo.br/j/sn/a/tRqQNr3nLXBNvqV3MpZGvhP/?lang=pt)



```python

```