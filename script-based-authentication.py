import os
import requests
import http.cookiejar

# Definir credenciales de inicio de sesión
username = 'prueba@123'
password = '12345'

# Definir la URL de inicio de sesión y las URL a las que deseas acceder después de iniciar sesión
login_url = 'http://172.17.0.1:3000/#/login'
target_url = 'http://172.17.0.1:3000/#/search'

# Iniciar sesión en la aplicación web y guardar las cookies en un archivo
session = requests.Session()
login_data = {'username': username, 'password': password}
response = session.post(login_url, data=login_data)
cookie_jar = http.cookiejar.MozillaCookieJar('cookies.txt')
for cookie in session.cookies:
    cookie_jar.set_cookie(cookie)
cookie_jar.save()
print('Inicio de sesión exitoso')

# Acceder a la URL restringida usando las cookies guardadas
session = requests.Session()
cookie_jar = http.cookiejar.MozillaCookieJar()
cookie_jar.load('cookies.txt', ignore_discard=True, ignore_expires=True)
for cookie in cookie_jar:
    session.cookies.set_cookie(cookie)
response = session.get(target_url)
print(response.text)

# Mover cookies.txt a la ruta /zap/wrk/
if not os.path.exists('/zap/wrk/'):
    os.makedirs('/zap/wrk/')
os.rename('cookies.txt', '/zap/wrk/cookies.txt')
print('Cookies guardadas en la ruta /zap/wrk/.')
