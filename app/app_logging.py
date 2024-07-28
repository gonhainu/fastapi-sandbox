# import logging

# def getLogger(name: str):
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#     fh = logging.FileHandler("logs/app.log")
#     logger.addHandler(fh)
#     fmt = logging.Formatter("[%(asctime)s] [%(process)s] [%(module)s] [%(levelname)s] %(message)s")
#     fh.setFormatter(fmt)

#     return logger

# logger = logging.getLogger("gunicorn.error")
# logger.setLevel(logging.INFO)

# fh = logging.FileHandler("logs/app.log")
# logger.addHandler(fh)

# fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# fh.setFormatter(fmt)



import logging, logging.config

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"default": {"format": "%(asctime)s [%(process)s] [%(module)s] %(levelname)s: %(message)s"}},
    "handlers": {
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "INFO",
        },
        "access": {
            "formatter": "default",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "logs/access_log.log",
            "encoding": "utf-8",
            "when": "D",
            "backupCount": 1
        },
        "app": {
            "formatter": "default",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "logs/app_log.log",
            "encoding": "utf-8",
            "when": "D",
            "backupCount": 1
        }
    },
    "root": {"handlers": ["console", "app"], "level": "INFO"},
    "loggers": {
        "gunicorn": {"propagate": True},
        "gunicorn.access": {"propagate": True},
        "gunicorn.error": {"propagate": True},
        "uvicorn": {"propagate": True},
        "uvicorn.access": {
            "handlers": ["access"],
            "propagate": False
        },
        "uvicorn.error": {
            "handlers": ["app"],
            "propagate": False
        },
    },
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)