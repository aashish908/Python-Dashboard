import dash
from dash import Dash
import json
import os
import dash_bootstrap_components as dbc

# app = dash.Dash(__name__)
app = Dash(
    __name__,
    suppress_callback_exceptions=True,  # 🔥 IMPORTANT
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server
app.title = "📊 Advanced Multi-Chart Viewer"

def load_saved_dashboard():
    if os.path.exists("saved_dashboard.json"):
        with open("saved_dashboard.json", "r") as f:
            return json.load(f)
    return None
