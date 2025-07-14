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


class CesvPostgresAcess(BaseConfig):
    @property
    def required_vars(self):
        return [
            'CESV_PROD',
            'CESV_PREPROD',
            'CESV_HML',
            'CESV_TST',
            'CESV_DEV',
        ]
