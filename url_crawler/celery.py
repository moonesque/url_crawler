import logging
from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger
from celery.app.log import TaskFormatter
from config import config


cerley_broker = config.BROKER_URL

# Celery instance
celery_app = Celery(
    "crawler",
    broker=cerley_broker,
    backend="redis://localhost:6379",
    include=["url_crawler.crawler"],
)
# Use to override celery log config with project level config
# celery_app.conf.update({"worker_hijack_root_logger": False})

# Config celery logger
@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    # Remove all default handlers of celery
    for handler in logger.handlers:
        logger.removeHandler(handler)
    # Add my own handler
    fh = config.log_fhandler
    tf = TaskFormatter(
        "%(asctime)s - %(task_id)s - %(task_name)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(tf)
    sh = config.log_shandler
    sh.setFormatter(tf)
    logger.addHandler(fh)
    logger.addHandler(sh)


@after_setup_task_logger.connect
def setup_task_logger(logger, *args, **kwargs):
    logger.handlers
    logger.addHandler(config.log_fhandler)
    tf = TaskFormatter(
        "%(asctime)s - %(task_id)s - %(task_name)s - %(name)s - %(levelname)s - %(message)s"
    )
    for handler in logger.handlers:
        handler.setFormatter(tf)


if __name__ == "__main__":
    celery_app.start()
