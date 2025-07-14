from src.core.extractors.base_extractor import BaseExtractor


class DataCesvExtractor(BaseExtractor):
    def extract(self, *args, **kwargs):
        query = """
                select 
                    t1.co_uuid_2,
                    t1.co_uuid as uuid_candidatura,
                    t2.co_uuid as uuid_processo 
                from cesv.tb_candidatura t1
                left join cesv.tb_processo_seletivo t2
                    on t1.co_processo_seletivo = t2.co_seq_processo_seletivo
                order by t1.co_seq_candidatura desc;
            """
        with self.db_connection as conn:
            data = conn.execute_query(query)
        if self.validate_output(data):
            return data
        return []
