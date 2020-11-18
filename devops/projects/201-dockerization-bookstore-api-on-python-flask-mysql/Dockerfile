FROM pypy:3
WORKDIR /usr/src/app
COPY . ./
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "pypy3", "./bookstore-api.py" ]


