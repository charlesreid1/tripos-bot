import rainbowmindmachine as rmm
import logging
import glob
from PhotoADaySheep import PhotoADaySheep

def setup():
    k = rmm.SimpleListKeymaker()
    k.make_keys([0],'/home/charles/codes/tripos-bot/keys/')

def run():
    sh = rmm.Shepherd('/home/charles/codes/tripos-bot/keys/',sheep_class=PhotoADaySheep)

    sh.perform_action('photo_a_day',{
                      'upload'  : True,
                      'publish' : True,
                      'images_dir':'latex'
                    })

if __name__=="__main__":
    #setup()
    run()
