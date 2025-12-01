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
from src.models.transaction_model import transaction_model
from src.dto.filter_dto import filter_dto
from src.dto.storage_dto import storage_dto
from src.dto.range_dto import range_dto
from src.dto.range_group_dto import range_group_dto
from src.dto.transaction_dto import transaction_dto
from src.dto.receipt_dto import receipt_dto
from src.dto.unit_dto import unit_dto
from src.core.prototype import prototype
from src.models.range_group_model import range_group_model
from src.models.range_model import range_model
from src.models.receipt_model import receipt_model
from src.models.storage_model import storage_model
from src.models.transaction_model import transaction_model
from src.models.unit_model import unit_model
from src.core.reposity_keys import reposity_keys
from src.logics.reference_service import reference_service
import datetime
import json
app = connexion.FlaskApp(__name__)
settings_manager_instance=settings_manager("config.json")
factory_entity=factory_entities()
load_result=settings_manager_instance.load()
factory_entity.default_value=settings_manager_instance.settings.response_format
if not(load_result):
    raise Exception("cant load config file")

start_service_instance=start_service()
start_service_instance.block_datetime=settings_manager_instance.settings.block_datetime
start_service_instance.start(settings_manager_instance.settings.first_start)
#start_service_instance.save_data_to_config("default_data.json")


dto_maps={
    reposity_keys.unit_key():unit_dto,
    reposity_keys.range_key():range_dto,
    reposity_keys.range_group_key():range_group_dto,
    reposity_keys.storage_key():storage_dto,
    reposity_keys.receipt_key():receipt_dto,
    reposity_keys.transaction_key():transaction_dto
}

