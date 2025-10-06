FROM python:3.11-slim-trixie



RUN pip install Twisted && \
    pip install Flask&& \
    pip install requests && \
    pip install pyOpenSSL
    


COPY ./sslstrip/ /app/sslstrip/

COPY ./webinterface/ /var/www/html/


WORKDIR /app/sslstrip/


RUN mkdir -p log && \ 
    touch mylog.log


CMD python3 /var/www/html/flaskserver.py & python3 sslstrip.py 

