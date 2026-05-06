FROM python:3.11-slim

RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*

ADD https://github.com/google/osv-scanner/releases/download/v1.7.0/osv-scanner_linux_amd64 /usr/local/bin/osv-scanner
RUN chmod +x /usr/local/bin/osv-scanner

COPY main.py /main.py

ENTRYPOINT ["python", "/main.py"]