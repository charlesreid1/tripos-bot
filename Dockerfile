# see https://git.charlesreid1.com/bots/b-rainbow-mind-machine
FROM rmm_base
MAINTAINER charles@charlesreid1.com

RUN git clone https://github.com/charlesreid1/tripos-bot.git /tripos
WORKDIR "/tripos/bot"
CMD ["/usr/bin/env","python","TriposBot.py"]

