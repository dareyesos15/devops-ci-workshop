Correcciones.

app.py:

1. se agrego el atributo uptime_seconds para la respuesta del endpoint de /health
2. Se cambia el valor del atributo status en el endpoint / de "ok" a "running" para que coincida con las pruebas unitarias.
3. Se cambia el nombre del endpoint /metric a /metrics para que coincida con las pruebas unitarias


4. Se cambia el puerto de 5001 a 5000, ya que en el Dockerfile expone 5000

Dockerfile:
1. Se agrega -slim a la version de python, convirtiendola en una imagen mas pequeña
2. Se agrega --no-cache-dir para evitar el cacheo de paquetes

docker-compose.yml:
1. Se corrige el puerto que se expone, pasa de 5000:5001 a 5000:5000

prometheus.yml:
1. Se cambia en el targets de localhots a api, por el nombre aplicado en docker-compose.yml
2. Se corrige metric por metrics 