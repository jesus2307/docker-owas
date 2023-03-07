# docker-owas
implemtnacion de docker con owaszap

sudo docker cp 8ff8bb771ff7:/zap/cookies.txt cookies.txt

sudo docker run --rm -u zap -p 8095:8095 -v $(pwd):/zap/wrk/:rw -v /ruta/hacia/cookies.txt:/zap/wrk/cookies.txt owasp/zap2docker-stable zap-baseline.py -t http://localhost:3000 -r baseline.html -c cookies.txt -l WARN -s -m 5


sudo docker run --rm -u zap -p 8095:8095 -v $(pwd):/zap/wrk/:rw -v /home/osboxes/Escritorio/porfin/cookies.txt:/zap/wrk/cookies.txt owasp/zap2docker-stable zap-baseline.py -t http://172.17.0.1:3000 -r baseline.html -c cookies.txt -l WARN -s -m 5
