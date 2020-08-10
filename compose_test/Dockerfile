FROM python/python3.8.5:v1.0
COPY src/ /opt/src
WORKDIR /opt/src
RUN pip install -r requirements.txt
#CMD ["python","app.py"]
#CMD source /opt/src/start.sh
CMD ["pytest","-v","-m","/api_test/api/testcases/*"]