CTR MLOPS pipeline
==============================

Пайплайн по предсказанию кликов пользователя для мобильной Web рекламы. За основу взяты данные соревнования Kaggle Avazu CTR Prediction.

**Структура пайплайна**

make_dataset: чтение данных

features/build_transformers: обработки признаков, в которую входят

DeviceCountTransformer, UserCountTransformer: трансформы для расчета количества рекламных объявлений на пользователя или девайс

CtrTransformer: трансформы, с помощью которых кодируем категориальные переменные средним CTR

model_fit_predict: обучаем классическую модель Catboost `а на предсказание вероятности клика для данной сессии пользователя.

**Установка**
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
**Обучение модели**
```
python ctr_project/train_pipeline.py --configs configs/train_config.yaml
```
**Юнит тестирование**
```
pytest
```
**Tools**

DVC : для версионирования данных и артефактов при помощи Git синтаксиса

MLFlow: для логирования экспериментов над моделью.

Удаленное S3 объектное хранилище в VK Cloud

REST сервис в FastAPI

Grafana: инструмент для визуализации метрик

Prometheus: система мониторинга которая собирает метрики у приложения и передает их в Grafana


**Метрики**

predict_proba: значение вероятности клика с каждого предсказания

predicted_proba_hist: гистограмма вероятностей

http_predict_request_total: счетчик входящих запросов на endpoint /predict

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
