import pandas as pd
import tkinter as tk
from tkinter import filedialog
import dash
from dash import dcc, html, Output, Input, State, ctx
from dash.dependencies import MATCH, ALL
import plotly.express as px
import uuid
from app import app
from dashboard import df, column_options
from style import create_chart_block
# from layout import layout
import call_back 
import style
import chart_render_callbacks
import global_filters 
import chart_store_callbacks
import call_back
import chart_column_rules
import chart_update_callbacks
import save_dashboard
# import load_dashboard

# app.layout = layout

from dash import html, dcc, Input, Output
from app import app
from layout import dashboardaa_layout
from login import login_layout
# import login
# import logout
# from logout import register_logout_callback


# MAIN APP LAYOUT
# -----------------------------
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),   # 🔑 REQUIRED FOR REDIRECT
    dcc.Store(id="session-user", storage_type="session"),
    html.Div(id="page-content")
])

# Page routing

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    Input("session-user", "data")
)
def render_page(pathname,user):
       # 🔐 NOT LOGGED IN
    
    if pathname in ["/", "/login"]:
        return login_layout() if not user else dashboardaa_layout()

    # 🔐 Protected dashboard
    
    if pathname == "/app":
        return dashboardaa_layout() if user else login_layout()

    # # ❌ UNKNOWN ROUTE
    return html.H3("404 - Page not found")
    # return login_layout()
    
        # 🔐 Protected dashboard
    # if pathname == "/app":
    #     if user:
    #         return layout
    #     return login_layout()

    # # 🔓 Default route
    # return login_layout()



if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

# if __name__ == "__main__":
#     app.run(debug=True)