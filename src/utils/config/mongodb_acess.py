from src.utils.config.base_config import BaseConfig


class FileserverMongodbAcess(BaseConfig):
    @property
    def required_vars(self):
        return [
            'FILESERVER_MONGODB_PROD',
            'FILESERVER_MONGODB_PREPROD',
            'FILESERVER_MONGODB_HML',
            'FILESERVER_MONGODB_TST',
            'FILESERVER_MONGODB_DEV',
        ]
