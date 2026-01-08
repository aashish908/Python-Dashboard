from dash import Output, Input, MATCH, html
from app import app
from dashboard import df
import pandas as pd
import plotly.express as px


# ---------------------------------------------------------
# UPDATE CHART / TABLE / KPI FROM STORED CONFIG
# ---------------------------------------------------------
@app.callback(
    Output({'type': 'chart-output', 'index': MATCH}, 'figure'),
    Output({'type': 'table-output', 'index': MATCH}, 'children'),
    Output({'type': 'kpi-output', 'index': MATCH}, 'children'),
    Output({'type': 'total-responses', 'index': MATCH}, 'children'),
    Input({'type': 'chart-store', 'index': MATCH}, 'data'),
    Input("global-filter-store", "data"),
)
def update_chart_from_store(store_data, global_filter):

    # 🔒 SAFETY CHECK
    if not store_data:
        return {}, "", "", ""

    # -------------------------------------------------
    # APPLY GLOBAL FILTER (SAFE)
    # -------------------------------------------------
    filtered_df = df.copy()

    if (
        global_filter
        and global_filter.get("column")
        and global_filter.get("values")
    ):
        filtered_df = filtered_df[
            filtered_df[global_filter["column"]]
            .astype(str)
            .isin(global_filter["values"])
        ]

    # -------------------------------------------------
    # READ CONFIG
    # -------------------------------------------------
    selected_columns = store_data.get("selected_columns", [])
    chart_type = store_data.get("chart_type")
    mapping = store_data.get("mapping")
    color_input = store_data.get("color_input")
    selected_values = store_data.get("selected_values")
    display_mode = store_data.get("display_mode", "count")

    if not selected_columns:
        return {}, "", "", ""

    # -------------------------------------------------
    # VALUE MAPPING
    # -------------------------------------------------
    value_map = {}
    if mapping:
        for item in mapping.split(","):
            if "=" in item:
                k, v = item.split("=")
                value_map[k.strip()] = v.strip()

    user_colors = (
        [c.strip() for c in color_input.split(",") if c.strip()]
        if color_input
        else px.colors.qualitative.Set3
    )

    combined_counts = pd.DataFrame()

    # -------------------------------------------------
    # CALCULATE COUNTS
    # -------------------------------------------------
    for col in selected_columns:
        original = filtered_df[col].dropna().astype(str)

        if value_map:
            original = original.map(value_map).fillna(original)

        total_responses = len(original)

        filtered = (
            original[original.isin(selected_values)]
            if selected_values
            else original
        )

        counts = filtered.value_counts().reset_index()
        counts.columns = ["Value", "Count"]
        counts["Column"] = col
        counts["Total_In_Column"] = total_responses

        counts["Percentage"] = (
            (counts["Count"] / total_responses) * 100
            if display_mode == "percentage" and total_responses > 0
            else counts["Count"]
        )

        combined_counts = pd.concat(
            [combined_counts, counts], ignore_index=True
        )

    total_text = f"Total Responses: {len(filtered_df)}"

    # -------------------------------------------------
    # KPI
    # -------------------------------------------------
    if chart_type == "kpi":
        col = selected_columns[0]
        kpi_value = combined_counts[
            combined_counts["Column"] == col
        ]["Count"].sum()

        return {}, "", html.Div([
            html.H4(col, style={"textAlign": "center"}),
            html.H1(f"{kpi_value:,}", style={
                "textAlign": "center",
                "color": "#2ecc71"
            })
        ]), total_text

    # -------------------------------------------------
    # TABLE
    # -------------------------------------------------
    if chart_type == "table":
        df_show = combined_counts.copy()
        df_show["Percentage"] = df_show["Percentage"].round(2)

        table = html.Table(
            [
                html.Thead(html.Tr([
                    html.Th(c) for c in df_show.columns
                ])),
                html.Tbody([
                    html.Tr([
                        html.Td(v) for v in row
                    ]) for row in df_show.values
                ])
            ],
            style={
                "margin": "auto",
                "border": "1px solid #ccc"
            }
        )

        return {}, table, "", total_text

    # -------------------------------------------------
    # PIE / DONUT
    # -------------------------------------------------
    if chart_type in ["pie", "donut"]:
        pie_data = combined_counts[
            combined_counts["Column"] == selected_columns[0]
        ]

        fig = px.pie(
            pie_data,
            names="Value",
            values="Count",
            hole=0.5 if chart_type == "donut" else 0,
            color_discrete_sequence=user_colors
        )
        fig.update_layout(title_x=0.5)

        return fig, "", "", total_text

    # -------------------------------------------------
    # BAR / COLUMN
    # -------------------------------------------------
    y_col = "Percentage" if display_mode == "percentage" else "Count"

    fig = px.bar(
        combined_counts,
        x="Value" if chart_type == "column" else "Column",
        y=y_col,
        color="Value",
        barmode="group",
        color_discrete_sequence=user_colors
    )
    fig.update_layout(title_x=0.5)

    return fig, "", "", total_text
