# docker-owas
implemtnacion de docker con owaszap

# Docker-OWASP

## Instrucciones de uso:

1. Descarga el repositorio de Git en el directorio donde desees instalar la aplicación: 

   ```bash
   git clone <url_del_repositorio>

2. Lanzar el contenedor: 

   ```bash
   sudo docker-compose up -d
3. Copiar el archivo urls.txt al contenedor: 

   ```bash
   sudo docker cp [CONTAINER ID]:/zap/cookies.txt cookies.txt
4. Copiar el archivo del script: 

   ```bash
   sudo docker exec -t [CONTAINER ID] python /zap/script-based-authentication.py

5. Lanzar el script: 

   ```bash
   sudo docker exec -t [CONTAINER ID] zap-baseline.py -t [http://localhost:3000] -g gen.conf -r baseline.html -c cookies.txt -l WARN -s -m 5
   
   import requests

# Leer las URLs del archivo "urlsblack.txt"
with open('urlsblack.txt') as f:
    urls = f.readlines()
urls = [url.strip() for url in urls]

# Agregar cada URL a la blacklist de ZAP
for url in urls:
    api_url = f'http://localhost:8080/JSON/core/view/alertFilters/addAlertFilter/?zapapiformat=JSON&name=Blacklist&rule=1001&enabled=true&urlRegex={url}&urlIsRegex=true'
    response = requests.post(api_url)
    if response.ok:
        print(f'{url} agregado a la blacklist')
    else:
        print(f'Error al agregar {url} a la blacklist')

# Verificar que la blacklist se ha creado correctamente
api_url = 'http://localhost:8080/JSON/core/view/alertFilters/listAlertFilters/?zapapiformat=JSON'
response = requests.get(api_url)
if response.ok:
    filters = response.json()['alertFilters']
    for filter in filters:
        if filter['name'] == 'Blacklist':
            print(f'Blacklist creada correctamente con {len(filter["urlRegexes"])} URLs')
else:
    print('Error al obtener las reglas de filtrado de alertas')

### Nota: Asegúrate de reemplazar <url_del_repositorio> con la URL real del repositorio de Git y [CONTAINER ID] con el ID de tu contenedor Docker. Además, verifica que [http://localhost:3000] sea la URL correcta de tu aplicación.




#### Créditos

El código utilizado en este ejemplo está basado en el repositorio de <a href="https://github.com/jesus2307?tab=repositories">@jesus2307</a>.
-----------------------------------------------------------------------------------------------------------------------------------------------

otros comandos de posible utilidad 
sudo docker run --rm -u zap -p 8095:8095 -v $(pwd):/zap/wrk/:rw -v /ruta/hacia/cookies.txt:/zap/wrk/cookies.txt owasp/zap2docker-stable zap-baseline.py -t http://localhost:3000 -r baseline.html -c cookies.txt -l WARN -s -m 5
sudo docker run --rm -u zap -p 8095:8095 -v $(pwd):/zap/wrk/:rw -v /home/osboxes/Escritorio/porfin/cookies.txt:/zap/wrk/cookies.txt owasp/zap2docker-stable zap-baseline.py -t http://172.17.0.1:3000 -r baseline.html -c cookies.txt -l WARN -s -m 5
