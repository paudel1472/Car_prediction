"""This create visualize data page"""

#Import necessary module

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_app(df):
    #Remove deprecation warning
    st.set_option('deprecation.showPyplotGlobalUse', False)

    #Give title
    st.title("Visualize Data")

    #Create a section for scatter plot
    st.header("Scatterplot")

    #Create a multi-select option to get x-axis from the user.
    feature_list = st.multiselect("Select x-axis values:", ('carwidth','enginesize','horsepower','drivewheel_fwd','car_company_buick'))

    for feature in feature_list:
        fig = plt.figure(figsize=(12,5))
        st.subheader(f"Scatter plot between {feature} and price")
        sns.scatterplot(x='price',y=feature,data=df)
        st.pyplot(fig)

    #Create a section for Visualization Selector
    st.header("Visualization Selector")

    #Create a multiselect option to create plots or charts.
    plot_type = st.multiselect("Select charts or plots:", ('Histogram','Box Plot','Correlation Heatmap'))

    #Create plot for histogram.
    if ("Histogram" in plot_type):
        st.subheader("Histogram")
        #Take column from user.
        hist_column = st.selectbox("Select the option to create its histogram", ('carwidth','enginesize','horsepower'))
        #Plot the chart
        fig = plt.figure(figsize=(12,5))
        plt.title(f"Histogram for {hist_column}")
        plt.hist(x=df[hist_column], bins = 'sturges', edgecolor = 'black')
        st.pyplot(fig)

    #Create plot for boxplot.
    if ("Box Plot" in plot_type):
        st.subheader("Boxplot")
        #Take column from user.
        box_column = st.selectbox("Select the option to create its boxplot", ('carwidth','enginesize','horsepower'))
        #Plot the chart
        fig = plt.figure(figsize=(12,2))
        plt.title(f"Box plot for {box_column}")
        sns.boxplot(df[box_column])
        st.pyplot(fig)

    #Create plot for Correlation Heatmap.
    if ("Correlation Heatmap" in plot_type):
        st.subheader("Correlation Heatmap")
        #Plot the chart
        fig = plt.figure(figsize=(12,10))
        ax = sns.heatmap(df.corr(), annot=True)
        bottom, top = ax.get_ylim() #Getting the top and bottom
        ax.set_ylim(bottom + 0.5, top-0.5) #Increaing the bottom
        st.pyplot(fig)