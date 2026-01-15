import pandas as pd
import tkinter as tk
from tkinter import filedialog
from dash import dcc, html, Output, Input
from dash.dependencies import MATCH, ALL
import plotly.express as px
import uuid

from app import app
from dashboard import df, column_options
from style import create_chart_block

import style
import call_back
import chart_render_callbacks
import global_filters
import chart_store_callbacks
import chart_column_rules
import chart_update_callbacks
import save_dashboard
# import logout   # 🔥 IMPORTANT (callback register hoga)

from layout import dashboardaa_layout
from login import login_layout
import logout


# -----------------------------
# MAIN APP LAYOUT
# -----------------------------
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    dcc.Store(id="session-user", storage_type="session"),
    html.Div(id="page-content")
])


# -----------------------------
# PAGE ROUTING
# -----------------------------
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    Input("session-user", "data")
)
def render_page(pathname, user):
    print(f"ROUTING: pathname={pathname}, user={user}")

    if pathname in ["/", "/login"]:
        return login_layout()

    if pathname == "/app":
        if user:
            return dashboardaa_layout()
        return login_layout()

    return html.H3("404 - Page not found")


# if __name__ == "__main__":
#     app.run(debug=False, use_reloader=False)

if __name__ == "__main__":
    print("Starting app...")
    print(f"Registered callbacks: {len(app.callback_map)}")
    app.run(debug=True, use_reloader=False, port=8050)