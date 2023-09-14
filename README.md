# ML Dengue Predict

This project aims to predict the number of dengue cases using machine learning models based on weather data and epidemiological information.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Notebook](#project-notebook)
- [Data Source](#data-source)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Dengue is a mosquito-borne disease that can have a significant impact on public health. Predicting the number of dengue cases can help healthcare authorities take proactive measures to mitigate outbreaks.

This project uses machine learning techniques to create a predictive model based on historical weather data and epidemiological information. The goal is to forecast the number of dengue cases for specific regions and time periods.

## Installation

To set up this project on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/osl-pocs/ml-dengue-predict.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ml-dengue-predict
   ```

3. Install project dependencies using [Poetry](https://python-poetry.org/). Make sure you have Poetry installed, and then run:

   ```bash
   poetry install
   ```

4. Activate the virtual environment created by Poetry:

   ```bash
   poetry shell
   ```

## Usage

1. Launch Jupyter Lab to open the notebook:

   ```bash
   jupyter lab
   ```

## Project Notebook

The main project details and documentation can be found in the Jupyter Notebook located in the `notebooks` directory:

- **[Project Notebook](https://github.com/osl-pocs/ml-dengue-predict/blob/main/notebooks/Projeto_ML_Dengue_Predict.ipynb)**

The notebook contains comprehensive information about the project, including data preprocessing, model building, and analysis.

## Data Source

This project utilizes data from the INFODENGUE database:

- **[INFODENGUE Data](https://info.dengue.mat.br/datasets/notificacao/20102023/)**

## Contributing

We welcome contributions from the community. If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix: `git checkout -b feature-name`
- Commit your changes and provide descriptive commit messages.
- Push your branch to your fork: `git push origin feature-name`
- Create a Pull Request to the `main` branch of the original repository.

## License

This project is licensed under the ["BSD License"](LICENSE.md).

---

Feel free to customize this README to fit the specific details and needs of your project. Include sections about data sources, model details, and any additional information that would be useful for users and contributors.

