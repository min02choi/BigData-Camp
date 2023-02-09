import os

from dash import Dash, dcc, html

from callbacks import get_callbacks
from utils import MBTI

app = Dash(__name__)


def user_controls():
    return html.Div(
        [
            html.Label("이름"),
            dcc.Input(placeholder="아무개", type="text"),
            dcc.Input(),
            html.Label("나이"),
            dcc.Input(placeholder="20", type="number"),
            dcc.Input(),
            html.Label("MBTI"),
            dcc.Dropdown(),
            html.Label("아바타 재설정"),
            html.Button(),

        ],
        className="three columns div-user-controls",
    )


def profile():
    return html.Div(
        [
            
        ],
        className="nine columns bg-grey",
        style={
            "display": "flex",
            "flex-direction": "column",
            "flex-grow": 1,
        },
    )


app.layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                user_controls(),
                profile(),
            ],
        )
    ]
)

get_callbacks(app)

# Remove all svg files is assets folder
for file in os.listdir("assets"):
    if file.endswith(".svg"):
        os.remove(os.path.join("assets", file))


if __name__ == "__main__":
    app.run_server(debug=True)
