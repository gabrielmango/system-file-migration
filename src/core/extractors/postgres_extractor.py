from src.core.extractors.base_extractor import BaseExtractor


class PostgresExtractor(BaseExtractor):
    def extract(self, *args, **kwargs):
        query = kwargs.get('query')
        if not query:
            raise ValueError(
                "A SQL query must be provided using the 'query' keyword argument."
            )

        with self.db_connection as conn:
            data = conn.execute_query(query)
        if self.validate_output(data):
            return data
        return []
