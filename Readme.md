This script works as a telegram bot that receive photo from user, cut out a person or another object( you can setting this using official documentation on pixellib) and send it to a user.
Requirement libraries:
pixellib
tenserflow
------------------------
In config.py you have to insert your bot token.
Also you have to download model 'Mask R-CNN 2.0' for bot on https://github.com/matterport/Mask_RCNN/releases/
And put it in /handlers/recognize
To load script open console, get in the project dir and type: "py bot.py"
