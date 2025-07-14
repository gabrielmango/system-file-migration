from src.pipelines.base_pipeline import BasePipeline


class CesvFileMigration(BasePipeline):
    def __init__(self):
        super().__init__(name='cesv_file_migration')

    def run(self):
        data = self._extract()

        new_data = self._transform(data)

        self._load(new_data)

    def _extract(self):
        ...

    def _transform(self, data):
        ...

    def _load(self, data):
        ...
