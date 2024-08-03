import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load your data
df = pd.read_csv("https://raw.githubusercontent.com/hadilfs/Healthcare/main/combined_data.csv")
df = df[df['val'] > 0]

df1 = pd.read_csv("https://raw.githubusercontent.com/hadilfs/Healthcare/main/AllRegions.csv")
df1 = df1[df1['val'] > 0]

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "EDA", "Dashboard", "Conclusion"])

# Home page
if page == "Home":
    st.image("https://raw.githubusercontent.com/hadilfs/Healthcare/main/AUBlogo.png", use_column_width=True)
    st.markdown("<h1 style='text-align: center;'>Diabetes Type 2 Mortality in the MENA Region: A Comparative Analysis of Regional and Global Trends</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center;'>
        <h2>Healthcare Analytics</h2>
        <h3>Dr. Samar El-hajj</h3>
        <p><strong>Hadil Fares</strong><br>
        <strong>Tina Chalhoub</strong><br>
        <strong>Rawan Hallal</strong></p>
    </div>
    """, unsafe_allow_html=True)

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

    st.subheader("Distribution of Deaths by Age Group")
    df_sorted = df1.sort_values('age')
    plt.figure(figsize=(14, 6))
    sns.barplot(x='age', y='val', data=df_sorted, color='#8B0000', errorbar=None)
    plt.title('Distribution of Deaths by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Deaths (Percent)')
    plt.yticks([])
    st.pyplot(plt)
    
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
    
    st.subheader("Correlation Between Risk Factors and Deaths by Diabetes Type 2")
    plt.figure(figsize=(12, 6))
    correlation_matrix = df1.pivot_table(index='location', columns='rei', values='val').corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Risk Factors and Deaths by Diabetes Type 2')
    st.pyplot(plt)
    
    st.subheader("Distribution of Deaths by Region")
    region_distribution = df1.groupby('location')['val'].sum().reset_index()
    region_distribution = region_distribution.sort_values('val', ascending=False)
    plt.figure(figsize=(10, 8))
    plt.barh(region_distribution['location'], region_distribution['val'], color='#8B0000')
    plt.xlabel('Total Deaths (Percent)')
    plt.ylabel('Region')
    plt.title('Distribution of Deaths by Region')
    plt.xticks([])
    plt.grid(axis='y', linestyle='', alpha=0.7)
    st.pyplot(plt)
    
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

# Dashboard page
elif page == "Dashboard":
    st.title("Dashboard: Diabetes Type 2 Analysis in the MENA Region")

    # Set the width of the plots
    plot_width = 900
    plot_height = 600

    # First row of the dashboard with three plots
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown("<h5 style='text-align: center;'>Deaths by Diabetes Type 2 Over Time Globally</h5>", unsafe_allow_html=True)
        mena_data = df1.groupby('year')['val'].sum().reset_index()
        plt.figure(figsize=(plot_width / 90, plot_height / 90))
        plt.plot(mena_data['year'], mena_data['val'], marker='o', linestyle='-', color='#8B0000')
        plt.xlabel('Year')
        plt.ylabel('Total Deaths (Percent)')
        plt.yticks([])
        st.pyplot(plt)
    
    with col2:
        st.markdown("<h5 style='text-align: center;'>Distribution of Deaths by Region</h5>", unsafe_allow_html=True)
        region_distribution = df1.groupby('location')['val'].sum().reset_index()
        region_distribution = region_distribution.sort_values('val', ascending=False)
        plt.figure(figsize=(plot_width / 80, plot_height / 60))
        plt.barh(region_distribution['location'], region_distribution['val'], color='#8B0000')
        plt.xlabel('Total Deaths (Percent)')
        plt.ylabel('Region')
        st.pyplot(plt)
    
    with col3:
        st.markdown("<h5 style='text-align: center;'>Total Deaths by Year in the MENA Region</h5>", unsafe_allow_html=True)
        mena_data = df.groupby('year')['val'].sum().reset_index()
        plt.figure(figsize=(plot_width / 100, plot_height / 100))
        plt.plot(mena_data['year'], mena_data['val'], marker='o', linestyle='-', color='#8B0000')
        plt.xlabel('Year')
        plt.ylabel('Total Deaths (Percent)')
        plt.yticks([])
        st.pyplot(plt)

    # Second row of the dashboard with two plots
    col4, col5 = st.columns([1, 1])

    with col4:
        st.markdown("<h5 style='text-align: center;'>Distribution of Risk Factors Globally</h5>", unsafe_allow_html=True)
        risk_factors = df1.groupby('rei')['val'].sum().reset_index()
        fig = px.treemap(
            risk_factors,
            path=['rei'],
            values='val',
            color='val',
            color_continuous_scale='Reds'
        )
        fig.update_traces(marker=dict(line=dict(color='rgba(0,0,0,0)', width=0)))
        fig.update_layout(
            width=1200,
            height=100,
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig)
    
    with col5:
        st.markdown("<h5 style='text-align: center;'>Correlation Between Risk Factors and Deaths by Diabetes Type 2</h5>", unsafe_allow_html=True)
        plt.figure(figsize=(plot_width / 90, plot_height / 100))
        correlation_matrix = df1.pivot_table(index='location', columns='rei', values='val').corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        st.pyplot(plt)


# Conclusion page
elif page == "Conclusion":
    st.title("Conclusion and Findings")
    st.image("https://raw.githubusercontent.com/hadilfs/Healthcare/main/diabetesImage.jpg", use_column_width=True)
    
    st.write("""
    **1. Gender Differences in Diabetes Type 2 Mortality:**
    The side-by-side boxplot analysis reveals that mortality rates due to diabetes Type 2 are similar across genders, indicating that both males and females are equally affected. This suggests that public health interventions should adopt a gender-neutral approach, focusing on comprehensive strategies that address the broader population rather than targeting specific genders.
    
    **2. Age Group Analysis:**
    The data highlights a troubling trend with the highest percentage of deaths occurring in the 20-24 years age group. This alarming finding underscores the need for targeted awareness programs and health initiatives aimed at young adults. Enhancing early detection, promoting healthy lifestyles, and implementing educational programs in schools and colleges are crucial steps in addressing this issue.
    
    **3. Global Trends in Diabetes Type 2 Mortality:**
    The global analysis shows a rising trend in diabetes Type 2 mortality from 2011 to 2020, with a notable dip in 2018 followed by a sharp increase. This suggests a growing global burden of diabetes, with potential impacts from external factors such as pandemics. Strengthening global health initiatives, improving data quality, and advocating for effective public health policies are essential to address this trend.
    
    **4. Regional Risk Factors in MENA:**
    The treemap and heatmap analyses highlight that high body-mass index (BMI) is the dominant risk factor in the MENA region, with significant correlations to poor dietary choices and low physical activity. Addressing obesity through lifestyle interventions, promoting healthier diets, and increasing physical activity are vital for reducing diabetes-related deaths in the region.
    
    **5. Regional and Country-Specific Trends:**
    The horizontal bar chart and regional trend analysis reveal varying mortality rates across regions and countries. North America and MENA exhibit high mortality rates, while East Asia and Sub-Saharan Africa show lower rates. The need for tailored public health strategies and regional collaborations is evident to effectively manage diabetes across different socio-economic and cultural contexts.
    
    **6. Healthcare System Challenges and Strategies:**
    Access to care, quality of healthcare, and financial burdens are key challenges in the MENA region. Implementing telemedicine, improving healthcare quality through standardized protocols and training, and reducing costs through generic medications and preventive care are crucial strategies. Expanding health insurance, fostering public-private partnerships, and leveraging digital health solutions will further support effective diabetes management.
    
    **Conclusion Summary:**
    The findings from the Exploratory Data Analysis (EDA) underscore the complexity of diabetes Type 2 mortality across different demographics and regions. Addressing this global health challenge requires a multi-faceted approach that includes gender-neutral interventions, targeted age-specific programs, global and regional health initiatives, and comprehensive healthcare strategies. By focusing on both clinical and economic aspects, we can better manage and reduce the impact of diabetes Type 2, ultimately improving health outcomes and reducing the burden on healthcare systems worldwide.
    """)
    st.subheader("A Future Forecast of Deaths by Diabetes Type 2 in the MENA Region")
    st.image("https://raw.githubusercontent.com/hadilfs/Healthcare/main/forecastingResult.png", use_column_width=True)
    st.write("""Our forecasting analysis of Type 2 Diabetes mortality rates in the MENA region reveals a notable trend: the forecast indicates that the high levels of mortality observed in recent years are expected to persist into the foreseeable future. The analysis shows that after an initial period of increasing mortality, the rates have stabilized at elevated levels. This suggests that, barring significant public health interventions or changes in risk factors, the high mortality rates associated with Type 2 Diabetes are likely to remain constant in the coming years. Addressing this issue will require sustained efforts and targeted health policies to mitigate the impact and improve long-term outcomes.""")
