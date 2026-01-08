# value_filter_callbacks.py

from dash import Output, Input, MATCH
from app import app
from dashboard import df


# ------------------ UPDATE FILTER OPTIONS ------------------
@app.callback(
    Output({'type': 'value-filter-dropdown', 'index': MATCH}, 'options'),
    Input({'type': 'columns-dropdown', 'index': MATCH}, 'value'),
    Input({'type': 'value-mapping-input', 'index': MATCH}, 'value')
)
def update_filter_dropdown(columns, mapping):

    if not columns:
        return []

    value_map = {}

    if mapping:
        try:
            for item in mapping.split(','):
                if '=' in item:
                    k, v = item.split('=')
                    value_map[k.strip()] = v.strip()
        except Exception:
            pass

    values = set()

    for col in columns:
        col_data = df[col].dropna().astype(str)

        if value_map:
            col_data = col_data.map(value_map).fillna(col_data)

        values.update(col_data.unique())

    return [{"label": v, "value": v} for v in sorted(values)]
