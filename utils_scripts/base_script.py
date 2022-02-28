import os
import uuid
from abc import ABC, abstractmethod
from datetime import datetime

import numpy as np
import pandas as pd


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
    def __init__(self):
        self.execution_id = str(uuid.uuid4())
        self.n_jobs = os.cpu_count()
        self.time_leaps = {}

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

    def _get_execution_time(self, start_time='', end_time=''):
        if start_time and end_time:
            return end_time - start_time
        else:
            return self.end_time - self.start_time

    def _get_append_now(self, key: str):
        """
        Can be used if the user wants to register the
        script's intermediate execution steps. A key name
        indicating the registered moment must be passed
        as input.
        """
        self.time_leaps[key] = datetime.now()

    def attr_to_parquet(self, attribute: str, filename: str):
        self.__dict__[attribute].to_parquet(filename)

    def attr_to_csv(self, attribute: str, filename: str):
        self.__dict__[attribute].to_parquet(filename)

    def attr_to_pickle(self, attribute: str, filename: str):
        pd.to_pickle(self.__dict__[attribute], filename)

    def to_parquet(self, obj_to_persist, filename):
        obj_to_persist.to_parquet(filename)

    def to_csv(self, obj_to_persist, filename, sep=';', index=False):
        obj_to_persist.to_csv(filename, sep=sep, index=index)

    def to_pickle(self, obj_to_persist, filename):
        pd.to_pickle(obj_to_persist, filename)
