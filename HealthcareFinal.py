import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
df = pd.read_csv("https://raw.githubusercontent.com/hadilfs/Healthcare/main/combined_data.csv")
df = df[df['val'] > 0]

df1 = pd.read_csv("https://raw.githubusercontent.com/hadilfs/Healthcare/main/AllRegions.csv")
df1 = df1[df1['val'] > 0]

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "EDA", "Conclusion"])

# Home page
if page == "Home":
    st.image("https://raw.githubusercontent.com/hadilfs/Healthcare/main/AUBlogo.png", use_column_width=True)
    st.title("Diabetes Type 2 Mortality in the MENA Region: A Comparative Analysis of Regional and Global Trends")
    st.subheader("**Healthcare Analytics**\n**Dr. Samar El-hajj**")
    st.write("**Hadil Fares**")
    st.write("**Tina Chalhoub**")
    st.write("**Rawan Hallal**")
    
# EDA page
elif page == "EDA":
    st.title("Exploratory Data Analysis")
    
    st.subheader("Deaths by Diabetes Type 2 by Sex")
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='sex', y='val', data=df1, palette=['#8B0000', '#d19999'])
    plt.title('Deaths by Diabetes Type 2 by Sex')
    plt.xlabel('Sex')
    plt.ylabel('Deaths (Percent)')
    plt.yticks([])
    st.pyplot(plt)
    st.write("**Explanation**")

    st.subheader("Distribution of Deaths by Age Group")
    df_sorted = df1.sort_values('age')
    plt.figure(figsize=(14, 6))
    sns.barplot(x='age', y='val', data=df_sorted, color='#8B0000', errorbar=None)
    plt.title('Distribution of Deaths by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Deaths (Percent)')
    plt.yticks([])
    st.pyplot(plt)
    st.write("**Explanation**")
    
    st.subheader("Deaths by Diabetes Type 2 Over Time Globally")
    mena_data = df1.groupby('year')['val'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(mena_data['year'], mena_data['val'], marker='o', linestyle='-', color='#8B0000')
    plt.title('Deaths by Diabetes Type 2 Over Time Globally')
    plt.xlabel('Year')
    plt.ylabel('Total Deaths (Percent)')
    plt.yticks([])
    plt.grid(False)
    st.pyplot(plt)
    st.write("**Explanation**")
    
    st.subheader("Distribution of Risk Factors Globally")
    risk_factors = df1.groupby('rei')['val'].sum().reset_index()
    fig = px.treemap(
        risk_factors,
        path=['rei'],
        values='val',
        title='Distribution of Risk Factors Globally',
        color='val',
        color_continuous_scale='Reds'
    )
    fig.update_traces(marker=dict(line=dict(color='rgba(0,0,0,0)', width=0)))
    fig.update_layout(
        width=900,
        height=500,
        margin=dict(t=50, b=50, l=50, r=50)
    )
    st.plotly_chart(fig)
    st.write("**Explanation**")
    
    st.subheader("Correlation Between Risk Factors and Deaths by Diabetes Type 2")
    plt.figure(figsize=(12, 6))
    correlation_matrix = df1.pivot_table(index='location', columns='rei', values='val').corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Risk Factors and Deaths by Diabetes Type 2')
    st.pyplot(plt)
    st.write("**Explanation**")
    
    st.subheader("Distribution of Deaths by Region")
    region_distribution = df1.groupby('location')['val'].sum().reset_index()
    region_distribution = region_distribution.sort_values('val', ascending=False)
    plt.figure(figsize=(10, 5))
    plt.barh(region_distribution['location'], region_distribution['val'], color='#8B0000')
    plt.xlabel('Total Deaths (Percent)')
    plt.ylabel('Region')
    plt.title('Distribution of Deaths by Region')
    plt.xticks([])
    plt.grid(axis='y', linestyle='', alpha=0.7)
    st.pyplot(plt)
    st.write("**Explanation**")
    
    st.subheader("Total Deaths by Year in the MENA Region")
    mena_data = df.groupby('year')['val'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    plt.plot(mena_data['year'], mena_data['val'], marker='o', linestyle='-', color='#8B0000')
    plt.title('Total Deaths by Year in the MENA Region')
    plt.xlabel('Year')
    plt.ylabel('Total Deaths (Percent)')
    plt.yticks([])
    plt.grid(False)
    st.pyplot(plt)
    st.write("**Explanation**")
    
    st.subheader("Trends in Deaths by Diabetes Type 2 Over Time")
    plt.figure(figsize=(16, 12))
    ax = sns.lineplot(x='year', y='val', hue='location', data=df, errorbar=None, legend=False)
    locations = df['location'].unique()
    for location in locations:
        line = ax.get_lines()[list(df['location'].unique()).index(location)]
        color = line.get_color()
        x_data = line.get_xdata()
        y_data = line.get_ydata()
        if len(x_data) > 0 and len(y_data) > 0:
            ax.text(x_data[-1], y_data[-1], location, color=color, ha='left', va='center', fontsize=10)
    plt.title('Trends in Deaths by Diabetes Type 2 Over Time')
    plt.xlabel('Year')
    plt.ylabel('Deaths (Percent)')
    plt.yticks([])
    st.pyplot(plt)
    st.write("**Explanation**")
    
    st.subheader("Distribution of Deaths by Country in the MENA Region")
    country_distribution = df.groupby('location')['val'].sum().reset_index()
    country_distribution = country_distribution.sort_values('val', ascending=False)
    num_colors = len(country_distribution)
    colors = plt.cm.Reds([i / num_colors for i in range(num_colors)])
    plt.figure(figsize=(10, 5))
    plt.pie(
        country_distribution['val'], 
        labels=country_distribution['location'], 
        colors=colors, 
        startangle=140
    )
    plt.title('Distribution of Deaths by Country in the MENA Region')
    plt.axis('equal')
    st.pyplot(plt)
    st.write("**Explanation**")

# Conclusion page
elif page == "Conclusion":
    st.title("Conclusion and Findings")
    st.write("**Explanation and findings will be added here**")
    
