from dash import html, dcc
from dashboard import column_options


def dashboardaa_layout():
    return html.Div(
        [
            # -----------------------------
            # HEADER
            # -----------------------------
            html.Div(
                html.H1(
                    "📊 Advanced Multi-Chart Viewer",
                    id="Heading"
                ),
                style={
                    "textAlign": "center",
                    "height": "8%",
                },
            ),

            # -----------------------------
            # TOP CONTROL BAR
            # -----------------------------
            html.Div(
                [
                    html.Button(
                        "📁 File Choose",
                        id="File-Choose-btn",
                        n_clicks=0,
                        className="File-Choose-btn",
                    ),

                    html.Button(
                        "➕ Add Chart",
                        id="add-chart-btn",
                        n_clicks=0,
                        className="add-chart-btn",
                    ),

                    html.Button(
                        "🌍 Add Global Filter",
                        id="show-global-filter-btn",
                        n_clicks=0,
                        className="global-filter-btn",
                    ),

                    html.Button(
                        "❌ Remove Global Filter",
                        id="remove-global-filter-btn",
                        n_clicks=0,
                        className="remove-filter-btn",
                    ),

                    html.Button(
                        "💾 Save Dashboard",
                        id="save-dashboard-btn",
                        n_clicks=0,
                        className="box",
                    ),

                    dcc.Download(id="download-dashboard"),

                    dcc.Upload(
                        id="upload-dashboard",
                        children=html.Button(
                            "📂 Load Dashboard",
                            className="upload-dashboard",
                        ),
                    ),

                    # 🔴 Logout Button (fixed via CSS)
                    html.Button(
                        "Logout",
                        id="logout-btn",
                        className="logout-btn",
                    ),
                ],
                style={
                    "display": "flex",
                    "alignItems": "center",
                    "gap": "10px",
                    "height": "6%",
                    "flexWrap": "wrap",
                },
            ),

            html.Hr(),

            # -----------------------------
            # GLOBAL FILTER
            # -----------------------------
            html.Div(
                id="global-filter-block",
                style={"display": "none"},
                children=[
                    html.H3("🌍 Global Filter"),
                    dcc.Dropdown(
                        id="global-filter-column",
                        options=column_options,
                    ),
                    dcc.Dropdown(
                        id="global-filter-values",
                        multi=True,
                    ),
                ],
            ),

            # -----------------------------
            # STORES
            # -----------------------------
            dcc.Store(id="global-filter-store"),
            dcc.Store(id="full-dashboard-store"),
            dcc.Store(id="chart-ids", data=[]),

            # -----------------------------
            # CHART CONTAINER
            # -----------------------------
            html.Div(id="charts-container", style={"height":"86%","overflow":"auto"}),
            
        ],
        style={
            "height": "100vh",
            "overflow": "auto",  # page scroll here
        },
    )
