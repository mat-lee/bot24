
import os

import dash
from dash import Input, Output, State, dcc, html

import dash_bootstrap_components as dbc


#
#
#
class Crux:

    @classmethod
    def app_init(cls, env_obj):
        cls.app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
                            suppress_callback_exceptions=True,
                            assets_folder=env_obj.ui_dir_assets
                            )
        cls.app_server = cls.app.server

        return cls.app, cls.app_server


    @classmethod
    def exe(cls, env_obj):
        cls.app_init(env_obj)
        cls.app.layout = cls.layout()
        cls.app.run_server(port=env_obj.ui_port)

    @classmethod
    def layout(cls):
        return html.P("Hello")
