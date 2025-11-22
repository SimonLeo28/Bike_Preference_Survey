# Bike Preference Survey Python Dashboard
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load and clean dataset
file_path = "Bike_preference_survey_updated.csv"
df = pd.read_csv(file_path)

# Drop unneeded columns (you already removed Timestamp)
drop_cols = ['Enter your name', 'Enter your email id']
df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors='ignore')

# Define important columns manually (for reliability)
age_col = 'What  Age Group do you fall in'
gender_col = 'Kindly mention your gender'
ownership_col = 'Do you currently own a two-wheeler?'
pref_col = 'According to your age group, which bike type is most suitable?  '
brand_col = 'When choosing a bike, which feature is most important to you?  '
usage_col = 'Do you currently own a two-wheeler?'  # reuse as "purpose/usage"

# Initialize Dash App
app = dash.Dash(__name__, title="Bike Preference Survey Dashboard")

# Dashboard Layout
app.layout = html.Div([
    html.H1("🏍️ Bike Preference Survey Dashboard",
            style={'textAlign': 'center', 'color': '#007BFF'}),

    # Filters
    html.Div([
        html.Div([
            html.Label("Filter by Gender:"),
            dcc.Dropdown(
                options=[{'label': g, 'value': g} for g in sorted(df[gender_col].dropna().unique())],
                id='gender_filter',
                placeholder='Select Gender',
                multi=True
            ),
        ], style={'width': '40%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label("Filter by Age Group:"),
            dcc.Dropdown(
                options=[{'label': a, 'value': a} for a in sorted(df[age_col].dropna().unique())],
                id='age_filter',
                placeholder='Select Age Group',
                multi=True
            ),
        ], style={'width': '40%', 'display': 'inline-block', 'padding': '10px'}),
    ], style={'textAlign': 'center'}),

    html.Hr(),

    # Graphs
    html.Div([
        dcc.Graph(id='age_distribution'),
        dcc.Graph(id='gender_distribution'),
        dcc.Graph(id='bike_type_preference'),
        dcc.Graph(id='age_vs_type'),
        dcc.Graph(id='brand_preference'),
        dcc.Graph(id='purpose_usage'),
    ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '15px'})
])

# Interactive Callback
@app.callback(
    [Output('age_distribution', 'figure'),
     Output('gender_distribution', 'figure'),
     Output('bike_type_preference', 'figure'),
     Output('age_vs_type', 'figure'),
     Output('brand_preference', 'figure'),
     Output('purpose_usage', 'figure')],
    [Input('gender_filter', 'value'),
     Input('age_filter', 'value')]
)
def update_graphs(selected_genders, selected_ages):
    dff = df.copy()

    # Apply filters
    if selected_genders:
        dff = dff[dff[gender_col].isin(selected_genders)]
    if selected_ages:
        dff = dff[dff[age_col].isin(selected_ages)]

    # 1️⃣ Age Group Distribution
    fig1 = px.histogram(
        dff, x=age_col, color=gender_col,
        title="Age Group Distribution",
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    # 2️⃣ Gender Distribution
    fig2 = px.pie(
        dff, names=gender_col,
        title="Gender Distribution of Respondents",
        hole=0.3,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    # 3️⃣ Preferred Bike Type
    fig3 = px.bar(
        dff, x=pref_col, color=gender_col,
        title="Preferred Bike Type",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )

    # 4️⃣ Age Group vs Bike Type
    fig4 = px.histogram(
        dff, x=age_col, color=pref_col,
        title="Age Group vs Preferred Bike Type",
        barmode='group',
        color_discrete_sequence=px.colors.qualitative.Dark24
    )

    # 5️⃣ Feature Importance (acts as Brand Preference)
    fig5 = px.bar(
        dff, x=brand_col, color=gender_col,
        title="Feature Importance when Choosing a Bike",
        color_discrete_sequence=px.colors.sequential.Magma
    )

    # 6️⃣ Two-wheeler Ownership (acts as Purpose/Usage)
    fig6 = px.bar(
        dff, x=usage_col, color=age_col,
        title="Bike Ownership across Age Groups",
        color_discrete_sequence=px.colors.sequential.Teal
    )

    # Common formatting
    for f in [fig1, fig2, fig3, fig4, fig5, fig6]:
        f.update_layout(title_x=0.5, plot_bgcolor='white')

    return fig1, fig2, fig3, fig4, fig5, fig6

# Run the App
if __name__ == '__main__':
    app.run(debug=True)