# Tripos Bot

Tripos Bot: your weekly math WTF.

## Required Software

This uses `pdflatex` to convert LaTeX to PDF,
and ImageMagick (`convert`) to convert PDF to JPG.

This bot also uses my 
[rainbow mind machine](https://charlesreid1.com:3000/charlesreid1/rainbow-mind-machine)
twitter bot library.

## Turn Latex Into Images

One-time thing: run `pdflatex` and `convert`
on each of the problems in `latex/`:

```
./compile.sh
```

## Tweet A Problem A Day

Run the bot to tweet a problem each day.

```
python3 Tripos.py
```

## How It Works

This uses the Rainbow Mind Machine library,
which is designed to run an arbitrary number
of Twitter Bots, to run a single bot.

This extends the Sheep class defined in Rainbow
Mind Machine (1 sheep = 1 bot) to tweet a photo
once per day.

(The Sheep class defines its own tweet scheduling.)

