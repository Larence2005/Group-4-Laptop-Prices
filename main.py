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

st.markdown("<h3>GROUP 4 - BM3</h3>", unsafe_allow_html=True)

st.write("The purpose of this website is to convert our previous Data Visualization activity in Google Colab Notebook into a Streamlit Web Application")
st.markdown("- Check the GitHub Repository at the bottom for the source code.")
st.write('')
st.markdown('<hr style="border:1px solid gray">', unsafe_allow_html=True)
st.write('')
st.write('')
"# Describing the Dataset"

df = pd.read_csv("laptop_price - dataset.csv")
df

df.info()
st.write('')

st.write("The sum of each categorical column can be seen below")

sum = df.isna().sum()
sum

desc = df.describe()
desc


#daniel santillan
st.title("Distribution of Laptop Companies")
st.write("It can be seen that Asus and Dell takes on the lead followed up by HP.")

company_data = {
    "Company": [
        "Dell", "Lenovo", "HP", "Asus", "Acer", "MSI", "Toshiba",
        "Apple", "Samsung", "Razer", "Mediacom", "Microsoft", 
        "Xiaomi", "Vero", "Chuwi", "Google", "Fujitsu", "LG", "Huawei"
    ],
    "Count": [
        291, 289, 268, 152, 101, 54, 48, 21, 9, 
        7, 7, 6, 4, 4, 3, 3, 3, 3, 2
    ]
}

# Set up the matplotlib figure
plt.figure(figsize=(8, 6))
sns.barplot(x=company_data["Company"], y=company_data["Count"], color='blue')  # Use barplot for categorical data
plt.title('Distribution of Laptop Companies')
plt.xlabel('Company')
plt.ylabel('Count')
plt.xticks(rotation=30)

# Show the plot in Streamlit
st.pyplot(plt)
st.write('')
st.write('')


#Screen Resolution Bar Graph (SOPHIA VITUG)

# Create a title for the app
st.title("Screen Resolution Distribution in Laptops Bar Graph")
st.write("The findings indicate that Full HD 1920x1080 is the most prevalent screen resolution among laptops, accounting for 505 units and greatly exceeding other resolutions. In contrast bold text, and higher-end resolutions including IPS Panel Full HD 1920x1200 and IPS Panel Touchscreen 2400x1600 are less prevalent because they have 1 unit compared to Full HD 1920-1080. Overall, this bar chart highlights that Full HD screens are the most prevalent in modern laptops while higher resolutions are rare.")
st.write('')
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
st.write('')
st.write('')


#CPU_Company Pie Graph (SOPHIA VITUG)
# Create a title for the app
st.title("CPU Company Distribution Pie Graph")
st.write("This pie graph illustrates that Intel dominates with a significant market share, accounting for 95.5% of CPUs (1,214 units). AMD follows with 4.7% (60 units), while Samsung represents a negligible portion with only 1 unit, making up less than 0.1%. Upon observing this pie graph, it suggests that Intel is the dominant brand for CPU in laptops, with AMD having a minor but noticeable presence, and Samsung being almost nonexistent.")
st.write('')
# DATA
data = {'CPU_Company' : ['Intel'] * 1214 + ['AMD'] * 60 + ['Samsung'] * 1}
df = pd.DataFrame(data)

# Calculate CPU company counts
cpu_counts = df['CPU_Company'].value_counts()

# Function to create the pie chart
def create_pie_chart(labels, sizes, label_type):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    if label_type == "percentage":
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    else:
        ax.pie(sizes, labels=[f"{label}: {size}" for label, size in zip(labels, sizes)])
    
    ax.set_title('CPU Company Distribution')
    return fig

# Get labels and sizes
labels = cpu_counts.index.tolist()
sizes = cpu_counts.values.tolist()

# User input for label type
label_type = st.selectbox("Choose label type:", ["Percentage", "Count"])

# Create and display the pie chart
fig = create_pie_chart(labels, sizes, label_type.lower())
st.pyplot(fig)
st.write('')
st.write('')


