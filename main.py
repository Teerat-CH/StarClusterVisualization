import pandas as pd
import streamlit as st
from StarClusterPlot import ClusterVis, HRDiagram

st.write("""
# Star Cluster Interactive Plot
""")

Cluster = st.selectbox('##### Select Star Cluster',('M13', 'NGC2420', 'NGC6791'))

file = str(Cluster) + '.csv'

data = pd.read_csv(file)
data_head = data.head()
st.write("""
##### Data Sample
""")
st.write(data_head)

st.write("""
##### Plots
""")

structure = st.checkbox('Star Cluster Structure', key=1)

if structure:
    x_scale_s = st.slider("X Axis Scale", min_value=1.0, max_value=10.0, value=6.75, key=3)
    y_scale_s = st.slider("Y Axis Scale", min_value=4.0, max_value=20.0, value=12.0, key=4)

    fig = ClusterVis(data, x_scale_s, y_scale_s)
    st.pyplot(fig)

HR = st.checkbox('Hertzsprung–Russell Diagram', key=2)

if HR:
    col1, col2 = st.columns(2)

    with col1:
        left_boun= st.slider("Left Boundary", min_value=-6.0, max_value=0.0, value=-3.0)
        lower_boun= st.slider("Lower Boundary", min_value=6, max_value=18, value=12)
        x_scale_HR = st.slider("X Axis Scale", min_value=4, max_value=20, value=12, key=5)
        
    with col2:
        right_boun= st.slider("Right Boundary", min_value=0, max_value=6, value=3)
        upper_boun= st.slider("Upper Boundary", min_value=18, max_value=30, value=24)
        y_scale_HR = st.slider("Y Axis Scale", min_value=1.0, max_value=10.0, value=6.75, key=6)

    fig = HRDiagram(data, left_boun, right_boun, lower_boun, upper_boun, x_scale_HR, y_scale_HR)
    st.pyplot(fig)

st.write('-------------------------------------------------------------------------------')

st.write("""
## Tutorial
""")

st.write("1.Install the Package")
st.code('!pip install StarClusterPlot==0.1.7', language='python')

st.write("2.Import package and required libraries")
code1 = """import pandas as pd
from matplotlib import pyplot as plt
from StarClusterPlot import ClusterVis, HRDiagram"""
st.code(code1, language='python')

st.write("3.Read data file")
st.code("data = pd.read_csv('M13.csv')", language='python')

st.write("4.Plot Star Clusters structure; all parameters apart from the dataframe (data) are optional")
st.code("ClusterVis(data, x_scale, y_scale)", language='python')

st.write("5.Plot Star Clusters HR-Diagram; all parameters apart from the dataframe (data) are optional")
st.code("HRDiagram(data, left_boun, right_boun, lower_boun, upper_boun, x_scale, y_scale)", language='python')

st.write('-------------------------------------------------------------------------------')
st.write(" ")
st.write("- If you wish to investigate other star clusters, check out this Sloan Digital Sky Survey tutorial. [link](https://skyserver.sdss.org/dr12/en/proj/advanced/hr/mast.aspx)")
st.write('After importing the data as a CSV file, simply delete the first row, and you should be good to go!')

st.write(" ")
st.write('- CSV file of Messier13, NGC2420, and NGC6791 can be found here: [link](https://drive.google.com/drive/folders/1-Xi4bIYWrpwXzEk2fneYXKSjzAAkP7sw?usp=sharing)')

st.write(" ")
st.write("- StarClusterPlot Package pypi.org: [link](https://pypi.org/project/StarClusterPlot/0.1.7/)")
st.write('-------------------------------------------------------------------------------')