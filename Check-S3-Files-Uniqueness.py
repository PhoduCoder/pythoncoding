import json
import boto3
import hashlib

# Initialize the SQS client and the S3 client
sqs = boto3.client('sqs')
s3 = boto3.client('s3')

# Initialize a dictionary to store the input file object keys
input_files = {}

def lambda_handler(event, context):
    # Get the messages from the event
    messages = event['Records']
    
    # Initialize a list to store the output file object keys
    output_files = []
    
    # Process each message in the batch
    for message in messages:
        # Get the S3 bucket and key from the message body
        s3_info = json.loads(message['body'])
        bucket = s3_info['s3']['bucket']['name']
        key = s3_info['s3']['object']['key']
        
        # Check if the message corresponds to an input or output file
        if key.startswith('input/'):
            # Store the input file object key in the dictionary
            input_files[key] = True
        elif key.startswith('output/'):
            # Check if the corresponding input file object key is in the dictionary
            input_key = key.replace('output/', 'input/')
            if input_key in input_files:
                # Calculate the MD5 hash of the input and output files
                input_md5 = get_md5(bucket, input_key)
                output_md5 = get_md5(bucket, key)
                
                # Compare the MD5 hashes and process the files as needed
                if input_md5 == output_md5:
                    print(f"File {input_key} and {key} match!")
                    # TODO: process the matching files as needed
                else:
                    print(f"File {input_key} and {key} don't match!")
                    # TODO: process the non-matching files as needed
            else:
                # Store the output file object key in the list
                output_files.append(key)
        else:
            print(f"Invalid key {key} in message body")
    
    # Check for output files that don't have corresponding input files
    for output_key in output_files:
        input_key = output_key.replace('output/', 'input/')
        if input_key not in input_files:
            print(f"Output file {output_key} has no corresponding input file!")
            # TODO: process the orphaned output file as needed
            
def get_md5(bucket, key):
    # Get the object from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    # Calculate the MD5 hash of the object contents
    md5 = hashlib.md5(response['Body'].read()).hexdigest()
    return md5
