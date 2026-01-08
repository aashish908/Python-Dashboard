from dash import Output, Input, State, MATCH
from app import app


# ----------------------------------------------------
# ⭐ ENFORCE SINGLE COLUMN FOR PIE / DONUT / KPI
# ----------------------------------------------------
@app.callback(
    Output({'type': 'columns-dropdown', 'index': MATCH}, 'value'),
    Input({'type': 'chart-type-dropdown', 'index': MATCH}, 'value'),
    State({'type': 'columns-dropdown', 'index': MATCH}, 'value'),
    prevent_initial_call=True
)
def enforce_single_column(chart_type, selected_columns):
    """
    For chart types that require only one column (pie, donut, kpi),
    automatically reduce the selected column list to a single value.
    """
    if chart_type in ["pie", "donut", "kpi"] and selected_columns and len(selected_columns) > 1:
        return [selected_columns[0]]

    return selected_columns
