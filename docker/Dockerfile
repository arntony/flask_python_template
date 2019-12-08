FROM centos

# Python installation required the GCC compiler on your system
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel wget make
# cmake automake autoconf

# Download and install Python 3.7
RUN cd /usr/src
RUN wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
RUN tar xzf Python-3.7.4.tgz
RUN cd Python-3.7.4 && ./configure --enable-optimizations && make altinstall
RUN cd ..
RUN rm Python-3.7.4.tgz

# install git and clone git repo
RUN yum install -y git && git clone https://github.com/arntony/flask_python_template.git

# set PYTHONPATH
RUN PYTHONPATH="${PYTHONPATH}:/usr/src/flask_python_template/src" && \
    export PYTHONPATH && \
    source ~/.bashrc

# install requirements
RUN pip3.7 install -r flask_python_template/src/requirements.txt
RUN echo pwd
EXPOSE 8080
ENTRYPOINT ["python3.7", "/usr/src/flask_python_template/src/run_application.py"]