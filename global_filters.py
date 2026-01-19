from dash import Output, Input, State,ctx,  no_update
from app import app
from dashboard import df


# ----------------------------------------------------
# ⭐ UPDATE FILTER VALUES BASED ON SELECTED COLUMN
# ----------------------------------------------------
@app.callback(
    Output("global-filter-values", "options"),
    Input("global-filter-column", "value")
)
def update_global_filter_values(column):
    if not column:
        return []

    values = (
        df[column]
        .dropna()
        .astype(str)
        .unique()
    )

    return [{"label": v, "value": v} for v in sorted(values)]


# ----------------------------------------------------
# ⭐ STORE GLOBAL FILTER STATE
# ----------------------------------------------------
@app.callback(
    Output("global-filter-store", "data"),
    Input("global-filter-column", "value"),
    Input("global-filter-values", "value"),
    prevent_initial_call=True
)
def store_global_filter(column, values):
    return {
        "column": column,
        "values": values or []
    }


# ----------------------------------------------------
# ⭐ SHOW / HIDE THE GLOBAL FILTER BLOCK
# ----------------------------------------------------
# @app.callback(
#     Output("global-filter-block", "style"),
#     Input("show-global-filter-btn", "n_clicks"),
# )

def toggle_global_filter(n):
    # ❌ No click → keep hidden
    if not n or n == 0:
        return {"display": "none"}

    # ✅ After first click → show block
    return {
        "padding": "10px",
        "margin": "15px 0",
        "border": "2px solid #3498db",
        "borderRadius": "8px",
        "backgroundColor": "#eef7ff",
        "display": "block"
    }

