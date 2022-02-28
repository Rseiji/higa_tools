import os
from inspect import currentframe, getframeinfo

from base_script import BaseScript


class PrimitiveDebugger(BaseScript):
    def __init__(self, filepath='', is_exec_id_folder=False, is_print=True):
        super().__init__()
        self.filepath = filepath
        self.is_exec_id_folder = is_exec_id_folder
        self.is_print = is_print

        if self.is_exec_id_folder:
            if filepath:
                self.filepath = os.path.join(filepath, self.execution_id)
            else:
                self.filepath = f'tmp_{self.execution_id}'

        self.persisted_items = {}
        self.execution_metadata = {
            'execution_id': self.execution_id
        }

    def _run(self):
        """
        Placeholder for abstract class. This method is intended
        not to be used when calling for this class
        """
        pass

    def persist_object_in_flow(self, obj_to_persist, filename='',
                               filetype='pickle', is_print=''):
        """Persists given object during the flow of code execution
        """
        path_and_file = self._get_filepath(filename, filetype)
        try:
            persisting_function = getattr(self, f'to_{filetype}')
            persisting_function(obj_to_persist, path_and_file)

            print(f'Successfully persisted {path_and_file}')

            if (not is_print and self.is_print) or is_print:
                print('Persisted object:', obj_to_persist)
                print('*' * 20)

            self.persisted_items.update({
                str(len(self.persisted_items) + 1): path_and_file
            })
        except:
            # to do: improve this implementation
            print(f'Failed to persist {path_and_file}')
            self.execution_metadata.update({
                f'failed_execution_{filename}': {self.filepath}
            })

    def _get_filepath(self, filename, filetype, preffix='tmp',
                      suffix=''):
        """Creates a file path in a parameterized way. Defines a filename
        with specific given pattern and uses os.path.join to include a
        direcotory name
        """
        if self.filepath != '' and not os.path.exists(self.filepath):
            os.makedirs(self.filepath)

        line_number = self._get_linenumber(level=3)

        if suffix:
            suffix = '_' + suffix

        if preffix:
            preffix = preffix + '_'

        filename_parameterized = (
            f"{preffix}{filename}_{line_number}{suffix}.{filetype}"
        )
        return os.path.join(self.filepath, filename_parameterized)

    def _get_linenumber(self, level=2):
        """Returns the line of the code calling this method
        """
        cf = currentframe()
        for i in range(level):
            cf = cf.f_back
        return getframeinfo(cf).lineno

    def persist_execution_metadata(self):
        self.execution_metadata.update({
            "qtd_saved_objects": len(self.persisted_items),
            "persisted_rows": [int(x) for x in self.persisted_items.keys()]
        })

        path_and_file = self._get_filepath('execution_metadata', 'pickle')
        self.to_pickle(self.execution_metadata, path_and_file)
