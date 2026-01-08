# # components.py
# from dash import html, dcc

# def create_chart_block(cid):
#     return html.Div(
#         id={"type": "chart-block", "index": cid},
#         children=[
#             html.H3(f"Chart {cid}"),
#             dcc.Graph(id={"type": "chart-graph", "index": cid}),
#             html.Button("Remove", id={"type": "remove-chart-btn", "index": cid})
#         ]
#     )
