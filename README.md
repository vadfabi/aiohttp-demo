Description
--------
Basic REST API service based on aiohttp.


Notable compromises
--------
- [schematics](https://github.com/schematics/schematics) provides serialization but no ORM
- [asyncpg](https://github.com/MagicStack/asyncpg) provides fast, binary, async access to Postgres, but is young and the documentation provides only the basics.
- [ujson](https://github.com/esnme/ultrajson) is very fast but, does not allow for customizing the serialization of unknown types, it just serializes an "unserializable" object to a dict containing each of its properties.


Docker
--------

To build Docker images run:

```
docker build -t aiodemo:latest .
cd docker/db/
docker build -t aiodemodb:latest .
```

To run demo:

```
docker-compose up -d db
docker-compose up -d web
```


Notes
--------

To validate everything is running correctly, we will check the version

First get your docker host machine ip, on mac this is probably found using one of these commands `docker-machine ip` or `dlite ip`.  Then run the following command substituting your ip for the `<docker_host>`

```
curl -H "Authorization: abc123" http://<docker_host>:8080/version
```

Note that for demonstration purposes, all endpoints require token authorization and the token is `abc123`.
