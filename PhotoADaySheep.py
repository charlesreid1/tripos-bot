import rainbowmindmachine as rmm
import logging
import glob
from datetime import datetime

class PhotoADaySheep(rmm.Sheep):
    """
    This sheep will tweet a photo a day.

    This overrides Sheep's default
    inner/outer timing loop and tweet behavior,
    but re-uses a lot of other stuff.

    Constructor takes a dictionary of parameters, 
    stored in self.params


    Parameters:

        images_dir: directory containing images


    Collective actions:
    
        image_a_day: tweet an image a day
    """
    def populate_queue(self):
        """
        Load parameters and prepare the tweet queue.

        This is actually just a list of image files, indexed by 
        the day of the year that they should be tweeted out.

        This method is only called by the public tweet() method.
        """
        # The format of this file can be whatever we'd like.
        # 
        # Opening a json file with contents like 
        #   { "1" : "001.png",
        # seems wasteful.
        # Cut to the chase with glob.
        return glob.glob(self.params['images_dir']+"/*.jpg")


    def perform_action(self,action,params):
        """
        Performs action indicated by string (action),
        passing a dictionary of parameters (params)

        Actions:

            image_a_day: tweet an image a day
        """
        rmm.Sheep.perform_action(self,action,params)

        if action=='image_a_day':
            self.image_a_day(params)


    def image_a_day(self,params):
        """
        Tweets an image a day,
        at 8 o'clock or so.

        Parameters:

            upload: boolean, upload media or not

            publish: boolean, publish or not

        """

        # --------------------------
        # Process parameters

        tweet_params = params

        # Default parameter values
        defaults = {}
        defaults['publish'] = False

        # populate missing params with default values
        for dk in defaults.keys():
            if dk not in tweet_params.keys():
                tweet_params[dk] = defaults[dk]


        # --------------------------
        # Start The Calendar

        remcycle = 60*60*2

        prior_dd = 0
        while True:

            try:

                # Repopulate in case there are changes
                twit_images = populate_queue()
        
                yy, mm, dd, hh, mm, _, _ = datetime.now()[0,1,2]

                if(abs(dd-prior_dd)>0 and hh>8):

                    # Index = days since beginning of year
                    index = (datime.now() - datetime(yy,1,1,0,0,0)).days

                    # If there is a photo for this date,
                    if(index < len(twit_images)):

                        # Get photo for this date
                        tweet_params['image_file'] = twit_images[index]

                        img_info = {}

                        # Upload image 
                        if(tweet_params['upload']):
                            img_info = upload_image_to_twitter(tweet_params)

                        if(tweet_params['upload'] and tweet_params['publish']):
                            _tweet(img_info)
                        else:
                            self._print("Testing image tweet: %s"%(tweet_params['image_file']))

                    # Update prior_dd
                    prior_dd = dd

                msg = self.timestamp_message("Boink. Still fully operational.")
                logging.info(msg)

                time.sleep(remcycle)

            except Exception as err:

                # oops!

                msg1 = self.timestamp_message("Sheep encountered an exception. More info:")
                msg2 = self.timestamp_message(traceback.format_exc())
                msg3 = self.timestamp_message("Sheep is continuing...")

                logging.info(msg1)
                logging.info(msg2)
                logging.info(msg3)

                time.sleep(remcycle)

            except AssertionError:
                raise Exception("Error: tweet queue was empty. Check your populate_queue() method definition.")

