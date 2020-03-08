import boto3
import json

# get AWS credentials
# input: filepath
# output: AWS ID, AWS key

def get_AWS_Credentials(filepath):
	with open(filepath) as f:
		data = json.load(f)
		ACCESS_ID = data["ACCESS_ID"]
		ACCESS_KEY = data["ACCESS_KEY"]
	return ACCESS_ID, ACCESS_KEY

# call AWS to translate text
# input: text to translate (EN), AWS ID, AWS key
# output: translated text (FR)
def translate_AWS(input_text, access_id, access_key):
	translate = boto3.client(service_name ='translate', aws_access_key_id = access_id, 
							aws_secret_access_key = access_key, region_name ='eu-west-2', 
							use_ssl=True)
	result = translate.translate_text(Text=input_text, SourceLanguageCode="en", 
									TargetLanguageCode="fr")
	return result.get('TranslatedText')

def main():
	output = translate_AWS("Hello, my name is John.")
	print(output)
  
if __name__== "__main__":
  main()