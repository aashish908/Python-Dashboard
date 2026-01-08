import uuid
from dash import Output, Input, State, ALL, ctx
from app import app   # IMPORTANT: import your Dash app

# --------------------------
#  Function to manage list
# --------------------------
def manage_chart_ids(n_add, n_remove_list, chart_ids):
    triggered = ctx.triggered_id

    if chart_ids is None:
        chart_ids = []

    if not triggered:
        return chart_ids

    # ➕ Add Chart
    if triggered == "add-chart-btn":
        return chart_ids + [str(uuid.uuid4())]

    # ❌ Remove Chart
    if isinstance(triggered, dict) and triggered.get("type") == "remove-chart-btn":
        remove_id = triggered.get("index")
        return [cid for cid in chart_ids if cid != remove_id]

    return chart_ids


# --------------------------
#  Callback Wrapper
# --------------------------
@app.callback(
    Output("chart-ids", "data", allow_duplicate=True),  # ⭐ FIX ⭐
    Input("add-chart-btn", "n_clicks"),
    Input({'type': 'remove-chart-btn', 'index': ALL}, "n_clicks"),
    State("chart-ids", "data"),
    prevent_initial_call=True
)
def update_chart_ids(n_add, n_remove_list, chart_ids):
    return manage_chart_ids(n_add, n_remove_list, chart_ids)
