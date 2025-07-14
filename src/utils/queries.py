DATA_CESV_QUERY = """
SELECT 
    t1.co_uuid_2,
    t1.co_uuid AS uuid_candidatura,
    t2.co_uuid AS uuid_processo 
FROM cesv.tb_candidatura t1
LEFT JOIN cesv.tb_processo_seletivo t2
    ON t1.co_processo_seletivo = t2.co_seq_processo_seletivo
ORDER BY t1.co_seq_candidatura DESC;
"""
