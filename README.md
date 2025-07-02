# Description
The aim of this project is to use implement a complete docker stack and and github actions to auto run pipeline test

## Virtual environment

Linux :
```bash
python3 -m venv .venv
```

MacOS-Windows
```bash
python -m venv .venv
```

## Activate Virtual environment :
Windows : 
```bash
.venv\Scripts\activate
```

macOS/Linux : 
```bash
source .venv/bin/activate
```

## Dependencies :

* Make sure you're in the project directory
* Install dependencies : `pip install -r requirements.txt`
* Alternatively, you can install the libraries yourself by reading requierements.txt file

### Structure : 
```
.
├── backend
│   ├── Dockerfile
│   ├── main.py
│   ├── modules
│   │   └── calcul.py
│   ├── requirements.txt
│   └── tests
│       └── test_calcul.py
├── docker-compose.yml
├── frontend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── README.md
```

## Start streamlit (front)
```batch 
streamlit run frontend/app.py
```

or 

```batch 
docker run -p 8501:8501 frontend-app
```


## Start fastAPI (back)
```batch 
uvicorn api:app --host 127.0.0.1 --port 9500 --reload
```
or
```batch 
docker run -p 9500:9500 backend-app
```

## API Swagger
[Documentation de l'api](http://127.0.0.1:9500/docs)


## Build project with docker (back)
```batch
cd backend
docker build -t frontend-app .
```

## Build project with docker (front)
```batch
cd frontend
docker build -t frontend-app .
```

## Run project with docker
```batch
docker compose up --build
```

or 

```batch
docker-compose up --build
```

## Execute test
```batch 
pytest backend/tests/test_calcul.py
```

## Generated containers
[Container back](https://hub.docker.com/repository/docker/thoutin/app-backend/general )
[Container front](https://hub.docker.com/repository/docker/thoutin/app-frontend/general)

## Github actions
[Actions](https://github.com/ThomasHtn/app-docker/actions)


## Pull une image
```batch 
docker pull thoutin/app-backend:aab3e8ff5b340ab116b6b66fe3dd57a216d0b078
```

## Run une image 
```batch
docker images 
docker run <image_id>
```

