# import logging
# import logging.config

log_conf = {
    'version': 1,
    'formatters': {
        'base': {
            'format': '%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s',
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'filename': 'cache.log',
            'formatter': 'base',

        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'base',
        },
    },
    'loggers': {
        'file_logger': {
            'level': 'INFO',
            'handlers': ['file_handler'],
        },
        'file_and_stream_logger': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler'],
        },
    },
}
