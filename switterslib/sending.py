import qrcode
import twitter_config
from PIL import Image
from subprocess import check_output
from tempfile import mkdtemp

def send(username, message, dry_run=False, verbose=False):
  print('Searching keybase for Twitter user \"' + username + '\"')
  kb_users_raw = check_output(['keybase', 'search', username]).splitlines()
  
  kb_user = None
  for user in kb_users_raw:
    tokens = user.split()
    kb_username = tokens[1]
    kb_twitter_handle = None
    for token in tokens:
      if token.startswith('twitter:'):
        token = token[8:]
        kb_twitter_handle = token
    if kb_twitter_handle == username:
      kb_user = (kb_username, kb_twitter_handle)
      
  
  if kb_user:
    print 'Found keybase user \"{} - @{}\"'.format(kb_user[0], kb_user[1])
  else:
    print "Could not find a Keybase account for twitter user: " + username
    sys.exit(status=1)
  
  print('Encoding message...')
  enc_message = check_output(['keybase', 'encrypt', '-m', message, username])
  
  if verbose:
  	print('Encoded message:\n{}'.format(enc_message))
  
  print('Creating QR code...')
  qr = qrcode.make(data=enc_message)
  side = qr.pixel_size / 2
  qr.thumbnail((side,side), Image.ANTIALIAS)
  temp_dir = mkdtemp()
  output_file = temp_dir + 'qr.png'
  if verbose:
    print 'Saving QR code file to ' + output_file
  qr.save(temp_dir + 'qr.png', 'PNG')
  
  # Save the image in a tweet
  api = twitter_config.create_twitter_api()
  if verbose:
  	print("Twitter api:\n{}".format(api))
  
  f = open(output_file, 'r')
  kwargs = {'status': '@' + kb_user[1] + ' Here\'s a secret message.\nVisit https://github.com/jkubicek/Switters to decrypt.', 'media[]': f}
  
  if verbose:
  	print("Tweet arguments:\n{}".format(kwargs))
  
  tweet = {'id': 'Not a real tweet'}
  if not dry_run:
    tweet = api.update_status_with_single_media(**kwargs)
    
  print("Sent tweet with ID {}".format(tweet['id']))
  