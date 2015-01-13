import twitter_config
import urllib
import zxing
from subprocess import check_output
from tempfile import mkdtemp


def receive(tweet_id, verbose=False):
  api = twitter_config.create_twitter_api()
  
  response = api.get_status(id=tweet_id)
  media_url = response['entities']['media'][0]['media_url']
  
  temp_dir = mkdtemp()
  temp_file = temp_dir + '/downloaded_qr.png'
  if verbose:
    print("Downloading attached file to \"" + temp_file + "\"")
  urllib.urlretrieve(media_url, temp_file)
  
  print("Decoding attached image...")
  reader = zxing.BarCodeReader()
  barcode = reader.decode(temp_file)
  
  print("Decrypting message...")
  message = check_output(['keybase', 'decrypt', '-m', barcode.data])
  
  print(message)