import boto3
import json

def update_user(event, context):
    # Obtener el cuerpo de la solicitud API
    body = json.loads(event['body'])

    print("body %s" % body)
    
    # Obtener los datos del registro a actualizar
    id = event['pathParameters']['id']
    
    # Crear una instancia del cliente DynamoDB
    dynamodb = boto3.resource('dynamodb')
    
    # Obtener la tabla de DynamoDB
    table = dynamodb.Table('usersTable')
    
    try:
        # Actualizar el registro en la tabla
        response = table.update_item(
            Key={
                'pk': id
            },
            UpdateExpression= "set #name = :name, #age = :age",
            ExpressionAttributeNames = {
                "#name":"name",
                "#age": "age"
            },
            ExpressionAttributeValues = { 
                ":name": body['name'], 
                ":age": body['age'] 
            }
        )
        
        # Responder con un mensaje de éxito
        response = {
            'statusCode': 200,
            'body': json.dumps('Registro actualizado exitosamente')
        }
    except Exception as e:
        # Manejar el error de DynamoDB
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error al actualizar el registro: {str(e)}')
        }
    
    return response
