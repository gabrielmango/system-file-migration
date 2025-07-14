from src.core.connections.postgres_connection import PostgresConnection
from src.core.extractors.postgres_extractor import PostgresExtractor
from src.pipelines.base_pipeline import BasePipeline
from src.utils.config.postgres_acess import CesvPostgresAcess
from src.utils.queries import DATA_CESV_QUERY


class CesvFileMigration(BasePipeline):
    def __init__(self):
        super().__init__(name='cesv_file_migration')
        self.__acess_cesv_postgres = CesvPostgresAcess().as_dict()

    def run(self):
        data = self._extract()

        new_data = self._transform(data)

        self._load(new_data)

    def _extract(self):
        cesv_data = self._extract_data_from_cesv()

    def _extract_data_from_cesv(self):
        postgres_conn = PostgresConnection(
            self.__acess_cesv_postgres.get('CESV_PROD')
        )
        extractor = PostgresExtractor(db_connection=postgres_conn)
        return extractor.extract(query=DATA_CESV_QUERY)

    def _transform(self, data):
        ...

    def _load(self, data):
        ...
