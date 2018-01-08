import rainbowmindmachine as rmm
import logging

LOG_FILE = "tripos_bot.log"

def setup():
    k = rmm.TxtKeymaker()
    k.make_keys('/Users/charles/codes/bots/tripos-bot/bot/data/','/Users/charles/codes/bots/tripos-bot/bot/keys/')
    
def run():
    sh = rmm.Shepherd('/Users/charles/codes/bots/tripos-bot/bot/keys/',sheep_class=rmm.QueneauSheep)

    #sh.perform_action('tweet',{'publish':False})
    sh.perform_pool_action('tweet',{
            'publish' : True,
            'inner_sleep' : 3*60,
            'outer_sleep' : 2*3600
        })

if __name__=="__main__":
    setup()
    #run()

