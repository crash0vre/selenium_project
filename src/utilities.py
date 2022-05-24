import time
import yaml


def load_yaml_file(filepath):
    try:
        print('reading yaml file')
        with open (filepath, 'r') as stream:
            file_content=yaml.safe_load(stream)
        #return file_content
    except FileNotFoundError as err:
        print('Incorrect file path is provided')
        print(f'File not foundError: {err}')
        raise
    else:
        return file_content


def get_str_second():
    return time.strftime("%Y%m/%d_%H:%M:%S", time.localtime())

def get_timestamp():
    return time.strftime('%m%d%H%S', time.localtime())