

import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State, ctx, no_update
from app import app
from database import validate_user, create_users_table, create_user
import smtplib
from email.mime.text import MIMEText

create_users_table()

EMAIL_SENDER = "as1513260@gmail.com"
EMAIL_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"   # 🔐 APP PASSWORD ONLY

def send_credentials_email(to_email, username, password):
    msg = MIMEText(f"""
Welcome 👋

Username: {username}
Password: {password}
""")
    msg["Subject"] = "Dashboard Login Credentials"
    msg["From"] = EMAIL_SENDER
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

# ----------------------------
# LOGIN UI (NO Location / Store HERE)
# ----------------------------
def login_layout():
    return dbc.Container(
        dbc.Row(
            dbc.Col(
                dbc.Card([
                    dbc.CardHeader("🔐 Login / Register", className="text-center"),
                    dbc.CardBody([

                        dbc.Input(id="login-username", placeholder="Username", className="mb-2"),
                        dbc.Input(id="login-password", placeholder="Password", type="password", className="mb-2"),
                        dbc.Input(id="register-email", placeholder="Email", type="email", className="mb-3"),

                        dbc.Button("Login", id="login-btn", color="primary", className="w-100 mb-2"),
                        dbc.Button("Register", id="register-btn", color="success", className="w-100"),

                        html.Div(id="login-msg", className="mt-3")
                    ])
                ], style={"maxWidth": "420px"}),
                className="d-flex justify-content-center"
            ),
            className="vh-100 align-items-center"
        ),
        fluid=True
    )

# ----------------------------
# AUTH CALLBACK
# ----------------------------
@app.callback(
    Output("session-user", "data"),
    Output("login-msg", "children"),
    Output("url", "pathname"),
    Input("login-btn", "n_clicks"),
    Input("register-btn", "n_clicks"),
    # Input("logout-btn", "n_clicks"),
    State("login-username", "value"),
    State("login-password", "value"),
    State("register-email", "value"),
    prevent_initial_call=True
)
def auth_handler(login_click, register_click, username, password, email):

    trigger = ctx.triggered_id

    if not username or not password:
        return None, dbc.Alert("Username & password required", color="warning"), no_update

    if trigger == "login-btn":
        user = validate_user(username, password)
        if user:
            return {"username": username}, dbc.Alert("Login successful ✅", color="success"), "/app"
        return None, dbc.Alert("Invalid credentials", color="danger"), no_update

    if trigger == "register-btn":
        if not email:
            return None, dbc.Alert("Email required", color="warning"), no_update

        create_user(username, password, email)
        send_credentials_email(email, username, password)
        return None, dbc.Alert("Registered! Check email 📧", color="success"), no_update

    return no_update, no_update, no_update


