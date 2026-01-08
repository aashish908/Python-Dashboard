# from dash import Output, Input, no_update
# from app import app


# def register_logout_callback():
#     @app.callback(
#         Output("session-user", "data"),
#         Output("url", "pathname"),
#         Input("logout-btn", "n_clicks"),
#         prevent_initial_call=True
#     )
#     def handle_logout(n_clicks):
#         if n_clicks:
#             print("LOGOUT CLICKED")  # 🔍 debug
#             return None, "/login"

#         return no_update, no_update
