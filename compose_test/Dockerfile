FROM python/python3.8.5:v1.0
COPY src/ /opt/src
WORKDIR /opt/src
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
CMD ["python","app.py"]
#CMD source /opt/src/start.sh
#CMD ["python","-m","pytest","-v","/api_test/api/testcases/*","--alluredir=./result"]