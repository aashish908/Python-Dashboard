import dash
from dash import Dash
import json
import os
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    suppress_callback_exceptions=True,  # 🔥 IMPORTANT
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
# Add this for better error handling
app.config.suppress_callback_exceptions = True
app.enable_dev_tools(debug=True)

server = app.server
app.title = "📊 Advanced Multi-Chart Viewer"

def load_saved_dashboard():
    if os.path.exists("saved_dashboard.json"):
        with open("saved_dashboard.json", "r") as f:
            return json.load(f)
    return None
