# Steps

 1. Write python command line tool
 2. Accept message and twitter handle
 3. Use Twitter handle and keybase to create encrypted message
 4. Use qrcode to create QR Code
 5. Attach image to tweet and @reply user
 
# Accepting a message

 1. Pass in tweet ID
 2. Convert QR code to text
 3. Decrypt text and display
 
# Detailed Steps

## Accept twitter handle

 1. Search keybase for handle
 2. Extract keybase ID
 3. Compose message, assert that the twitter handle matches to keybase base ID
 
# Shit to install
 
    $ pip install tweetpony
    $ pip install qrcode
    
# ZXing

Download and create the .jar files

https://github.com/zxing/zxing

    wget http://zxing.googlecode.com/files/ZXing-1.6.zip
    cd zxing-1.6 
    ant -f core/build.xml
    ant -f javase/build.xml 
    git clone git://github.com/oostendo/python-zxing.git
    cd python-zxing