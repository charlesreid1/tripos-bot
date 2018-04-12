FROM charlesreid1/rainbowmindmachine
MAINTAINER charles@charlesreid1.com

RUN git clone https://github.com/charlesreid1/tripos-bot.git /tripos

WORKDIR "/tripos/bot"

CMD ["/usr/bin/env","python","TriposBot.py"]

