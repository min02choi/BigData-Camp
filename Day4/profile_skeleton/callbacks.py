import plotly.express as px
from dash.dependencies import Input, Output
from plotly import graph_objects as go

from utils import MBTI, random_avatar


def get_callbacks(app):
    @app.callback(
        Output(),
        Input("avatar-button", "n_clicks"),
    )
    def update_avater():