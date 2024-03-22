import os


class FileSystem:
    fnf_message = "\n{filename} was not found by {path}\n"

    @staticmethod
    def check_file_exists(path: str, name: str, err_to_raise: type):
        """ Checks if the file path is valid """
        if os.path.exists(path=path) is False:
            raise err_to_raise(msg=FileSystem.fnf_message.format(filename=name, path=path))
