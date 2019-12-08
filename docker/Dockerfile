FROM centos

# Python installation required the GCC compiler on your system
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel

# Install wget, tar
RUN yum install -y wget
RUN yum install -y make

# Download Python 3.7
RUN cd /usr/src
RUN wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
RUN tar xzf Python-3.7.4.tgz

# Install Python 3.7
RUN cd Python-3.7.4
RUN ./configure --enable-optimizations
RUN make altinstall

# remove downloaded source archive file from system
RUN rm /usr/src/Python-3.7.4.tgz
RUN cd ..

# install git
RUN yum -y install git

# clone git repo
RUN git clone https://github.com/arntony/flask_python_template.git

# set PYTHONPATH
RUN PYTHONPATH="${PYTHONPATH}:/usr/src/flask_python_template/src"
RUN export PYTHONPATH
RUN source ~/.bashrc

# install requirements
RUN pip install -r flask_python_template/src/requirements.txt
EXPOSE 8080
ENTRYPOINT ["python3.7", "/usr/src/flask_python_template/src/run_application.py"]