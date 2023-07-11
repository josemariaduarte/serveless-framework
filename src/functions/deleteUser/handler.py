import boto3
import json

def delete_user(event, context):
    id = event['pathParameters']['id']
    # Crear una instancia del cliente DynamoDB
    dynamodb = boto3.resource('dynamodb')
    
    # Obtener la tabla de DynamoDB
    table = dynamodb.Table('usersTable')
    
    # Insertar el registro en la tabla
    try:
        table.delete_item(
            Key={ 'pk': id }
        )
    
        # Responder con un mensaje de éxito
        response = {
            'statusCode': 200,
            'body': json.dumps('Registro eliminado exitosamente')
        }
    except Exception as ex:
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error al eliminar el registro: {str(ex)}')
        }
    
    return response
