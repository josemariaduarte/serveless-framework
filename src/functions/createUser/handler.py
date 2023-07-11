import boto3
import json

def create_user(event, context):
    # Obtener el cuerpo de la solicitud API
    body = json.loads(event['body'])
    print('body %s', body)
    # Obtener los datos del registro a insertar
    id = body['id']
    name = body['name']
    age = body['age']
    
    # Crear una instancia del cliente DynamoDB
    dynamodb = boto3.resource('dynamodb')
    
    # Obtener la tabla de DynamoDB
    table = dynamodb.Table('usersTable')
    
    # Insertar el registro en la tabla
    try:
        table.put_item(
            Item={
                'pk': id,
                'name': name,
                'age': age
            }
        )
    
        # Responder con un mensaje de éxito
        response = {
            'statusCode': 200,
            'body': json.dumps('Registro insertado exitosamente')
        }
    except Exception as ex:
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error al insertar el registro: {str(ex)}')
        }
    
    return response
