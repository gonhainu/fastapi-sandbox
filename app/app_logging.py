import logging

def getLogger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("logs/app.log")
    logger.addHandler(fh)
    fmt = logging.Formatter("[%(asctime)s] [%(process)s] [%(module)s] [%(levelname)s] %(message)s")
    fh.setFormatter(fmt)

    return logger

# logger = logging.getLogger("gunicorn.error")
# logger.setLevel(logging.INFO)

# fh = logging.FileHandler("logs/app.log")
# logger.addHandler(fh)

# fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# fh.setFormatter(fmt)



# import logging, logging.config

# LOG_CONFIG = {
#     "version": 1,
#     "disable_existing_loggers": True,
#     "formatters": {
#         "default": {
#             "format": "%(asctime)s [%(process)s] %(levelname)s: %(message)s"
#         },
#         "access": {
#             "format": '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
#         }
#     },
#     "handlers": {
#         "console": {
#             "formatter": "default",
#             "class": "logging.StreamHandler",
#             "stream": "ext://sys.stdout",
#             "level": "INFO",
#         },
#         "access_log": {
#             "formatter": "access",
#             "class": "logging.StreamHandler",
#             "stream": "ext://sys.stdout",
#             "level": "INFO",
#         }
#     },
#     "root": {"handlers": ["console"], "level": "INFO"},
#     "loggers": {
#         "gunicorn": {"propagate": True},
#         "gunicorn.access": {
#             "handlers": ["access_log"],
#             "level": "INFO",
#             "propagate": True
#         },
#         "gunicorn.error": {"propagate": True},
#         "uvicorn": {
#             "handlers": ["access_log"],
#             "level": "INFO",
#             "propagate": True
#         },
#         "uvicorn.access": {"propagate": True},
#         "uvicorn.error": {"propagate": True},
#     },
# }

# logging.config.dictConfig(LOG_CONFIG)
# logger = logging.getLogger(__name__)