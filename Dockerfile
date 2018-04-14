#FROM charlesreid1/rainbowmindmachine
FROM rmm_local
MAINTAINER charles@charlesreid1.com

RUN git clone https://git.charlesreid1.com/bots/b-tripos-bot.git /tripos
WORKDIR "/tripos/bot"
CMD ["/usr/bin/env","python","TriposBot.py"]

