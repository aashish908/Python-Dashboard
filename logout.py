# from dash import Output, Input, no_update
# from app import app

# @app.callback(
#     Output("session-user", "data"),
#     Output("url", "pathname"),
#     Input("logout-btn", "n_clicks"),
#     prevent_initial_call=True
# )
# def logout_user(n_clicks):
#     if n_clicks:
#         return None, "/login"   # 🔥 session clear + redirect
#     return no_update, no_update
