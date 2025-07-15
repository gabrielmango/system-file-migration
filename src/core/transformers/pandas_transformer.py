import pandas as pd

from src.core.extractors.postgres_extractor import PostgresExtractor
from src.core.transformers.base_transformer import BaseTransformer
from src.utils.config.postgres_acess import FileserverPostgresAcess


class PandasTransformer(BaseTransformer):
    def transform(self, *args, **kwargs):
        column = kwargs.get('column')
        data = kwargs.get('data')
        new_data = self._merge_data(data, column)
        return self._data_enrichment(new_data.dropna())

    def _merge_data(self, data, column):
        dfs = [pd.DataFrame(lines) for lines in data.values()]

        return pd.merge(dfs[0], dfs[1], on=column, how='left')

    def _data_enrichment(self, data):
        data_list = []
        for index, row in data.iterrows():
            new_data = self._extract_data_from_fileserver(row['co_seq_anexo'])
            new_data['co_uuid_2'] = row['uuid_candidatura']

        return data_list.append(new_data)

    def _extract_data_from_fileserver(self, id):
        fileserver_acess = FileserverPostgresAcess().as_dict()
        extractor = PostgresExtractor(
            db_connection=fileserver_acess.get('FILESERVER_POSTGRES_PROD')
        )
        query = f'SELECT * FROM fileserver.tb_anexo WHERE co_seq_anexo = {id};'
        return extractor.extract(query)

    def _change_data(self, data_list):
        ...
