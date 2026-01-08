from dash import Output, Input, State, ALL, dcc
from app import app
import json


@app.callback(
    Output("download-dashboard", "data"),
    Input("save-dashboard-btn", "n_clicks"),
    State("chart-ids", "data"),
    State({"type": "chart-store", "index": ALL}, "data"),
    State("global-filter-store", "data"),
    prevent_initial_call=True
)
def save_dashboard(n_clicks, chart_ids, charts_data, global_filter):

    # 🔹 Build charts dictionary → {chart_id: config}
    charts_dict = {}

    for chart_id, chart_config in zip(chart_ids, charts_data):
        charts_dict[chart_id] = chart_config

    # 🔹 Final dashboard state (YOUR REQUIRED FORMAT)
    dashboard_state = {
        "charts": charts_dict,
        "global_filter": global_filter
    }

    # 🔹 Save JSON file
    file_path = "saved_dashboard.json"
    with open(file_path, "w") as f:
        json.dump(dashboard_state, f, indent=4)

    # 🔹 Download file
    return dcc.send_file(file_path)
