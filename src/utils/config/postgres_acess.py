from src.utils.config.base_config import BaseConfig


class FileserverPostgresAcess(BaseConfig):
    @property
    def required_vars(self):
        return [
            'FILESERVER_POSTGRES_PROD',
            'FILESERVER_POSTGRES_PREPROD',
            'FILESERVER_POSTGRES_HML',
            'FILESERVER_POSTGRES_TST',
            'FILESERVER_POSTGRES_DEV',
        ]
