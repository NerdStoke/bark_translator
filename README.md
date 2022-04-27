# bark_translator

## Inspiration
Based on https://github.com/russinnes/py-vox-recorder/blob/master/py-corder-osx.py

## Dependencies
`apt-get install python3-pyaudio python3-numpy libasound2-dev`

## Running

The device needs to be able to start the scripts by itself.  
In order to do that, add the following two lines to the end of `/etc/rc.local`  
```
sudo python3 /home/pi/git/bark_translator/voice.py &
exit 0
```
