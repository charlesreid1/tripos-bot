import rainbowmindmachine as rmm
import os, glob

DATADIR = os.path.join(os.getcwd(), 'latex')
KEYSDIR = os.path.join(os.getcwd(), 'keys')

def setup():
    k = rmm.Keymaker()
    k.make_keys([0], KEYSDIR) # the "item" for our only bot is 0

def run():
    sh = rmm.Shepherd(KEYSDIR, 
                      flock_name = 'math_tripos',
                      sheep_class = rmm.PhotoADaySheep)


    LIVE = False


    if not LIVE:
        sh.perform_pool_action('tweet',{
                      'upload'  : False,
                      'publish' : False,
                      'images_dir' : DATADIR,
                      'images_template' : '{i}.jpg'
        })

    else:
        sh.perform_pool_action('tweet',{
                      'upload'  : True,
                      'publish' : True,
                      'images_dir' : DATADIR,
                      'images_template' : '{i}.jpg'
        })


if __name__=="__main__":

    keys_exists = os.path.isdir(KEYSDIR)
    keys_has_keys = len(glob.glob(os.path.join(KEYSDIR,"*.json"))) > 0
    if( keys_exists and keys_has_keys ):
        print("running bot")
        run()
    else:
        print("setting up bot")
        setup()

