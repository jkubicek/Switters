Switters
========

Installation
------------

Switters requires a keybase account. Create an account at http://keybase.io and install the [keybase script](kb). Make sure that you've logged in with `keybase login`.

Switters also requires that you've got the [Java runtime](java). You can test your installation by running `java -version`. If you are running Yosemite (OS X 10.10) and you are seeing "No Java runtime present, requesting install" errors, you may have better luck installing Java from [Apple](apple). 

Once keybase and Java are installed, run `brew install switters` to install the switters client. Before you're able to send messages, you'll need to create an app ID and save the credentials locally. On Twitter's [app pages](td) create a new app. Make sure the app has read and write permissions. From the "Keys and Access Tokens" tab, copy down the consumer key, secret, access token and access token secret. These should be placed in a file located at `~/.swittersconfig`. The file looks like:

    [TwitterConfig]
    consumer_key = <add key here>
    consumer_secret = <add secret here>
    access_token = <add token here>
    access_token_secret = <add secret token here>
	
Sending Messages
----------------

    switters send -u jkubicek -m "Hey there, guy"
    
The `-u` flag should be a Twitter username, the `-m` flag is your message. 

Receiving Messages
------------------

    switters receive tweet_id

`tweet_id` is the id of a message containing an encrypted QR code. Visit the tweet page and copy the ID from the URL. 

[kb]: https://keybase.io/docs/command_line/installation
[td]: https://apps.twitter.com
[java]: http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html
[apple]: http://support.apple.com/kb/DL1572
