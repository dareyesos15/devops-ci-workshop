# Correcciones

**Integrantes:**
- David Reyes
- Isabela Mesa

## Error 1
- **Archivo:** app.py
- **Problema:** El endpoint `/health` no incluia el campo `uptime_seconds` esperado por las pruebas.
- **Solucion:** Se agrego `uptime_seconds` en la respuesta JSON del endpoint `/health`.

## Error 2
- **Archivo:** app.py
- **Problema:** El endpoint `/` devolvia `status: "ok"`, pero las pruebas esperaban `status: "running"`.
- **Solucion:** Se cambio el valor de `status` de `"ok"` a `"running"`.

## Error 3
- **Archivo:** app.py
- **Problema:** La ruta estaba definida como `/metric` y las pruebas consumian `/metrics`.
- **Solucion:** Se cambio la ruta a `/metrics` para que coincidiera con el contrato esperado.

## Error 4
- **Archivo:** app.py
- **Problema:** La aplicacion corria en el puerto `5001`, pero el despliegue y consumo esperaban el puerto `5000`.
- **Solucion:** Se actualizo el puerto de ejecucion de la app a `5000`.

## Error 5
- **Archivo:** Dockerfile
- **Problema:** La imagen base `python:3.11` era funcional pero mas pesada de lo necesario.
- **Solucion:** Se cambio a `python:3.11-slim` para reducir el tamano de la imagen.

## Error 6
- **Archivo:** Dockerfile
- **Problema:** La instalacion de dependencias almacenaba cache de `pip`, aumentando tamano de la imagen.
- **Solucion:** Se agrego la bandera `--no-cache-dir` en la instalacion de dependencias.

## Error 7
- **Archivo:** docker-compose.yml
- **Problema:** El mapeo de puertos estaba como `5000:5001`, generando inconsistencia con el puerto final de la API.
- **Solucion:** Se corrigio el mapeo a `5000:5000`.

## Error 8
- **Archivo:** prometheus.yml
- **Problema:** El target estaba en `localhost`, pero en Docker Compose debe usarse el nombre del servicio.
- **Solucion:** Se cambio el target a `api`.

## Error 9
- **Archivo:** prometheus.yml
- **Problema:** La ruta configurada era `/metric` en lugar de `/metrics`.
- **Solucion:** Se actualizo la ruta a `/metrics`.