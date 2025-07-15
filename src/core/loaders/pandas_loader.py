from pprint import pprint

import pandas as pd

from src.core.loaders.base_loader import BaseLoader


class PandasLoader(BaseLoader):
    def load(self, *args, **kwargs):
        ...
