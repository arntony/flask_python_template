FROM centos

# Python installation required the GCC compiler on your system
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel wget make git && \
    RUN cd /usr/src  && \
    wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz && \
    tar xzf Python-3.7.4.tgz && cd Python-3.7.4 && ./configure --enable-optimizations && make altinstall && \
    cd .. && rm Python-3.7.4.tgz && \
    git clone https://github.com/arntony/flask_python_template.git && \
    PYTHONPATH="${PYTHONPATH}:/usr/src/flask_python_template/src" && \
    export PYTHONPATH && \
    source ~/.bashrc && \
    pip3.7 install -r flask_python_template/src/requirements.txt

EXPOSE 8080
ENTRYPOINT ["python3.7", "flask_python_template/src/run_application.py"]