## This container defines a base rainbow mind machine image.
## This base container image is used to build other twitter bots.
FROM rainbowmindmachine/rainbowmindmachine:stable

MAINTAINER charles@charlesreid1.com

RUN git clone https://git.charlesreid1.com/bots/b-tripos.git /tripos
WORKDIR "/tripos/bot"
CMD ["/usr/bin/env","python","TriposBot.py"]

