FROM python:3.11.5 

#setuo Linux packages
RUN python -m venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#install dependency
RUN apt-get update && apt-get install -y \
    #for postgres
    libpq-dev \
    #for Pillow
    libjpeg-dev \
    #for carioSVG
    libcairo2 \
    #other
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Create the mini vm's code directory
RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt

COPY ./src /code

RUN pip install -r /tmp/requirements.txt

RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "gunicorn \${PROJ_NAME}:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind \"[::]:\${RUN_PORT}\"\n" >> ./paracord_runner.sh


COPY ./boot/docker-run.sh /opt/run.sh
RUN chmod +x /opt/run.sh
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

CMD ["/opt/run.sh"]

