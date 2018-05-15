## This container defines a base rainbow mind machine image.
## This base container image is used to build other twitter bots.
FROM rainbowmindmachine/rainbowmindmachine:latest

####################################################
## remove this once rainbow mind machine is okay
#FROM jfloff/alpine-python:recent-onbuild
#
#COPY ./requirements.txt /requirements.txt
#
#RUN git clone https://git.charlesreid1.com/bots/b-rainbow-mind-machine.git /rmm
#RUN cd /rmm && \
#    /usr/bin/env python /rmm/setup.py build && \
#    /usr/bin/env python /rmm/setup.py install
####################################################

MAINTAINER charles@charlesreid1.com

RUN git clone https://git.charlesreid1.com/bots/b-tripos.git /tripos
WORKDIR "/tripos/bot"
CMD ["/usr/bin/env","python","TriposBot.py"]

