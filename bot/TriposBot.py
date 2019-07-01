import rainbowmindmachine as rmm
import os, glob
import logging

ch = logging.StreamHandler()
logger = logging.getLogger('')
logger.setLevel(logging.INFO)
logger.addHandler(ch)

fh = logging.FileHandler(filename='rmm_tripos.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)

DATADIR = os.path.join(os.getcwd(), 'latex')
KEYSDIR = os.path.join(os.getcwd(), 'keys')

def setup():
    k = rmm.TwitterKeymaker()
    k.set_apikeys_file('apikeys.json')
    k.make_a_key( **{
            'name' : 'math_tripos',
            'json_target' : 'math_tripos.json',
            'keys_out_dir' : KEYSDIR
    })

def run():
    sh = rmm.TwitterShepherd(
            json_keys_dir = KEYSDIR, 
            flock_name = 'math_tripos',
            sheep_class = rmm.PhotoADaySheep
    )


    LIVE = True


    if not LIVE:
        sh.perform_parallel_action(
                'photo_a_day',
                **{
                    'publish' : False,
                    'images_dir' : DATADIR,
                    'images_pattern' : '{i:03}.jpg',
                    'message' : 'Your daily Mathematical Tripos question.'
                }
        )

    else:
        sh.perform_parallel_action(
                'photo_a_day',
                **{
                    'publish' : True,
                    'images_dir' : DATADIR,
                    'images_pattern' : '{i:03}.jpg',
                    'message' : 'Your daily Mathematical Tripos question.'
                }
        )


if __name__=="__main__":

    keys_exists = os.path.isdir(KEYSDIR)
    keys_has_keys = len(glob.glob(os.path.join(KEYSDIR,"*.json"))) > 0
    if( keys_exists and keys_has_keys ):
        print("running bot")
        run()
    else:
        print("setting up bot")
        setup()

