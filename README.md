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


### Django

```
virtualenv --python=python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

```
./manage.py migrate
./manage.py loaddata fixtures/user.json
./manage.py loaddata fixtures/sales.json
./manage.py loaddata fixtures/channels.json
./manage.py loaddata fixtures/products.json
./manage.py loaddata fixtures/entities.json
```

Superuser `root` with password `root`.


```
cd core
python manage.py runserver
```

http://localhost:8000

```
python make-salesperformance.py
```

## Dev
```
python manage.py search_index --rebuild
```

# References

A lot of good ideas stolen from Nik Tomazic' amazing tutorial https://testdriven.io/blog/django-drf-elasticsearch/

Elasticsearch setup taken from https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-docker.html