import requests
import pickle
# Definir credenciales de inicio de sesión
username = 'prueba@123'
password = '12345'
# Definir la URL de inicio de sesión y las URL a las que deseas acceder después de iniciar sesión
login_url = 'http://172.17.0.1:3000/#/login'
target_url = 'http://172.17.0.1:3000/#/search'
# Iniciar sesión en la aplicación web y guardar las cookies en un archivo
with requests.Session() as session:
    login_data = {'username': username, 'password': password}
    response = session.post(login_url, data=login_data)
    with open('cookies.txt', 'wb') as f:
        pickle.dump(session.cookies, f)
    print('Inicio de sesión exitoso')
# Acceder a la URL restringida usando las cookies guardadas
with requests.Session() as session:
    with open('cookies.txt', 'rb') as f:
        cookies = pickle.load(f)
        session.cookies.update(cookies)
    response = session.get(target_url)
    print(response.text)
