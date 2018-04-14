# Math Tripos Bot Flock

[math tripos bot on twitter](https://twitter.com/math_tripos)

The Math Tripos Bot Flock is a (singleton) flock of (one) Twitter bots 
tweeting a daily photo of a LaTeX-rendered question from Cambridge 
University's Mathematical Tripos. (Most questions come from G. H. Hardy's
_A Course of Pure Mathematics_.)

`bot/` contains the code for the Math Tripos Bot Flock.

(TODO) `pelican/` contains the Pelican files used to generate 
[the project web page](http://charlesreid1.github.io/math_tripos).

(TODO) See [the project web page](http://charlesreid1.github.io/math_tripos) for more information,
or browse through the code.

## List of Bot Accounts

[@math_tripos](https://twitter.com/math_tripos)

## Required Software

This bot flock utilizes [rainbow-mind-machine](https://github.com/charlesreid1/rainbow-mind-machine),
the extensible bot flock framework authored by yours truly.

This bot also requires LaTeX to render mathematical equations
as images. This should be as simple as `apt-get install latex` 
or some such nonsense.

::sad trombone::

## Required Twitter Setup

You will need to set up some Twitter accounts for your bots, obviously.
Set up a new Gmail account, create a Google Voice number, and use that 
as a phone number if Twitter demands a phone number from you.
(Twilio phone numbers _will not work_ for Twitter registration. Don't blow $1.)

You will also need a bot-master account. This acount will be associated with
your application. You can have one bot-master that runs all of your bot flocks
under the same application, even if they are different flocks running on 
different machines.

You will need to create a Twitter app through the bot-master account.
This will give you a consumer token and a consumer secret token.

**Captain Obvious sez:** you should keep your consumer secret token a secret!

Once you have your consumer token and consumer secret, they go in `bot/apikeys.py`.
This step must be done prior to running the bot.

## Where Do I Put My Keys

Your keys should go in the same directory as
the bot script and (optionally) any data or 
external files used to initialize each bot.

For example:

```
bot/
    MathTriposBot.py
    apikeys.py
    latex/
        ...
    keys/
        math_tripos.json
```

While you can put the keys anywhere you'd like,
this is the recommended layout.

## Where Do I Put My apikeys.py

Your `apikeys.py` containing your consumer token
and consumer secret should be defined like two
Python variables in `apikeys.py`:

```
consumer_token = 'AAAAA'
consumer_secret_token = 'BBBBBBBBBBBBBB'
```

The file `apikey.py` should go next to `MathTriposBot.py`:

```
bot/
    MathTriposBot.py
    apikeys.py
    latex/
        ...
    keys/
        math_tripos.json
```

## Before You Run The Bot Flock

Before running the bot flock, you must compile the latex 
into equation images:

```
cd bot/
cd latex/
./compile.sh
```

## Running The Bot Flock

(Note: take care of `apikeys.py` before you begin.)

Running the bot flock is a two-step process:

1. (One time) Authorize the program to tweet on behalf of your account 
    (i.e., log in with each user account). This requires `apikeys.py` be present
    next to your bot flock program. This step generates key files (JSON format).

2. Run the bot flock. Tweet! Sleep! Repeat!

Either way, run it with Python:

```
$ cd bot/
$ python MathTriposBot.py
```

## Docker

To run the bot flock using docker, use the Dockerfile
contained in this directory to build the container:

```
$ docker build -t triposbotflock .
```

Now you can run the container:

```
$ doker run -d \
    --name stormy_tripos_singleton \
    -v ${PWD}/bot/apikeys.py:/tripos/bot/apikeys.py \
    -v ${PWD}/bot/keys:/tripos/bot/keys \
    -v ${PWD}/bot/latex:/tripos/bot/latex \
    triposbotflock
```

(hopefully that's right, but in any case, just use docker-compose.)

The container should be run interactively the first time through
(add the `-it` flag to docker to make it interactive and give you tty),
so you can set up the keys. The keys will live next to the bot program
and `apikeys.py file`, in a folder called `keys/` containing one json file
per bot account.

This bot also needs 365 LaTeX files (one for each day) and a script
to compile these LaTeX files into images. The directory containing
LaTeX and rendered images is `latex/`. It is bind-mounted into the directory.

On first run, the bot container will detect that there are no keys and 
run the interactive part of the script (Keymaker).

After the keys are set up, the bot container will detect that keys are present
and can run in detached mode.

##  Docker Compose

Running the bot with docker-compose is a three-step process.

The first step is to build the pod (one container).

```
$ docker-compose build
```

If you've made some changes to files copied into the 
container, specify the `--no-cache` flag or it will
continue to use the crusty version:

```
$ docker-compose --no-cache
```

First, to run the container interactively,
modify the docker-compose service `tripos_botflock`
to include `stdin_open: true` and `tty: true`:

```
  stormy_tripos:
    build: . 
    # ---------------
    # Only include these two lines 
    # when setting up API keys. 
    stdin_open: true
    tty: true
    # ---------------
```

Note, if you need an interactive shell, you can
set the entrypoint variable to `/bin/bash`:

```
  stormy_tripos:
    build: . 
    # ---------------
    # fully interactive container
    stdin_open: true
    tty: true
    entrypoint: /bin/bash
    # ---------------
```

This is good for checking whether the container 
is being initialized correctly.

Once those two lines are added to make the container
interactive, run the container using `docker-compose run <service-name>` 
(do not use `up`!):

```
$ docker-compose run stormy_tripos
```

This will run the entrypoint script, install 
rainbow mind machine, and run the interactive 
script.

Note that if you already have most of the keys 
you need in `bot/keys/`, but there's just one 
key that you need to make, you should 
temporarily move `bot/keys/` to, e.g., `bot/_keys/`,
and re-run the above `docker-compose run` command,
to run through the keymaking process.
You can skip the keymaking process for all of the
keys that you already have. When you are finished, 
you can kill that container and merge the two
key directories.

Once the keys are present in the `keys/` directory, 
you can run the bot using `docker-compose up`, 
and optionally use the `-d` flag to detach it:

```
$ docker-compose up -d
```

Use this as a building block to create a
master `docker-compose.yml` running all the 
bot flocks.

## Rebuilding the Docker Container (Debugging)

If you end up doing debugging work,
and changes to files don't seem to have 
any effect, you should probably try 
rebuilding with the `--no-cache` option.

```
docker build --no-cache
```

