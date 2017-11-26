FROM brainiak/brainiak

RUN mkdir /rtcloud
COPY . /rtcloud

WORKDIR /rtcloud
RUN python3 -m pip install -e .
RUN python3 -m pip install -e '.[demo]'

# RUN jupyter contrib nbextension install
# RUN jupyter nbextension enable --py widgetsnbextension
# RUN jupyter nbextension enable skip-traceback/main
