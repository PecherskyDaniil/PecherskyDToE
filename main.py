import connexion
import datetime
import json
import os
from connexion.lifecycle import ConnexionResponse
from flask import request,Response
from src.logics.factory_entities import factory_entities
from src.settings_manager import settings_manager
from src.start_service import start_service
from src.reposity import reposity
from src.logics.response_formats import response_formats
import json
app = connexion.FlaskApp(__name__)
settings_manager_instance=settings_manager("config.json")
factory_entity=factory_entities()
load_result=settings_manager_instance.load()
factory_entity.default_value=settings_manager_instance.settings.response_format
if not(load_result):
    raise Exception("cant load config file")

start_service_instance=start_service()
start_service_instance.start()

@app.route("/api/accessibility", methods=['GET'])
def formats():
    """
    Проверить доступность REST API
    """
    return "SUCCESS"

@app.route("/api/<model>/format/<format>", methods=['GET'])
def get_model_data(model:str,format:str):
    """
    Получить модель данных в указанном формате
    """
    if model not in start_service_instance.reposity.data.keys():
        return Response(
            status=404,
            response=f"There isn't model with name {model}",
            content_type="text/plain"
        )
    try:
        result_format=factory_entity.create(format)()
        result=result_format.create(list(start_service_instance.reposity.data[model].values()))
        return Response(
            response=result,
            status=200,
            content_type=result_format.response_type(),
            )
    except Exception as e:
        #raise e
        if str(e)=="Формат не верный":
            return Response(
                status=404,
                response="Format isn't supported",
                content_type="text/plain"
            )
        else:
            return Response(
                response="Server problem",
                status=500,
                content_type="text/plain",
                )

@app.route("/api/<model>/default", methods=['GET'])
def get_model_default_data(model:str):
    """
    Получить модель данных в обычном формате
    """
    if model not in start_service_instance.reposity.data.keys():
        return Response(
            status=404,
            response=f"There isn't model with name {model}",
            content_type="text/plain"
        )
    try:
        result_format=factory_entity.create_default()()
        result=result_format.create(list(start_service_instance.reposity.data[model].values()))
        return Response(
            response=result,
            status=200,
            content_type=result_format.response_type(),
            )
    except Exception as e:
        if str(e)=="Формат не верный":
            return Response(
                status=404,
                response="Format isn't supported",
                content_type="text/plain"
            )
        else:
            return Response(
                response="Server problem",
                status=500,
                content_type="text/plain",
                )


@app.route("/api/get/list/receipt", methods=['GET'])
def get_receipts():
    """
    Получить список рецептов
    """
    result_format=factory_entity.create("json")()
    result=result_format.create(list(start_service_instance.reposity.data["receipt_model"].values()))
    return Response(
        status=200,
        response=result,
        content_type="application/json"
    )

@app.route("/api/get/receipt/<uuid>", methods=['GET'])
def get_receipt(uuid:str):
    """
    Получить рецепт по uuid
    """
    result_format=factory_entity.create("json")()
    receipts=json.loads(result_format.create(list(start_service_instance.reposity.data["receipt_model"].values())))
    result={}
    for obj in receipts["data"]:
        if obj["uuid"]==uuid:
            result=obj
            break
    return Response(
        status=200,
        response=json.dumps(result),
        content_type="application/json"
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8080)