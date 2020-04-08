FROM centos:7
RUN yum install -y nano python3 openssl python3-pip libcurl-devel openssl-devel
RUN python3 -m pip install --install-option="--with-openssl" --install-option="--openssl-dir=/usr/local/opt/openssl" --user pycurl
RUN mkdir /py
ADD py/ /py/
ADD sh/run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]