FROM python:3.11-slim

ADD [https://github.com/google/osv-scanner/releases/download/v1.7.0/osv-scanner_linux_amd64](https://github.com/google/osv-scanner/releases/download/v1.7.0/osv-scanner_linux_amd64) /usr/local/bin/osv-scanner
RUN chmod +x /usr/local/bin/osv-scanner

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]