import pandas as pd

from src.core.transformers.base_transformer import BaseTransformer


class PandasTransformer(BaseTransformer):
    def transform(self, *args, **kwargs):
        column = kwargs.get('column')
        data = kwargs.get('data')
        return self._merge_data(data, column)

    def _merge_data(self, data, column):
        dfs = [pd.DataFrame(lines) for lines in data.values()]

        return pd.merge(dfs[0], dfs[1], on=column, how='left')
