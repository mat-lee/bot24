
import os

#
# Env
#    pip install python-dotenv
#
from dotenv import load_dotenv, dotenv_values, find_dotenv

#
#
#
class DotEnv:

    def __init__(self, work_dir=os.getcwd(), os_name_id=os.name):

        #if work_dir is None:
        #    work_dir=os.getcwd()

        #
        # dot_env files
        #
        dot_env_file_name = 'dot_env_'+os_name_id
        dot_env_file = os.path.join(work_dir, 'a_', 'b_bash', dot_env_file_name)
        dot_env_dict = dict()
        if find_dotenv(dot_env_file):
            load_dotenv(dot_env_file)  # take environment variables from .env.
            dot_env_dict = dotenv_values(dot_env_file)

        for a_key in dot_env_dict.keys():
            setattr(self, a_key, dot_env_dict[a_key])

        # attributes
        # ui_dir_a_f_file =
        self.attr_list = ['ui_dir_assets_f_file', 'ui_dir_assets_p_pdfs', ]
        # unique ids
        for an_attr in self.attr_list:
            setattr(self, an_attr, an_attr)

dotEnv = DotEnv()