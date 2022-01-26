import pandas as pd
import numpy as np
import uuid

from datetime import datetime
from abc import ABC, abstractmethod


class BaseScript(ABC):
    """
    Abstract class for general purpose support activities.
    The class using this abstract class as template gets additional
    features, like execution id and register of start and end of an
    execution.

    It is important that the user treats each instanciation of the
    class being used as one individual execution, because execution
    parameters are treated as the abstract class's attributes.
    """
    @abstractmethod
    def __init__(self):
        self.execution_id = str(uuid.uuid4())

    def run(self):
        """
        Runs the class. Persists a start and end time values
        """
        self.start_time = datetime.now()
        output = self._run()
        self.end_time = datetime.now()
        return output

    @abstractmethod
    def _run(self):
        pass

    def _get_attributes(self):
        return self.__dict__

    def _to_parquet(self, attribute: str, filename: str):
        self.__dict__[attribute].to_parquet(filename)

    def _to_csv(self, attribute: str, filename: str):
        self.__dict__[attribute].to_parquet(filename)

    def _to_pickle(self, attribute: str, filename: str):
        pd.to_pickle(self.__dict__[attribute], filename)
