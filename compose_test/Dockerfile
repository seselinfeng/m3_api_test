FROM python/python3.8.5:v1.0
COPY ../../m3_api_test/ /opt/m3_api_test
WORKDIR /opt/m3_api_test/compose_test/src
RUN pip install -r requirements.txt
CMD ["python","app.py"]
#CMD source /opt/src/start.sh
#CMD ["pytest","-v","-m","/api_test/api/testcases/*"]