# Create a title for the app
st.title("CPU Type Bar Graph")
st.write("This bar graph indicates the most popular CPU type, with 193 occurrences, followed by the Core i7 7700HQ and Core i7 7500U, which have 147 and 133 counts, respectively. After the top three, the frequency drops significantly, with the Core i3 6066U and Core i7 8550U being fairly common but in smaller quantities. Furthermore, rare CPU types appear only once, such as M3-6Y30, A6-Series 7310, and others, which indicates that these types are less frequently used in laptops.")
st.write('')
# Prepare the data
cpu_types = ['Core i5 7200U', 'Core i7 7700HQ', 'Core i7 7500u', 'Core i3 6006U','Core i7 8550U',
             'Core M m3', 'E-Series E2-9000', 'Core M M3-6Y30', 'A6-Series 7310', 'A9-Series 9410']
counts = [193, 147, 133, 81, 73, 1, 1, 1, 1, 1]

df = pd.DataFrame({'CPU Type': cpu_types, 'Count': counts})

# Sort the dataframe by count in descending order
df = df.sort_values('Count', ascending=False)

# Create Altair chart
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Count', axis=alt.Axis(title='Count')),
    y=alt.Y('CPU Type', sort='-x', axis=alt.Axis(title='CPU Type'))
)

# Customize chart appearance
chart = chart.properties(
    title='CPU Types and Their Counts',
    width=800,
    height=600
)

st.altair_chart(chart)
st.write('')
st.write('')


# CPU Frequency Bar Graph (JOHN LARENCE LUSAYA)
st.title('CPU Frequency Bar Graph')
st.write('The data indicates a strong preference for CPUs in the 2.00 GHz to 2.90 GHz range, highlighting consumer demand trends and market availability. CPUs with lower frequencies are less frequently found.')
st.write('')
data = {
    "CPU_Frequency (GHz)": [2.50, 2.80, 2.70, 1.60, 2.30, 2.00, 1.80, 2.60, 1.10, 2.40,
                            2.90, 3.00, 1.20, 1.44, 2.20, 1.50, 1.30, 3.60, 3.10, 2.10,
                            1.90, 0.90, 3.20, 1.00, 1.92],
    "count": [285, 165, 164, 124, 86, 86, 78, 74, 53, 50,
              19, 19, 15, 12, 11, 10, 6, 5, 3, 3,
              2, 2, 1, 1, 1]
}
df = pd.DataFrame(data)

cpu_frequency = df["CPU_Frequency (GHz)"].values
count = df["count"].values
x = np.arange(len(cpu_frequency))

fig, ax = plt.subplots(figsize=(12, 6))
colors = plt.cm.viridis(np.linspace(0, 1, len(cpu_frequency)))
ax.bar(x, count, color=colors)

ax.set_xlabel('CPU Frequency (GHz)')
ax.set_ylabel('Count')
ax.set_title('CPU Frequency Preference')

ax.set_xticks(x)
ax.set_xticklabels(cpu_frequency, rotation=40, ha='right', fontsize=10)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

st.pyplot(fig)
st.write('')
st.write('')


#GPU Company Pie Graph (JOHN LARENCE LUSAYA)
gpu_companies = ['Intel', 'Nvidia', 'AMD', 'ARM']
counts = [704, 396, 174, 1]

st.title("GPU Company Distribution")
st. write("The pie chart illustrates the distribution of GPU companies, with Intel leading significantly at 704 units, followed by Nvidia with 396 units and AMD with 174 units. ARM has a minimal presence, with only 1 unit.")
st.write('')
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(counts, labels=gpu_companies, autopct='%1.1f%%', startangle=140)
ax.set_title('GPU Company Distribution')
ax.axis('equal')

st.pyplot(fig)
st.write('')
st.write('')

