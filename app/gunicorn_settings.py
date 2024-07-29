# from app.app_logging import LOG_CONFIG

# logconfig_dict = LOG_CONFIG
bind = "0.0.0.0:8000"
workers = 4
# accesslog = "logs/access.log"
# errorlog = "logs/app.log"
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# worker_class = "uvicorn.workers.UvicornWorker"
worker_class = "app.worker.MyAppWorker"