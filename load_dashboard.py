# from dash import Input, Output, State
# from dash.dependencies import ALL
# from app import app
# import json


# @app.callback(
#     Output("chart-ids", "data"),
#     Output({"type": "chart-store", "index": ALL}, "data"),
#     Output("global-filter-store", "data"),
#     Input("upload-dashboard", "contents"),
#     State("upload-dashboard", "filename"),
#     prevent_initial_call=True
# )
# def load_dashboard(contents, filename):

#     if not contents or not filename.endswith(".json"):
#         return [], [], {"column": None, "values": []}

#     # 🔹 Decode uploaded JSON
#     content_type, content_string = contents.split(",")
#     decoded = json.loads(content_string)

#     charts_dict = decoded.get("charts", {})
#     global_filter = decoded.get("global_filter", {"column": None, "values": []})

#     chart_ids = list(charts_dict.keys())
#     chart_data = list(charts_dict.values())

#     return chart_ids, chart_data, global_filter

from dash import Input, Output, State
from app import app
import json
import base64


@app.callback(
    Output("chart-ids", "data"),
    Output("global-filter-store", "data"),
    Output("full-dashboard-store", "data"),   # 👈 STORE FULL JSON
    Input("upload-dashboard", "contents"),
    State("upload-dashboard", "filename"),
    prevent_initial_call=True
)
def load_dashboard(contents, filename):

    if not contents or not filename.endswith(".json"):
        return [], {"column": None, "values": []}, {}

    # ✅ Decode base64 JSON
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string).decode("utf-8")
    dashboard_data = json.loads(decoded)

    charts_dict = dashboard_data.get("charts", {})
    global_filter = dashboard_data.get("global_filter", {"column": None, "values": []})

    chart_ids = list(charts_dict.keys())

    return chart_ids, global_filter, dashboard_data
