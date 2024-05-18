
import os
import glob
import pandas as pd
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html, dash_table

from act.crux import Crux
from polyfuzz import PolyFuzz

#
# Fuzzy Pandas (Python)
#
# @pytest.mark.skip
class TestFuzzyPoly2a:

    fuzzy_approaches=['tfidf', 'embeddings']
    uid_attr_list = [ 'uid_file_a_name', 'uid_file_b_name', 'uid_file_c_name', 'uid_file_d_name', 'uid_file_e_name',
                      'uid_table_a_div', 'uid_table_b_div', 'uid_table_c_div', 'uid_table_d_div', 'uid_table_e_div',
                      'uid_table_f_div', 'uid_table_g_div',
                      'uid_file_name', 'uid_data_table_div', 'uid_button_e']

    def test_fuzzy_poly2a(self, dot_env_obj):

        self.attributes(dot_env_obj)
        self.app, self.app_server = Crux.app_init(dot_env_obj)
        self.app.layout = self.layout()
        self.callbacks(self.app)
        self.app.run_server(port=dot_env_obj.ui_port)

    def attributes(self, env_obj):

        for an_attr in self.uid_attr_list:
            setattr(self, an_attr, an_attr)

        self.f_loc = env_obj.ui_assets_y24m05d08
        self.f_dir = [os.path.basename(x) for x in glob.glob( os.path.join( self.f_loc,'*.json' ) )]

    def layout(self):
        """
        :param cls_arg:
        :return:
        """

        return html.Div([

            dbc.Row([
                dbc.Col(width=1, style={'border': '1px'}, children=html.Div(html.H4('String'))),
                dbc.Col(width=3, style={'border': '1px'}, children=html.Div(html.H4('List1'))),
                dbc.Col(width=3, style={'border': '1px'}, children=html.Div(html.H4('List2'))),
                dbc.Col(width=2, style={'border': '1px'}, children=html.Div(html.H4('Algorithms'))),
            ]),
            dbc.Row([
                dbc.Col(width=1, children=html.P("Matching")),
                dbc.Col(width=3, children=dcc.Dropdown(id=self.uid_file_a_name, value='company_names.json', options=self.f_dir)),
                dbc.Col(width=3, children=dcc.Dropdown(id=self.uid_file_c_name, value='company_names.json', options=self.f_dir)),
                dbc.Col(width=2, children=dcc.Dropdown(id=self.uid_file_b_name, value=self.fuzzy_approaches[0], options=self.fuzzy_approaches)),
                dbc.Col(width=2, children=dbc.Button('Submit', id=self.uid_button_e,  n_clicks=0)),
            ]),
            dbc.Row([
                dbc.Col(width=1, ),
                dbc.Col(width=3, children=html.Div(id=self.uid_table_a_div), ),
                dbc.Col(width=3, children=html.Div(id=self.uid_table_c_div), ),
                dbc.Col(width=4, children=html.P(id=self.uid_table_b_div), ),
            ]),
            dbc.Row([
                #dbc.Col(width=6, children=dcc.Dropdown(id=self.uid_file_d_name, value='company_names.json', options=self.f_dir)),
                #dbc.Col(width=6, children=dcc.Dropdown(id=self.uid_file_e_name, value='company_names.json', options=self.f_dir)),
            ]),
            dbc.Row([
                dbc.Col(width=5, children=html.Div(id=self.uid_table_d_div), ),
                #dbc.Col(width=6, children=html.Div(html.Img(id=self.uid_table_e_div)), ),
                # dbc.Col(width=6, children=html.Img(id=self.uid_table_d_div), ),
                # dbc.Col(width=6, children=html.Div(id=self.uid_table_d_div), ),
            ]),
            dbc.Row([
                dbc.Col(width=1, ),
                dbc.Col(width=5, children=html.Div(id=self.uid_table_f_div), ),
                #dbc.Col(width=6, children=html.Div(id=self.uid_table_g_div), ),
                dbc.Col(width=6, children=html.Div(html.Img(id=self.uid_table_g_div)), ),
            ]),

        ])


    def callbacks(self, cls_arg):

        @cls_arg.callback(
            Output(self.uid_table_a_div, 'children'),
            [Input(self.uid_file_a_name, 'value')],
        )
        def update_output_src(input_value):
            full_name = os.path.join( self.f_loc, input_value )
            df = pd.read_json(full_name)
            df.rename(columns={0: 'From'}, inplace=True)
            return dash_table.DataTable(data=df.to_dict('records'),
                                        columns=[{"name": i, "id": i} for i in df.columns],
                                        page_size=10),

        # Output(self.uid_table_d_div, 'children')
        @cls_arg.callback(
            Output(self.uid_table_b_div, 'children'),
            Input(self.uid_file_b_name, 'value')
        )
        def update_output_approaches(input_value):
            return input_value


        @cls_arg.callback(
            Output(self.uid_table_c_div, 'children'),
            [Input(self.uid_file_c_name, 'value')],
        )
        def update_output_target(input_value):
            full_name = os.path.join( self.f_loc, input_value )
            df = pd.read_json(full_name)
            df.rename(columns={0: 'To'}, inplace=True)
            return dash_table.DataTable(data=df.to_dict('records'),
                                        columns=[{"name": i, "id": i} for i in df.columns],
                                        page_size=10),

        #
        # State(self.uid_button_e, 'n_clicks_timestamp')
        @cls_arg.callback(
            [
                Output(self.uid_table_f_div, 'children'),
                Output(self.uid_table_g_div, 'children')
            ],
            Input(self.uid_button_e, 'n_clicks'),
        )
        def on_click(n_clicks):

            from_list = ["apple", "apples", "appl", "recal", "house", "similarity"]
            to_list = ["apple", "apples", "mouse"]
            model = PolyFuzz("TF-IDF").match(from_list, to_list)
            df = model.get_matches()

            t1 =  dash_table.DataTable(data=df.to_dict('records'),
                                        columns=[{"name": i, "id": i} for i in df.columns],
                                        page_size=10),


            return t1, t1

