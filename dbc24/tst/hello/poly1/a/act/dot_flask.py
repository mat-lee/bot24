
import os

import dash
from dash import Input, Output, State, dcc, html

import dash_bootstrap_components as dbc


#
#
#
class DotFlask:

    @classmethod
    def app_init(cls, env_obj):
        cls.app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
                            suppress_callback_exceptions=True,
                            assets_folder=env_obj.FLASK_STATIC_DIR,
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

    @classmethod
    def page_not_found__layout(cls, path_name):
        return html.Div([
                    html.H1("404: Not found", className="text-danger"),
                    html.Hr(),
                    html.P(f"The pathname {path_name} was not recognised..."),
                ],
                className="p-3 bg-light rounded-3",)
