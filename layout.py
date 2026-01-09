from dash import html, dcc
from dashboard import column_options

def dashboardaa_layout():
    return html.Div([
        html.H1("📊 Advanced Multi-Chart Viewer",id="Heading"),

        # html.Div([
        #     html.Button("➕ Add Chart", id="add-chart-btn", n_clicks=0, className="add-chart-btn"),
        #     html.Button("🌍 Add Global Filter", id="show-global-filter-btn", n_clicks=0,className="button#show-global-filter-btn"),
        #     html.Button("❌ Remove Global Filter", id="remove-global-filter-btn", n_clicks=0,className="button#remove-global-filter-btn"),
        #     html.Button("💾 Save Dashboard", id="save-dashboard-btn", n_clicks=0, className="button#save-dashboard-btn"),
        #     dcc.Download(id="download-dashboard"),  # Invisible
        #     dcc.Upload(
        #         id="upload-dashboard", 
        #         children=html.Button("📂 Load Dashboard", style={"float": "right"},className="upload-dashboard")
        #     ),
        #     html.Button("Logout", id="logout-btn", style={"float": "right"},className="logout-btn")
        # ], style={"overflow": "hidden"}),  # ✅ Fixed: Contains floats, no extra div issues [web:46]
        html.Div(
            [
                html.Button(
                    "📁 File Choose",
                    id="File-Choose-btn",
                    n_clicks=0,
                    className="File-Choose-btn"
                ),

                html.Button(
                    "➕ Add Chart",
                    id="add-chart-btn",
                    n_clicks=0,
                    className="add-chart-btn"
                ),

                html.Button(
                    "🌍 Add Global Filter",
                    id="show-global-filter-btn",
                    n_clicks=0,
                    className="global-filter-btn"
                ),

                html.Button(
                    "❌ Remove Global Filter",
                    id="remove-global-filter-btn",
                    n_clicks=0,
                    className="remove-filter-btn"
                ),

                html.Button(
                    "💾 Save Dashboard",
                    id="save-dashboard-btn",
                    n_clicks=0,
                    className="box"   # your Uiverse style
                ),

                dcc.Download(id="download-dashboard"),

                dcc.Upload(
                    id="upload-dashboard",
                    children=html.Button(
                        "📂 Load Dashboard",
                        className="upload-dashboard"
                    )
                ),

                html.Button(
                    "Logout",
                    id="logout-btn",
                    className="logout-btn"
                )

            ],
            style={
                "display": "flex",
                "alignItems": "center",
                "gap": "10px",
                "flexWrap": "wrap"   # keeps line clean on small screens
            }
        ),


        html.Hr(),

        html.Div(
            id="global-filter-block",
            style={"display": "none"},
            children=[
                html.H3("🌍 Global Filter"),
                dcc.Dropdown(id="global-filter-column", options=column_options),
                dcc.Dropdown(id="global-filter-values", multi=True)
            ]
        ),

        dcc.Store(id="global-filter-store"),
        dcc.Store(id="full-dashboard-store"),
        dcc.Store(id="chart-ids", data=[]),

        html.Div(id="charts-container")
    ])
