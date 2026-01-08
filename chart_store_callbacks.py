from dash import Output, Input, State, MATCH
from app import app


# ----------------------------------------------------
# ⭐ UPDATE INDIVIDUAL CHART STORE (MATCHED CALLBACK)
# ----------------------------------------------------
@app.callback(
    Output({'type': 'chart-store', 'index': MATCH}, 'data'),
    Input({'type': 'columns-dropdown', 'index': MATCH}, 'value'),
    Input({'type': 'chart-type-dropdown', 'index': MATCH}, 'value'),
    Input({'type': 'value-mapping-input', 'index': MATCH}, 'value'),
    Input({'type': 'color-input', 'index': MATCH}, 'value'),
    Input({'type': 'value-filter-dropdown', 'index': MATCH}, 'value'),
    Input({'type': 'display-mode-radio', 'index': MATCH}, 'value'),
    State({'type': 'chart-store', 'index': MATCH}, 'data'),
    prevent_initial_call=True
)
def update_chart_store(columns, chart_type, mapping, color_input, selected_values, display_mode, current_store):
    """
    Update the store for each chart independently based on MATCH index.
    """

    # Update all fields inside the per-chart store
    current_store["selected_columns"] = columns
    current_store["chart_type"] = chart_type
    current_store["mapping"] = mapping
    current_store["color_input"] = color_input
    current_store["selected_values"] = selected_values
    current_store["display_mode"] = display_mode

    return current_store
