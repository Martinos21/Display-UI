import dash
from dash import html,dcc, Input, Output
import dash_bootstrap_components as dbc
import paho.mqtt.client as mqtt

global current_temperature
current_temperature = "NaN"

##############################################################
mqttc = mqtt.Client()
mqttc.connect("broker.hivemq.com", 1883, 60)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttc.subscribe("myroom/temperature")

def on_message(client, userdata, msg):
    global current_temperature
    current_temperature = msg.payload.decode()

mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.loop_start()

##############################################################
app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

card = dbc.Card(
    html.H4(id="temperature")
)

app.layout = dbc.Container(
    [
        dcc.Interval(id='update', n_intervals=0, interval=1000*3),
        html.H1("Monitoring IoT Sensor Data with Plotly Dash"),
        html.Hr(),
        dbc.Row(dbc.Col(card, lg=4))
    ]
)

@app.callback(
    Output('temperature', 'children'),
    Input('update', 'n_intervals')
)

def update_temperature(timer):
    return ("Temperature: " + str(current_temperature))

if __name__ == "__main__":
    app.run_server(debug=True)
