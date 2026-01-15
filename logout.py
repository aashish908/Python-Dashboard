# logout.py
from dash import Input, Output, no_update
from app import app

@app.callback(
    Output("session-user", "data", allow_duplicate=True),
    Output("url", "pathname", allow_duplicate=True),
    Input("logout-btn", "n_clicks"),
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    print(f"LOGOUT: Button clicked {n_clicks} times")
    if n_clicks:
        return None, "/login"
    return no_update, no_update
