FROM centos:7
RUN yum install -y nano python3 openssl python3-pip libcurl-devel gcc python3-devel
RUN python3 -m pip install --compile --install-option="--with-nss" --no-cache-dir pycurl && python3 -m pip install python-a2s
RUN mkdir /py
ADD py/ /py/
ADD sh/run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]