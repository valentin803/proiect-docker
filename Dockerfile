FROM ubuntu:22.04

# Setează modul non-interactiv pentru a nu bloca instalarea pachetelor
ENV DEBIAN_FRONTEND=noninteractive

# Rulează update-ul ignorând erorile de semnătură GPG și instalează Python
RUN apt-get update --allow-insecure-repositories && \
    apt-get install -y --allow-unauthenticated python3 python3-pip

WORKDIR /app

COPY . /app

RUN pip3 install flask

EXPOSE 5000

CMD ["python3", "app.py"]