FROM owasp/zap2docker-stable 
USER root
# Instala las dependencias necesarias para el script de autenticación
RUN apt-get update && \
apt-get -y install python3 python3-pip && \
pip install requests && \
pip install selenium && \
#apt-get install -y firefox && \
#wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
#tar -C /opt -xzf /tmp/geckodriver.tar.gz && \
#chmod 755 /opt/geckodriver && \
#ln -fs /opt/geckodriver /usr/bin/geckodriver && \
#rm /tmp/geckodriver.tar.gz
rm -rf /var/lib/apt/lists/* 
# Copia el script de autenticación al contenedor
COPY script-based-authentication.py /zap/ 
# Copia el archivo con el árbol de URLs al contenedor
COPY urls.txt /zap/ 
# Define el punto de entrada del contenedor
#ENTRYPOINT ["/docker-entrypoint.s
