# python-elastic-ingest

## Installation

### ELK

```
docker-compose up
```

```
curl -X GET "localhost:9200/_cat/nodes?v&pretty"
```

http://localhost:5601

Setup taken from https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-docker.html

### Django

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

```
./manage.py loaddata fixtures/user.json
./manage.py loaddate fixtures/sales.json
```

Superuser `root` with password `root`.


```
cd core
python manage.py runserver
```

http://localhost:8000


## Dev
```
python manage.py search_index --rebuild
```