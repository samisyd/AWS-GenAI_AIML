import boto3
import json
import urllib.parse


# FIX 1: Added region_name to all clients
rekognition = boto3.client('rekognition', region_name='us-east-2')
polly = boto3.client('polly', region_name='us-east-2')
s3 = boto3.client('s3', region_name='us-east-2')


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    image_key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key']
    )


    # Step 1: Call Rekognition to detect labels
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': image_key
            }
        },
        MaxLabels=5,
        MinConfidence=80
    )
    # Step 2: Convert detections to a spoken sentence
    description = generate_description(response)


    # Step 3: Call Polly to convert text to speech
    audio = polly.synthesize_speech(
        Text=description,
        OutputFormat='mp3',
        VoiceId='Joanna'
    )


    # Step 4: Save the MP3 audio to the output bucket
    # FIX 2: Correct output bucket name
    audio_key = image_key.replace('.jpg', '.mp3')
    s3.put_object(
        Bucket='rekognition-output-audio-274285228998-us-east-2-an', #change your bucket name here 
        Key=audio_key,
        Body=audio['AudioStream'].read(),
        ContentType='audio/mpeg'
    )


    return {
        'statusCode': 200,
        'body': json.dumps(f'Audio saved: {audio_key}')  # FIX 3: Shows exact file saved
    }


def generate_description(rekognition_response):
    labels = rekognition_response['Labels']
    if not labels:
        return "I could not identify any objects in this image."
    sentence = "I can see the following items. "
    for label in labels:
        sentence += f"{label['Name']}, "
    return sentence
