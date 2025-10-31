# # Bike Preference Survey - Meaningful Data Visualization
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
#
# # Read CSV
# file_path = "Bike_preference_survey_updated.csv"  # Change path if needed
# df = pd.read_csv(file_path)
#
# # Create output folder
# os.makedirs("survey_graphs", exist_ok=True)
#
# # Drop unneeded columns
# drop_cols = ['Timestamp', 'Enter your name', 'Enter your email id']
# df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors='ignore')
#
# # Set style
# sns.set(style="whitegrid")
#
# # ===============================
# # 1️⃣ AGE GROUP DISTRIBUTION
# # ===============================
# if 'What  Age Group do you fall in' in df.columns:
#     plt.figure(figsize=(7,5))
#     sns.countplot(x='What  Age Group do you fall in', data=df, palette='viridis')
#     plt.title('Age Group Distribution of Respondents')
#     plt.xlabel('Age Group')
#     plt.ylabel('Count')
#     plt.xticks(rotation=30)
#     plt.tight_layout()
#     plt.savefig("survey_graphs/age_group_distribution.png")
#     plt.close()
#
# # ===============================
# # 2️⃣ GENDER DISTRIBUTION
# # ===============================
# if 'Kindly mention your gender' in df.columns:
#     plt.figure(figsize=(5,5))
#     df['Kindly mention your gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'))
#     plt.title('Gender Distribution')
#     plt.ylabel('')
#     plt.tight_layout()
#     plt.savefig("survey_graphs/gender_distribution.png")
#     plt.close()
#
# # ===============================
# # 3️⃣ BIKE OWNERSHIP
# # ===============================
# ownership_cols = [c for c in df.columns if 'own' in c.lower() and 'bike' in c.lower()]
# if ownership_cols:
#     col = ownership_cols[0]
#     plt.figure(figsize=(7,5))
#     sns.countplot(x=col, data=df, palette='mako')
#     plt.title('Do You Currently Own a Bike?')
#     plt.xlabel('Response')
#     plt.ylabel('Count')
#     plt.tight_layout()
#     plt.savefig("survey_graphs/bike_ownership.png")
#     plt.close()
#
# # ===============================
# # 4️⃣ PREFERRED BIKE TYPE
# # ===============================
# pref_cols = [c for c in df.columns if 'type' in c.lower() and 'bike' in c.lower()]
# if pref_cols:
#     col = pref_cols[0]
#     plt.figure(figsize=(8,5))
#     sns.countplot(x=col, data=df, palette='crest')
#     plt.title('Preferred Type of Bike')
#     plt.xlabel('Bike Type')
#     plt.ylabel('Count')
#     plt.xticks(rotation=30)
#     plt.tight_layout()
#     plt.savefig("survey_graphs/preferred_bike_type.png")
#     plt.close()
#
# # ===============================
# # 5️⃣ AGE GROUP VS PREFERRED BIKE TYPE
# # ===============================
# if 'What  Age Group do you fall in' in df.columns and pref_cols:
#     plt.figure(figsize=(8,5))
#     sns.countplot(x='What  Age Group do you fall in', hue=pref_cols[0], data=df, palette='cool')
#     plt.title('Age Group vs Preferred Bike Type')
#     plt.xlabel('Age Group')
#     plt.ylabel('Count')
#     plt.xticks(rotation=30)
#     plt.legend(title='Bike Type')
#     plt.tight_layout()
#     plt.savefig("survey_graphs/age_vs_bike_type.png")
#     plt.close()
#
# # ===============================
# # 6️⃣ FACTORS INFLUENCING BIKE PURCHASE
# # ===============================
# factor_cols = [c for c in df.columns if 'factor' in c.lower() or 'influence' in c.lower()]
# if factor_cols:
#     col = factor_cols[0]
#     plt.figure(figsize=(8,5))
#     sns.countplot(x=col, data=df, palette='flare')
#     plt.title('Factors Influencing Bike Purchase Decision')
#     plt.xlabel('Factor')
#     plt.ylabel('Count')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.savefig("survey_graphs/purchase_factors.png")
#     plt.close()
#
# # ===============================
# # 7️⃣ BIKE BRAND PREFERENCE
# # ===============================
# brand_cols = [c for c in df.columns if 'brand' in c.lower()]
# if brand_cols:
#     col = brand_cols[0]
#     plt.figure(figsize=(8,5))
#     sns.countplot(x=col, data=df, palette='plasma')
#     plt.title('Preferred Bike Brand')
#     plt.xlabel('Brand')
#     plt.ylabel('Count')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.savefig("survey_graphs/brand_preference.png")
#     plt.close()
#
# # ===============================
# # 8️⃣ PURPOSE OF BIKE USAGE
# # ===============================
# usage_cols = [c for c in df.columns if 'purpose' in c.lower() or 'usage' in c.lower()]
# if usage_cols:
#     col = usage_cols[0]
#     plt.figure(figsize=(8,5))
#     sns.countplot(x=col, data=df, palette='icefire')
#     plt.title('Purpose of Using a Bike')
#     plt.xlabel('Purpose')
#     plt.ylabel('Count')
#     plt.xticks(rotation=30)
#     plt.tight_layout()
#     plt.savefig("survey_graphs/purpose_of_bike_usage.png")
#     plt.close()
#
# print("✅ All meaningful graphs saved inside the 'survey_graphs' folder.")
# ===============================================
# Bike Preference Survey - Interactive Dashboard
# ===============================================

