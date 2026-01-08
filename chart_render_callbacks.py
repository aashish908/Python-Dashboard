from dash import Output, Input, State
from app import app
from style import create_chart_block   # <-- You must import your chart block generator
# from style import create_global_filter_block


# ---------------------------------------------
#  Callback: Render charts dynamically
# ---------------------------------------------
@app.callback(
    Output("charts-container", "children"),
    Input("chart-ids", "data"),
    State("charts-container", "children"),
    prevent_initial_call=True
)
def render_charts(chart_ids, existing_charts):
    if existing_charts is None:
        existing_charts = []

    # Convert existing chart list into a dictionary for faster lookup
    existing_dict = {}
    for chart in existing_charts:
        try:
            cid = chart["props"]["id"]["index"]
            existing_dict[cid] = chart
        except:
            pass

    output_charts = []

    # Preserve old charts OR create new ones
    for cid in chart_ids:
        if cid in existing_dict:
            output_charts.append(existing_dict[cid])   # Keep old chart
        else:
            output_charts.append(create_chart_block(cid))  # Create a new chart block

    return output_charts