model_maps={
    reposity_keys.unit_key():unit_model,
    reposity_keys.range_key():range_model,
    reposity_keys.range_group_key():range_group_model,
    reposity_keys.storage_key():storage_model,
    reposity_keys.receipt_key():receipt_model,
    reposity_keys.transaction_key():transaction_model
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
        if str(e)=="Формат не верный":
            return Response(
                status=404,
                response="Format isn't supported",
                content_type="text/plain"
            )
        else:
            #raise e
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

@app.route("/api/reposity/save", methods=['POST'])
def save_reposity():
    """
    Save reposity to file
    """
    try:
        start_service_instance.save_data("default_data.json")
        return Response(
            status=200,
            response=json.dumps({"detail":"reposity successfuly saved to file"}),
            content_type="application/json"
        )
    except Exception as e:
        return Response(
            status=400,
            response=json.dumps({"detail":"internal server error"}),
            content_type="application/json"
        )

@app.route("/api/reposity/get/balance_sheet", methods=['GET'])
def get_balance_sheet():
    """
    Get balance sheets
    """
    args=request.args
    begin_date=args.get("begin_date")
    end_date=args.get("end_date")
    storage_name=args.get("storage_name")
    try:
        start_datetime=datetime.datetime.strptime(begin_date,"%Y-%m-%dT%H:%M:%S") if begin_date is not None else datetime.datetime.strptime("2000-01-01T00:00:00","%Y-%m-%dT%H:%M:%S")
        end_datetime=datetime.datetime.strptime(end_date,"%Y-%m-%dT%H:%M:%S") if end_date is not None else datetime.datetime.now()
    except Exception as e:
        return Response(
            status=400,
            response=json.dumps({"detail":"cant resolve begin date or end date"}),
            content_type="application/json"
        )
    start_balance_datetime_filters=[
            filter_dto.create("datetime","lt",start_datetime)
        ]
    main_balance_datetime_filters=[
        filter_dto.create("datetime","lt",end_datetime),
        filter_dto.create("datetime","gt",start_datetime)
    ]
    #storage_obj=start_service_instance.reposity.data[reposity_keys.storage_key()][storage_name]
    storage_filters=[
        filter_dto.create("storage.name","eq",storage_name)
    ]
    balance_sheet=start_service_instance.create_balance_sheet_with_remnants(start_balance_datetime_filters,main_balance_datetime_filters,storage_filters)
    result_format=factory_entity.create("csv")()
    result=result_format.create(balance_sheet)
    return Response(
            response=result,
            status=200,
            content_type=result_format.response_type(),
            )

@app.route("/api/reposity/get/balance_sheet/filtered", methods=['POST'])
def get_filtered_balance_sheet():
    """
    Get filtered balance sheets
    """
    content=request.get_json()
    filter_objs=[]
    start_datetime_filters=[]
    main_datetime_filters=[]
    storage_filters=[]
    if "filters" in content.keys():
        for filter_json in content["filters"]:
            filter_obj=filter_dto.from_dict(filter_json)
            if filter_json["field_name"]=="datetime":
                filter_obj.value=datetime.datetime.strptime(filter_obj.value,"%Y-%m-%dT%H:%M:%S")
                main_datetime_filters.append(filter_obj)
                if filter_json["type"]=="gt" or filter_json["type"]=="ge":
                    start_datetime_filters.append(filter_dto.create("datetime","lt",filter_obj.value))
            elif filter_json["field_name"].split(".")[0]=="storage":
                storage_filters.append(filter_obj)
            else:
                filter_objs.append(filter_obj)
    balance_sheet=start_service_instance.create_balance_sheet(start_datetime_filters,main_datetime_filters,storage_filters,filter_objs)
    result_format=factory_entity.create("csv")()
    result=result_format.create(balance_sheet)
    return Response(
            response=result,
            status=200,
            content_type=result_format.response_type(),
            )


@app.route("/api/<model>/format/<format>/filtered", methods=['POST'])
def get_filtered_model_data(model:str,format:str):
    """
    Получить фильтрованную модель данных в указанном формате
    """
    if model not in start_service_instance.reposity.data.keys():
        return Response(
            status=404,
            response=f"There isn't model with name {model}",
            content_type="text/plain"
        )
    try:
        content=request.get_json()
        filter_objs=[]
        if "filters" in content.keys():
            for filter_json in content["filters"]:
                filter_objs.append(filter_dto.from_dict(filter_json))
        result_format=factory_entity.create(format)()
        base_prototype=prototype(list(start_service_instance.reposity.data[model].values()))
        filtered_prototype=prototype.filter(base_prototype,filter_objs)
        if len(filtered_prototype.data)==0:
            result="empty"
        else:
            result=result_format.create(filtered_prototype.data)
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

@app.route("/api/block_datetime", methods=['POST'])
def change_block_datetime():
    """
    Получить фильтрованную модель данных в указанном формате
    """
    try:
        content=request.get_json()
        new_block_datetime=datetime.datetime.strptime(content["block_datetime"],"%Y-%m-%dT%H:%M:%S")
        start_service_instance.block_datetime=new_block_datetime
        start_service_instance.create_block_remnant()
        return Response(
            response=json.dumps({"message":"block datetime changed successfuly"}),
            status=200,
            content_type="application/json",
            )
    except Exception as e:
        return Response(
            response="Server problem",
            status=500,
            content_type="text/plain",
            )

@app.route("/api/block_datetime", methods=['GET'])
def get_block_datetime():
    """
    Получить фильтрованную модель данных в указанном формате
    """
    try:
        

        return Response(
            response=json.dumps({"block_datetime":start_service_instance.block_datetime.strftime("%Y-%m-%dT%H:%M:%S")}),
            status=200,
            content_type="application/json",
            )
    except Exception as e:
        #raise e
        return Response(
            response="Server problem",
            status=500,
            content_type="text/plain",
            )
    
@app.route("/api/remnants", methods=['POST'])
def get_remnants_by_datetime():
    """
    Получить остатки на конкретную дату
    """
    try:
        content=request.get_json()
        datetime_obj=content["datetime"]
        remnants=start_service_instance.create_remnant(datetime.datetime.strptime(datetime_obj,"%Y-%m-%dT%H:%M:%S"))
        result_format=factory_entity.create_default()()
        result=result_format.create(remnants)
        return Response(
            response=result,
            status=200,
            content_type=result_format.response_type(),
            )
    except Exception as e:
        raise e
        return Response(
            response="Server problem",
            status=500,
            content_type="text/plain",
            )
if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8080)