import sys
import tweetpony
import ConfigParser
from os.path import expanduser, isfile

def print_help_and_exit():
  help_text = '''
  You must setup your Twitter configuration information.
  
  Visit https://apps.twitter.com to create a twitter app with at least Read and Write permissions.
  Under the 'Keys and Access Tokens' tab, get your Consumer Key and Consumer secret.
  
  Generate an access token for your account.
  
  These four keys should be put in ~/.swittersconfig.
  '''
  print(help_text)
  sys.exit(1)

def create_twitter_api():
  
  config_path = expanduser('~/.swittersconfig')
  if isfile(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    key = config.get('TwitterConfig', 'consumer_key')
    secret = config.get('TwitterConfig', 'consumer_secret')
    token = config.get('TwitterConfig', 'access_token')
    token_secret = config.get('TwitterConfig', 'access_token_secret')
    
    if key[:4] == '<add':
      print_help_and_exit()

    api = tweetpony.API(
      consumer_key = key,
      consumer_secret = secret,
      access_token = token,
      access_token_secret = token_secret)
    return api
  else:
    config = ConfigParser.ConfigParser()
    
    config.add_section('TwitterConfig')
    config.set('TwitterConfig', 'consumer_key', '<add key here>')
    config.set('TwitterConfig', 'consumer_secret', '<add secret here>')
    config.set('TwitterConfig', 'access_token', '<add token here>')
    config.set('TwitterConfig', 'access_token_secret', '<add secret token here>')
    
    with open(config_path, 'wb') as configFile:
      config.write(configFile)
      
    print_help_and_exit()
  
if __name__ == "__main__":
  print(create_twitter_api())
  