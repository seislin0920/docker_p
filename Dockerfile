# FROM python:3.9
# WORKDIR /python

FROM continuumio/miniconda3
WORKDIR /python
RUN conda install python=3.8 -y && \
    conda clean -afy

CMD ["/bin/bash"]