#GPU Type Bar Graph (JOHN LARENCE LUSAYA)
gpus = [
    'HD Graphics 620', 'HD Graphics 520', 'UHD Graphics 620', 'GeForce GTX 1050',
    'GeForce GTX 1060', 'Graphics 620', 'Radeon R5 520', 'Radeon R7',
    'HD Graphics 540', 'Mali T860 MP4'
]
counts = [280, 181, 68, 66, 48, 1, 1, 1, 1, 1]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
          '#FFC300', '#DAF7A6', '#FFC300', '#581845', '#900C3F']

st.title("GPU Type Bar Graph")
st.write('The number of varieties of GPU is indicated in the bar graph with a total of 280 units, HD Graphics 620 is the most frequently used type. Following it is HD Graphics 520 with 181 units. Others include UHD Graphics 620, GeForce GTX 1050, and others stand at 68 and 66 units respectively. Most other types of GPU had few units, with several having only 1 unit. This shows that integrated graphics, particularly from Intel, are preferred than the discrete GPUs.')
st.write('')

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(gpus, counts, color=colors)
ax.set_title('GPU Type')
ax.set_xlabel('GPU Type')
ax.set_ylabel('Count')
ax.set_xticklabels(gpus, rotation=45, ha='right')

for i, v in enumerate(counts):
    ax.text(i, v, str(v), ha='center', va='bottom')

plt.tight_layout()

st.pyplot(fig)
st.write('')
st.write('')

#RAM GB - EDELLE LUMABI
# Data
RAM = [8, 4, 16, 6, 12, 32, 2, 24, 64]
count = [613, 367, 198, 35, 25, 17, 16, 3, 1]

# Create a DataFrame
data = {'RAM (GB)': RAM, 'Count': count}
df = pd.DataFrame(data)

# Streamlit Title
st.title('RAM (GB) Distribution')

# Description
st.write("The histogram above indicates that most laptops only have *8GB of RAM*. The graph is skewed to the right which means there are fewer laptops with larger sizes of RAM. It can also be observed that most laptops only have RAM sizes that range from *0 - 16 GB.*")
st.write('')

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))
sns.barplot(x='RAM (GB)', y='Count', data=df, color='green', ax=ax)
ax.set_title('RAM (GB) Distribution')
ax.set_xlabel('RAM (GB)')
ax.set_ylabel('Frequency')

# Display the plot
st.pyplot(fig)
st.write('')
st.write('')



#MEMORY - EDELLE LUMABI
# Create and display the bar chart
st.title("Memory Distribution")
st.write("Based from the graph, most laptops have a 256GB SSD memory followed by a 1TB HDD memory.")
st.title("Memory Count Distribution")
st.write("This chart displays the count of different memory configurations.")

# Data preparation (using existing data array)
memory_data = {
    "Memory": [
        "256GB SSD", "1TB HDD", "500GB HDD", "512GB SSD", "128GB SSD + 1TB HDD",
        "128GB SSD", "256GB SSD + 1TB HDD", "32GB Flash Storage", "2TB HDD",
        "512GB SSD + 1TB HDD", "1TB SSD", "64GB Flash Storage", "256GB SSD + 2TB HDD",
        "256GB Flash Storage", "16GB Flash Storage", "1.0TB Hybrid", "32GB SSD",
        "180GB SSD", "128GB Flash Storage", "512GB SSD + 2TB HDD", "16GB SSD",
        "512GB Flash Storage", "1TB SSD + 1TB HDD", "256GB SSD + 500GB HDD",
        "128GB SSD + 2TB HDD", "256GB SSD + 256GB SSD", "512GB SSD + 256GB SSD",
        "512GB SSD + 512GB SSD", "64GB Flash Storage + 1TB HDD", "1TB HDD + 1TB HDD",
        "32GB HDD", "64GB SSD", "128GB HDD", "240GB SSD", "8GB SSD", "508GB Hybrid",
        "1.0TB HDD", "512GB SSD + 1.0TB Hybrid", "256GB SSD + 1.0TB Hybrid"
    ],
    "Count": [
        412, 215, 124, 114, 94,
        74, 73, 36, 16,
        14, 14, 13, 10, 8,
        7, 7, 6, 5,
        4, 3, 3, 2,
        2, 2, 2, 2,
        1, 1, 1, 1,
        1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
}

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))
sns.barplot(x=memory_data["Memory"], y=memory_data["Count"], color='blue')  # Use barplot for categorical data
plt.title('Memory Distribution')
plt.xlabel('Memory (GB)')
plt.ylabel('Number of Laptops')
plt.xticks(rotation=90)
st.pyplot(plt)
st.write('')
st.write('')





