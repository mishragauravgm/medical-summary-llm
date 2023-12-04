import json
import boto3

ENDPOINT = ''
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    # TODO implement
    query_params = event['queryStringParameters']
    query = query_params.get('query')
    
    payload = {
    "input":query,
    "parameters":{
        "do_sample":True,
        "top_p":0.7,
        "temperature":0.3,
        "top_k":50
        }
    } 
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType ='application/json', Body=json.dumps(payload))
    prediction = json.loads(response['Body'].read().decode('utf-8'))
    summary = predictiom[0]['generated_text']

    return {
        'statusCode': 200,
        'body': json.dumps(summary)
    }

