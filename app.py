import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Criar dados fictícios de vendas
data = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto B', 'Produto C'],
    'Vendas': [100, 150, 200, 300, 250, 400],
    'Mês': ['Janeiro', 'Janeiro', 'Janeiro', 'Fevereiro', 'Fevereiro', 'Fevereiro']
}
df = pd.DataFrame(data)

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Definir o layout do aplicativo
app.layout = html.Div([
    html.H1("Dashboard de Vendas"),
    dcc.Dropdown(
        id='dropdown-produto',
        options=[{'label': produto, 'value': produto} for produto in df['Produto'].unique()],
        value='Produto A'
    ),
    dcc.Graph(id='grafico-vendas')
])

# Definir callback para atualizar o gráfico
@app.callback(
    Output('grafico-vendas', 'figure'),
    [Input('dropdown-produto', 'value')]
)
def update_graph(selected_product):
    filtered_df = df[df['Produto'] == selected_product]
    fig = px.bar(filtered_df, x='Mês', y='Vendas', title=f'Vendas de {selected_product}')
    return fig

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
