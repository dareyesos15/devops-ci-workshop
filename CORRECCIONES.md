Correcciones.

app.py:

1. se agrego el atributo uptime_seconds para la respuesta del endpoint de /health
2. Se cambia el valor del atributo status en el endpoint / de "ok" a "running" para que coincida con las pruebas unitarias.
3. Se cambia el nombre del endpoint /metric a /metrics para que coincida con las pruebas unitarias