import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load CSV
file_path = "Bike_preference_survey_updated.csv"
df = pd.read_csv(file_path)

# Drop unneeded columns
drop_cols = ['Timestamp', 'Enter your name', 'Enter your email id']
df = df.drop(columns=[c for c in drop_cols if c in df.columns], errors='ignore')

# Identify dynamic columns
age_col = 'What  Age Group do you fall in'
gender_col = 'Kindly mention your gender'
ownership_col = next((c for c in df.columns if 'own' in c.lower() and 'bike' in c.lower()), None)
pref_col = next((c for c in df.columns if 'type' in c.lower() and 'bike' in c.lower()), None)
factor_col = next((c for c in df.columns if 'factor' in c.lower() or 'influence' in c.lower()), None)
brand_col = next((c for c in df.columns if 'brand' in c.lower()), None)
usage_col = next((c for c in df.columns if 'purpose' in c.lower() or 'usage' in c.lower()), None)

# Initialize Dash App
app = dash.Dash(__name__, title="Bike Preference Survey Dashboard")

# -----------------------------------------------
# Dashboard Layout
# -----------------------------------------------
app.layout = html.Div([
    html.H1("🏍️ Bike Preference Survey Dashboard", style={'textAlign': 'center', 'color': '#007BFF'}),

    html.Div([
        html.Div([
            html.Label("Filter by Gender:"),
            dcc.Dropdown(
                options=[{'label': g, 'value': g} for g in df[gender_col].unique()],
                id='gender_filter',
                placeholder='Select Gender',
                multi=True
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label("Filter by Age Group:"),
            dcc.Dropdown(
                options=[{'label': a, 'value': a} for a in df[age_col].unique()],
                id='age_filter',
                placeholder='Select Age Group',
                multi=True
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'padding': '10px'}),
    ], style={'textAlign': 'center'}),

    html.Hr(),

    # Graphs grid
    html.Div([
        dcc.Graph(id='age_distribution'),
        dcc.Graph(id='gender_distribution'),
        dcc.Graph(id='bike_type_preference'),
        dcc.Graph(id='age_vs_type'),
        dcc.Graph(id='brand_preference'),
        dcc.Graph(id='purpose_usage'),
    ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '15px'}),
])


# -----------------------------------------------
# Callbacks for Interactive Filtering
# -----------------------------------------------
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
    # 2️⃣ Gender Distribution
    fig2 = px.pie(
        dff, names=gender_col,
        title="Gender Distribution of Respondents",
        hole=0.3,
        color_discrete_sequence=px.colors.qualitative.Pastel  # ✅ fixed here
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

    # 5️⃣ Bike Brand Preference
    fig5 = px.bar(
        dff, x=brand_col, color=gender_col,
        title="Preferred Bike Brand",
        color_discrete_sequence=px.colors.sequential.Magma
    )

    # 6️⃣ Purpose of Bike Usage
    fig6 = px.bar(
        dff, x=usage_col, color=age_col,
        title="Purpose of Bike Usage",
        color_discrete_sequence=px.colors.sequential.Teal  # ✅ fixed palette
    )

    for f in [fig1, fig2, fig3, fig4, fig5, fig6]:
        f.update_layout(title_x=0.5, plot_bgcolor='white')

    return fig1, fig2, fig3, fig4, fig5, fig6


# -----------------------------------------------
# Run Server
# -----------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
