from uvicorn.workers import UvicornWorker

class MyAppWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "log_config": "app/logging_config.json"
    }