FROM python:3.6.5-stretch

ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

### python install for machine learning
# add repo
RUN echo deb http://ftp.de.debian.org/debian testing main >> /etc/apt/sources.list
# mecab install
RUN apt-get update \
    && apt-get install -y mecab \
       libmecab-dev \
       mecab-ipadic-utf8 \
       libicu-dev
# add liblary
RUN pip3 install --upgrade pip \
    && pip install scikit-learn \
    numpy \
    pandas \
    matplotlib \
    scipy \
    mecab-python3 \
    polyglot \
    pyicu \
    pycld2 \
    morfessor

WORKDIR /ml-dev

COPY . .

EXPOSE 3000
