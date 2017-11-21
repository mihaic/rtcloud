FROM brainiak/brainiak

RUN mkdir /rtcloud
COPY . /rtcloud

WORKDIR /rtcloud
RUN python3 -m pip install -e .
RUN python3 -m pip install -e '.[demo]'
