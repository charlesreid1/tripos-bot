import rainbowmindmachine as rmm
import logging
import glob
from PhotoADaySheep import PhotoADaySheep

LOG_FILE = "tripos_bot.log"

def setup():
    k = rmm.SimpleListKeymaker()
    k.make_keys([0],'keys/')

def run():
    sh = rmm.Shepherd('keys/',sheep_class=PhotoADaySheep)

    sh.perform_action('photo_a_day',{
                        'publish':False,
                        'images_dir':'latex'
                    })

if __name__=="__main__":

    #setup()

    run()
