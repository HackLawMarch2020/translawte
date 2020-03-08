import boto3
import json

def get_Credentials(filename):
	with open(filename) as json_file:
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
	return ACCESS_ID, ACCESS_KEY

# call AWS to translate text
def translate_AWS(input_text):
	translate = boto3.client(service_name='translate', aws_access_key_id=ACCESS_ID, aws_secret_access_key= ACCESS_KEY, region_name='eu-west-2', use_ssl=True)
	result = translate.translate_text(Text="Hello, World", 
	            SourceLanguageCode="en", TargetLanguageCode="fr")
	print('TranslatedText: ' + result.get('TranslatedText'))
	print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
	print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))



def main():
  print("Hello World!")
  
if __name__== "__main__":
  main()