

import os
import sys
import pytest
import pprint as pp

#
# PYTHONPATH
#
sys.path.insert(0, os.getcwd())
pp.pprint(sys.path)

#
# Env
#    pip install python-dotenv
#
from dotenv import load_dotenv, dotenv_values, find_dotenv


class DotEnv:

    # ui_dir_a_f_file =
    #attr_list=['ui_dir_a_f_file', 'ui_dir_a_p_pdfs', 'ui_dir_assets' ]
    # unique ids
    #for an_attr in self.attr_list:
    #    setattr(self, an_attr, an_attr)

    def __init__(self):

        #
        dot_env_file_name = 'dot_env'
        dot_env_file = os.path.join(os.getcwd(), 'a_', 'b_bash', dot_env_file_name)
        if find_dotenv(dot_env_file):
            load_dotenv(dot_env_file)  # take environment variables from .env.
            dot_env_dict = dotenv_values(dot_env_file)

        for a_key in dot_env_dict.keys():
            setattr(self, a_key, dot_env_dict[a_key])

dotEnv = DotEnv()

@pytest.fixture(scope='session')
def dot_env_obj():
    return dotEnv