#OPSYS - EDELLE
os = [
    'Windows 10', 'No OS', 'Linux', 'Windows 7',
    'Chrome OS', 'macOS', 'Mac OS X', 'Windows 10 S',
    'Android'
]
counts = [1048, 66, 58, 45, 27, 13, 8, 8, 2]

# Create a DataFrame
df = pd.DataFrame({'Operating System': os, 'Count': counts})

# Streamlit Title
st.title('Operating System Distribution')

# Description
st.write('Based from the graph below, the operating system or OS used by most laptops is **Windows 10** and some laptops have no OS at all. There are only a few who use MacOS and Android OS.')

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(df['Operating System'], df['Count'], color='purple')
ax.set_title('Operating Systems')
ax.set_xlabel('Operating System')
ax.set_ylabel('Count')
ax.set_xticklabels(df['Operating System'], rotation=40)

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

# Optional blank space
st.write('')
st.write('')


#CPU FREQ VS PRICE - NICK

data = {'CPU_Frequency (GHz)': [2.4, 3.1, 2.8, 3.6, 4.0],
        'Price (Euro)': [200, 350, 300, 450, 500]}
df = pd.DataFrame(data)

def cpu_freq_vs_price_bar_chart(df):
    plt.figure(figsize=(10,6))
    sns.barplot(x=df['CPU_Frequency (GHz)'], y=df['Price (Euro)'], color='magenta')
    plt.xticks(rotation=80)
    plt.title('CPU Frequency (GHz) vs. Price (Euro)')
    st.pyplot(plt)

st.title("CPU Frequency vs Price Bar Chart")
cpu_freq_vs_price_bar_chart(df)
st.write('')
st.write('')




#=====================================THIS IS A FOOTER=====================================
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

st.markdown('<hr style="border:1px solid gray">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Contributors")
    st.markdown(
        """
        - <a href="https://github.com/edelle-del" style="text-decoration:none;">Edelle Lumabi</a>
        - <a href="https://github.com/Larence2005" style="text-decoration:none;">John Larence Lusaya</a> 
        - <a href="https://github.com/edelle-del" style="text-decoration:none;">Nicholas Rian Pastiu</a>
        - <a href="https://github.com/edelle-del" style="text-decoration:none;">Daniel Santillan</a>
        - <a href="https://github.com/sophiavitug10" style="text-decoration:none;">Sophia Vitug</a>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown("### Main Repository")
    st.markdown(
        """
        - <a href="https://github.com/Larence2005/Group-4-Laptop-Prices" style="text-decoration:none;">View on GitHub</a>
        """, 
        unsafe_allow_html=True
    )
    st.write('')
    st.markdown("### Google Colab")
    st.markdown(
        """
        - <a href="https://colab.research.google.com/drive/11aJWw77VGMlYehHPJNIqTT0UDC-sdsTT?usp=sharing&fbclid=IwY2xjawFiUxNleHRuA2FlbQIxMAABHX9PyWKgfDOWhwvIL-jNZ3LzqTKxenn_0kcFhe7zqT3DGo9iiTg8tQFGDQ_aem_zv9k5pN3oqaiXDyEMqPy9Q#scrollTo=8RL5-7v5MXwW" style="text-decoration:none;">Open the Notebook</a>
        """, 
        unsafe_allow_html=True
    )

with col3:
    st.markdown("### Details")
    st.markdown(
        """
        <p>© GROUP 4 - BM3</p>
        <p>2024. All Rights Reserved.</p>
        <p>Mapua University - Makati</p>
        """, 
        unsafe_allow_html=True
    )
