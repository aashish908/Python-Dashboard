from dash import dcc, html
from dashboard import df, column_options
# # ------------------ CHART BLOCK ------------------
def create_chart_block(chart_id):
    return html.Div([
      dcc.Store(
            id={'type': 'chart-store', 'index': chart_id},
            data={
                'selected_columns': [df.columns[0]],
                'chart_type': 'bar',
                'mapping': '',
                'color_input': '',
                'selected_values': [],
                'display_mode': 'frequency'
            }
        ),
        
        html.Div([
            html.Button(
                "❌ Remove Chart",
                id={'type': 'remove-chart-btn', 'index': chart_id},
                n_clicks=0,
                style={
                    "marginBottom": "10px",
                    "backgroundColor": "#e74c3c",
                    "color": "white",
                    "border": "none",
                    "padding": "5px 10px",
                    "cursor": "pointer",
                    "borderRadius": "5px",
                    "fontWeight": "bold"
                }
            ),
        ], style={"textAlign": "right"}),

        html.Hr(),

        html.Div([
            html.Div([
                html.Label("Select Columns:"),
                dcc.Dropdown(
                    id={'type': 'columns-dropdown', 'index': chart_id},
                    options=column_options,
                    value=[df.columns[0]],
                    multi=True,
                    style={"width": "220px"}
                ),
            ], style={"marginRight": "20px"}),

            html.Div([
                html.Label("Chart Type:"),
                dcc.Dropdown(
                    id={'type': 'chart-type-dropdown', 'index': chart_id},
                    options=[
                        {"label": "Bar Chart", "value": "bar"},
                        {"label": "Column Chart", "value": "column"},
                        {"label": "Pie Chart", "value": "pie"},
                        {"label": "Donut Chart", "value": "donut"},
                        {"label": "Table", "value": "table"},
                        {"label": "KPI", "value": "kpi"},
                    ],
                    value='bar',
                    clearable=False,
                    style={"width": "180px"}
                ),
            ], style={"marginRight": "20px"}),

            html.Div([
                html.Label("Manual Mapping:"),
                dcc.Input(
                    id={'type': 'value-mapping-input', 'index': chart_id},
                    type='text',
                    placeholder="1=Male, 2=Female",
                    style={"width": "200px"}
                ),
            ], style={"marginRight": "20px"}),

            html.Div([
                html.Label("Custom Colors:"),
                dcc.Input(
                    id={'type': 'color-input', 'index': chart_id},
                    type='text',
                    placeholder="#FF0000, #00FF00",
                    style={"width": "200px"}
                ),
            ])
        ], style={"display": "flex", "flexWrap": "wrap", "justifyContent": "center"}),

        html.Div([
            html.Label("Filter Specific Values (optional):"),
            dcc.Dropdown(
                id={'type': 'value-filter-dropdown', 'index': chart_id},
                multi=True,
                placeholder="Select values to include..."
            ),
        ], style={"width": "400px", "margin": "10px auto"}),

        html.Div([
            html.Label("Display Mode:"),
            dcc.RadioItems(
                id={'type': 'display-mode-radio', 'index': chart_id},
                options=[
                    {'label': 'Frequency', 'value': 'frequency'},
                    {'label': 'Percentage', 'value': 'percentage'},
                ],
                value='frequency',
                labelStyle={'display': 'inline-block', 'marginRight': '20px'}
            )
        ], style={"textAlign": "center", "marginBottom": "10px"}),

        html.Div(id={'type': 'chart-container', 'index': chart_id}, children=[
            dcc.Graph(id={'type': 'chart-output', 'index': chart_id}),
            html.Div(id={'type': 'table-output', 'index': chart_id}),
            html.Div(id={'type': 'kpi-output', 'index': chart_id})
        ]),

        html.Div(id={'type': 'total-responses', 'index': chart_id},
                 style={"textAlign": "center", "color": "red", "fontSize": 16})

    ], id={'type': 'chart-block', 'index': chart_id},
       style={"border": "1px solid #ccc", "padding": "15px", "marginBottom": "20px", "borderRadius": "8px"})

# def create_global_filter_block(filter_id):
#     return html.Div([

#         dcc.Store(
#             id={'type': 'global-filter-store', 'index': filter_id},
#             data={"column": None, "values": []}
#         ),

#         html.Div([
#             html.Button(
#                 "❌ Remove Filter",
#                 id={'type': 'remove-global-filter-btn', 'index': filter_id},
#                 n_clicks=0,
#                 style={
#                     "marginBottom": "10px",
#                     "backgroundColor": "#e74c3c",
#                     "color": "white",
#                     "border": "none",
#                     "padding": "5px 10px",
#                     "cursor": "pointer",
#                     "borderRadius": "5px",
#                     "fontWeight": "bold"
#                 }
#             )
#         ], style={"textAlign": "right"}),

#         html.Hr(),

#         html.Div([

#             html.Div([
#                 html.Label("Select Filter Column:"),
#                 dcc.Dropdown(
#                     id={'type': 'global-filter-column', 'index': filter_id},
#                     options=column_options,
#                     placeholder="Select column...",
#                     style={"width": "220px"}
#                 ),
#             ], style={"marginRight": "20px"}),

#             html.Div([
#                 html.Label("Select Filter Values:"),
#                 dcc.Dropdown(
#                     id={'type': 'global-filter-values', 'index': filter_id},
#                     multi=True,
#                     placeholder="Select values...",
#                     style={"width": "220px"}
#                 ),
#             ])

#         ], style={"display": "flex", "flexWrap": "wrap", "justifyContent": "center"}),

#     ], id={'type': 'global-filter-block', 'index': filter_id},
#        style={"border": "2px solid #3498db",
#               "padding": "15px",
#               "marginBottom": "20px",
#               "borderRadius": "8px",
#               "backgroundColor": "#eef7ff"})
