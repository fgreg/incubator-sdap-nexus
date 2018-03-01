# Run example: docker run -it --net=host -p 8083:8083 -e MASTER=mesos://127.0.0.1:5050 nexus-webapp

FROM nexusjpl/spark-mesos-base

MAINTAINER Joseph Jacob "Joseph.Jacob@jpl.nasa.gov"

# Set environment variables.

ENV MASTER=local[1] \
    SPARK_LOCAL_IP=nexus-webapp

# Run NEXUS webapp.

EXPOSE 8083

WORKDIR /tmp

COPY docker-entrypoint.sh /tmp/docker-entrypoint.sh

RUN rm -rf /nexus/analysis
COPY data-access /nexus/data-access
COPY analysis /nexus/analysis
COPY nexusproto.tar.gz /nexus/nexusproto/nexusproto.tar.gz

WORKDIR /nexus/nexusproto
RUN pip install nexusproto.tar.gz --force --ignore-installed

WORKDIR /nexus/data-access
RUN python setup.py install

WORKDIR /nexus/analysis
RUN python setup.py install




ENTRYPOINT ["/tmp/docker-entrypoint.sh"]
