from fastapi.testclient import TestClient
from inline_snapshot import snapshot

from docs_src.path_params.tutorial005_py310 import app

client = TestClient(app)


def test_get_enums_alexnet():
    response = client.get("/models/alexnet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "alexnet", "message": "Deep Learning FTW!"}


def test_get_enums_lenet():
    response = client.get("/models/lenet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "lenet", "message": "LeCNN all the images"}


def test_get_enums_resnet():
    response = client.get("/models/resnet")
    assert response.status_code == 200
    assert response.json() == {"model_name": "resnet", "message": "Have some residuals"}


def test_get_any_model_name():
    response = client.get("/models/foo")
    assert response.status_code == 200
    assert response.json() == {"model_name": "foo", "message": "Have some residuals"}


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {"title": "FastAPI", "version": "0.1.0"},
            "paths": {
                "/models/{model_name}": {
                    "get": {
                        "summary": "Get Model",
                        "operationId": "get_model_models__model_name__get",
                        "parameters": [
                            {
                                "name": "model_name",
                                "in": "path",
                                "required": True,
                                "schema": {"type": "string", "title": "Model Name"},
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {"application/json": {"schema": {}}},
                            },
                            "422": {
                                "description": "Validation Error",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/HTTPValidationError"
                                        }
                                    }
                                },
                            },
                        },
                    }
                }
            },
            "components": {
                "schemas": {
                    "HTTPValidationError": {
                        "properties": {
                            "detail": {
                                "items": {
                                    "$ref": "#/components/schemas/ValidationError"
                                },
                                "type": "array",
                                "title": "Detail",
                            }
                        },
                        "type": "object",
                        "title": "HTTPValidationError",
                    },
                    "ValidationError": {
                        "properties": {
                            "loc": {
                                "items": {
                                    "anyOf": [{"type": "string"}, {"type": "integer"}]
                                },
                                "type": "array",
                                "title": "Location",
                            },
                            "msg": {"type": "string", "title": "Message"},
                            "type": {"type": "string", "title": "Error Type"},
                            "input": {"title": "Input"},
                            "ctx": {"type": "object", "title": "Context"},
                        },
                        "type": "object",
                        "required": ["loc", "msg", "type"],
                        "title": "ValidationError",
                    },
                }
            },
        }
    )
