# src/mypkg/logger.py

import logging
from logging import Logger
from typing import Optional

def get_logger (
        name: Optional[str] =None,
        level: int =logging.INFO,
        fmt_str: str ="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
) -> Logger:
    
    logger = logging.getLogger(name if name else "mypkg")
    if not logger.handlers:
        logger.setLevel()
        handler=logging.StreamHandler()
        fmt=logging.Formatter(fmt_str)
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.propagate = False 
    return logger 

