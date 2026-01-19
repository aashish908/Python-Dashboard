from dash import Input, Output, no_update, ctx
from app import app

FILTER_STYLE = {
    "padding": "10px",
    "margin": "15px 0",
    "border": "2px solid #3498db",
    "borderRadius": "8px",
    "backgroundColor": "#eef7ff",
    "display": "block"
}

@app.callback(
    Output("global-filter-block", "style"),
    Output("show-global-filter-btn", "style"),
    Input("show-global-filter-btn", "n_clicks"),
    Input("remove-global-filter-btn", "n_clicks"),
    prevent_initial_call=True
)
def toggle_global_filter(show_clicks, remove_clicks):
    trigger = ctx.triggered_id

    if trigger == "show-global-filter-btn":
        return FILTER_STYLE, {"display": "none"}

    if trigger == "remove-global-filter-btn":
        return {"display": "none"}, {"display": "inline-block"}

    return no_update, no_update
