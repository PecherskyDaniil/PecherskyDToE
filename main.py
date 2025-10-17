import connexion
from connexion.lifecycle import ConnexionResponse
from flask import request,Response
from src.logics.factory_entities import factory_entities
from src.settings_manager import settings_manager
from src.start_service import start_service
from src.reposity import reposity
app = connexion.FlaskApp(__name__)
settings_manager_instance=settings_manager("config.json")
load_result=settings_manager_instance.load()

if not(load_result):
    raise Exception("cant load config file")

start_service_instance=start_service()
start_service_instance.start()

endpoint_to_key={
    "range":reposity.range_key(),
    "range_group":reposity.range_group_key(),
    "unit":reposity.unit_key(),
    "receipt":reposity.receipt_key(),
}

content_types={
    "csv":"text/plain",
    "json":"application/json",
    "xml":"application/xml",
    "markdown":"text/plain"
}


@app.route("/api/accessibility", methods=['GET'])
def formats():
    """
    Проверить доступность REST API
    """
    return "SUCCESS"

@app.route("/api/<model>/format/<format>", methods=['GET'])
def get_model_data(model:str,format:str):
    """
    Проверить доступность REST API
    """
    if format not in content_types.keys():
        return Response(
            status=404,
            response="Format isn't supported",
            content_type="text/plain"
        )

    if model not in endpoint_to_key.keys():
        return Response(
            status=404,
            response=f"There isn't model with name {model}",
            content_type="text/plain"
        )
    try:
        result_format=settings_manager_instance.settings.factory_entity.create(format)()
        result=result_format.create(list(start_service_instance.reposity.data[endpoint_to_key[model]].values()))
        content_type=content_types[format]
        return Response(
            response=result,
            status=200,
            content_type=content_type,
            )
    except:
        return Response(
            response="Server problem",
            status=500,
            content_type="text/plain",
            )

@app.route("/api/<model>/default", methods=['GET'])
def get_model_default_data(model:str):
    """
    Проверить доступность REST API
    """
    if model not in endpoint_to_key.keys():
        return Response(
            status=404,
            response=f"There isn't model with name {model}",
            content_type="text/plain"
        )
    try:
        result_format=settings_manager_instance.settings.factory_entity.create_default()()
        result=result_format.create(list(start_service_instance.reposity.data[endpoint_to_key[model]].values()))
        content_type=content_types[settings_manager_instance.settings.factory_entity.default_value]
        return Response(
            response=result,
            status=200,
            content_type=content_type,
            )
    except:
        return Response(
            response="Server problem",
            status=500,
            content_type="text/plain",
            )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8080)