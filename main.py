import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D

st.title('Analyzing Laptops and Their Prices')
st.write('')
st.write('')

"## GROUP 4 - BM3"

st.write("The purpose of this is to convert our previous Data Visualization activity in Google Colab Notebook into a Streamlit Web Application")
st.markdown("Also check the [GitHub Repository](https://github.com/Larence2005/Group-4-Laptop-Prices) for the source code.")
st.write('')
"# Describing the Dataset"

df = pd.read_csv("laptop_price - dataset.csv")
df

df.info()

st.write("The sum of each categorical column can be seen below")

sum = df.isna().sum()
sum

desc = df.describe()
desc

"# Company Column"

company = df['Company'].value_counts()
company

#Screen Resolution Bar Graph (SOPHIA VITUG)

# Create a title for the app
st.title("Screen Resolution Distribution in Laptops")
st.write("The findings indicate that Full HD 1920x1080 is the most prevalent screen resolution among laptops, accounting for 505 units and greatly exceeding other resolutions. In contrast bold text, and higher-end resolutions including IPS Panel Full HD 1920x1200 and IPS Panel Touchscreen 2400x1600 are less prevalent because they have 1 unit compared to Full HD 1920-1080. Overall, this bar chart highlights that Full HD screens are the most prevalent in modern laptops while higher resolutions are rare.")

# DATA
data = {
    'ScreenResolution': [
        'Full HD 1920x1080', '1366x786', 'IPS Panel Full HD 1920x1080',
        'IPS Panel Full HD / Touchscreen 1920x1080', 'Full HD / Touchscreen 1920x1080',
        '1600x900', 'Touchscreen 1366/768', 'Quad HD+ / Touchscreen 3200x1800',
        'IPS Panel 4k Ultra HD 3840x2160', 'IPS Panel 4k Ultra HD / Touchscreen 3840x2160',
        '4K Ultra HD / Touchscreen 3840x2160', '4K Ultra HD 3840X2160', 'Touchscreen 2560x1440',
        'IPS Panel 1366x768', 'IPS Panel Retina Display 2560x1660', 'IPS Panel Retina Display 2304x1440',
        'Touchscreen 2256x1504', 'IPS Panel Touchscreen 2560x1440', 'IPS Panel Quad HD+ / Touchscreen 3200x1800',
        'IPS Panel Touchscreen 1920x1200', '1440x900', 'IPS Panel Retina Display 2880x1800',
        'IPS Panel 2560x1440','2560x1440', 'Quad HD+ 3200X1800', '1920x1080','Touchscreen 2400x1600',
        'IPS Quad HD+ 2560x1440', 'IPS Panel Touchscreen 1366x768', 'IPS Panel Touchscreen / 4k Ultra HD 3840X2160',
        'IPS Panel Full HD 2160X1440', 'IPS Panel HD+ 3200x1800', 'IPS Panel Retina Display 2736x1824',
        'IPS Panel Full HD 1920x1200', 'IPS Panel Full HD 2560x1440', 'IPS Panel Full HD 1366x768',
        'Touchscreen / Full HD 1920X1080', 'Touchscreen / Quad HD+ 3200X1800', 'Touchscreen / 4K Ultra HD 3840x2160',
        'IPS Panel Touchscreen 2400x1600'
    ],
    'Count': [
        505, 263, 226, 51, 47, 23, 16, 15, 12, 11, 10, 7, 7, 7, 6, 6, 6, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort the dataframe
df = df.sort_values(by='Count', ascending=False)

# Create Altair chart
chart = alt.Chart(df).mark_bar().encode(
    x='Count',
    y=alt.Y('ScreenResolution', sort='-x')
)

# Display the chart
st.altair_chart(chart, use_container_width=True)





# CPU Frequency Bar Graph (JOHN LARENCE LUSAYA)
st.title('CPU Frequency Bar Graph')
st.write('The data indicates a strong preference for CPUs in the 2.00 GHz to 2.90 GHz range, highlighting consumer demand trends and market availability. CPUs with lower frequencies are less frequently found.')

# Data
data = {
    "CPU_Frequency (GHz)": [2.50, 2.80, 2.70, 1.60, 2.30, 2.00, 1.80, 2.60, 1.10, 2.40,
                            2.90, 3.00, 1.20, 1.44, 2.20, 1.50, 1.30, 3.60, 3.10, 2.10,
                            1.90, 0.90, 3.20, 1.00, 1.92],
    "count": [285, 165, 164, 124, 86, 86, 78, 74, 53, 50,
              19, 19, 15, 12, 11, 10, 6, 5, 3, 3,
              2, 2, 1, 1, 1]
}
df = pd.DataFrame(data)

# Extract values
cpu_frequency = df["CPU_Frequency (GHz)"].values
count = df["count"].values
x = np.arange(len(cpu_frequency))

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(cpu_frequency)))
ax.bar(x, count, color=colors)

# Labels and title
ax.set_xlabel('CPU Frequency (GHz)')
ax.set_ylabel('Count')
ax.set_title('CPU Frequency Preference')

# Customize x-axis labels
ax.set_xticks(x)
ax.set_xticklabels(cpu_frequency, rotation=40, ha='right', fontsize=10)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

# Display the plot in Streamlit
st.pyplot(fig)
