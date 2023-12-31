import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt, patches, ticker as ticker
from StarClusterPlot import ClusterVis, HRDiagram, Temp_to_RGB

st.sidebar.title("Options")
option = st.sidebar.radio("Select Page", ["Home", "Interactive Plots", "Package Tutorial", "Technical Documentation"])

if option == "Home":
    st.title("StarClusterPlot")
    st.write("[StarClusterPlot](https://pypi.org/project/StarClusterPlot/0.1.7/) is a Python package published and maintained by [Teerat Chanromyen](https://cosmicdusts.wordpress.com/about/) that helps visualize a star cluster's structure and its Hertzsprung-Russell Diagram with real, calculated color. It is specifically designed to work with data from the [Sloan Digital Sky Survey](https://www.sdss.org/) or any dataset that contains g, r, right ascension, and declination values. This site served as a documentation hub, featuring examples of interactive plots, a package tutorial, and technical documentation. To explore each part, select a topic from the left-hand sidebar.")
    st.write(" ")
    st.image('StarCluster_background.png')

if option == "Interactive Plots":
    st.title("Interactive Plot")

    st.sidebar.subheader("Star cluster's structure/HR-Diagram")
    Cluster = st.sidebar.selectbox('Select Data',('M2', 'M13', 'M15', 'NGC2420', 'NGC5053', 'NGC6791', 'Pal3', 'Pal5', 'Pal14'))
    feature = st.sidebar.multiselect('Select Plots/Data Sample', ["Data Sample", "Star Cluster Structure", "Hertzsprung–Russell Diagram"])

    file = str(Cluster) + '.csv'

    data = pd.read_csv(file)

    if "Data Sample" in feature:
        st.subheader("Data Sample")
        data_head = data.head()
        st.dataframe(data_head)
        st.divider()

    if "Star Cluster Structure" in feature:
        st.subheader("Star Cluster Structure")
        x_ratio_s = st.slider("X Axis ratio", min_value=1.0, max_value=10.0, value=6.75, key=3)
        y_ratio_s = st.slider("Y Axis ratio", min_value=4.0, max_value=20.0, value=12.0, key=4)
        temperature = st.slider('Select Minimum and Maximum Temperature', 1667, 26000, (1667, 26000))

        fig = ClusterVis(data, x_ratio_s, y_ratio_s, temperature[0], temperature[1])
        st.pyplot(fig)
        st.divider()

    if "Hertzsprung–Russell Diagram" in feature:
        st.subheader("Hertzsprung–Russell Diagram")

        left_right_bound = st.slider('Select Left and Right boundary (g-r)', -4.0, 4.0, (-3.0, 3.0))
        lower_upper_bound = st.slider('Select Lower and Upper boundary (r)', 10.0, 26.0, (12.0, 24.0))
        col1, col2 = st.columns(2)

        with col1:
            x_ratio_HR = st.slider("X Axis ratio", min_value=4.0, max_value=20.0, value=12.0, key=5)
            
        with col2:
            y_ratio_HR = st.slider("Y Axis ratio", min_value=5.0, max_value=15.0, value=10.0, key=6)

        fig = HRDiagram(data, left_right_bound[0], left_right_bound[1], lower_upper_bound[0], lower_upper_bound[1], x_ratio_HR, y_ratio_HR)
        st.pyplot(fig)
        st.divider()

    st.sidebar.subheader("Visualize a star's color from its temperature")
    temp_color_plot = st.sidebar.checkbox("Star's Temperature-Color plot", False)

    if temp_color_plot:
        temp = st.slider("Temperature", 1667, 25000, 4000, 1)
        color = Temp_to_RGB(temp)
        plt.rcParams["figure.figsize"] = [5, 5]
        plt.rcParams['axes.facecolor'] = '#353535'
        fig = plt.figure()
        ax = fig.add_subplot()
        circle1 = patches.Circle((0, 0), radius=0.5, color=color)
        ax.add_patch(circle1)
        ax.set(xlim=(-1, 1), ylim=(-1,1))
        ax.xaxis.set_major_locator(ticker.NullLocator())
        ax.yaxis.set_major_locator(ticker.NullLocator())
        st.pyplot(fig)

if option == "Package Tutorial":
    st.title("Package Tutorial")

    st.write("1.Install the Package")
    st.code('pip install StarClusterPlot==0.2.0', language='python')

    st.write("2.Import package and required libraries")
    code1 = """
    import pandas as pd
    from matplotlib import pyplot as plt
    from StarClusterPlot import ClusterVis, HRDiagram, Temp_to_RGB"""
    st.code(code1, language='python')

    st.write("3.Read data file")
    st.code("data = pd.read_csv('M13.csv')", language='python')

    st.write("- Plot Star Clusters structure; all parameters apart from the dataframe (data) are optional")
    st.code("ClusterVis(data, x_ratio, y_ratio, minimum_temperature, maximum_temperature)", language='python')

    st.write("- Plot Star Clusters HR-Diagram; all parameters apart from the dataframe (data) are optional")
    st.code("HRDiagram(data, left_boun, right_boun, lower_boun, upper_boun, x_ratio, y_ratio)", language='python')

    st.write("- Convert Temperature in Kelvin to RGB; 1667K < Temperature < 25000K")
    st.code("Temp_to_RGB(Temperature)", language='python')

    st.divider()
    st.write(" ")
    st.write("- If you wish to investigate other star clusters, data from the Sloan Digital Sky Survey can be found here. [link](https://classic.sdss.org/dr7/products/value_added/anjohnson08_clusterphotometry.php)")
    st.write("Use the code below to read the text file from the link.")
    st.code("data = pd.read_csv('file_name.txt', header=None, delimiter=r'\s+', names='Run Rerun CamCol DAOPHOTID ra dec x_u y_u u uErr chi_u sharp_u flag_u x_g y_g g gErr chi_g sharp_g flag_g x_r y_r r rErr chi_r sharp_r flag_r x_i y_i i iErr chi_i sharp_i flag_i x_z y_z z zErr chi_z sharp_z flag_z'.split(' '))", language='python')

    st.write(" ")
    st.write('- CSV file of Messier13, NGC2420, and NGC6791 can be found here: [link](https://github.com/Milne-Centre/ThaiPASS2019/tree/master/DATA_FOR_TASKS)')

    st.write(" ")
    st.write("- StarClusterPlot Package pypi.org: [link](https://pypi.org/project/StarClusterPlot/0.1.7/)")
    st.divider()

if option == "Technical Documentation":
    st.title("Technical Documentation")

    st.subheader("Convert g and r values to RGB color")

    st.divider()
    st.latex(r'''
    g,r \rightarrow B,V \rightarrow Temperature(Kelvin) \rightarrow Color(xyY) \rightarrow Color(XYZ) \rightarrow Color(RGB) \\
    ''')
    
    '''
    ##### 1. Convert g and r to B and V values.
    '''
    st.latex(r'''
        B = g + 0.3130(g-r) + 0.2271 \\
        V = g - 0.5784(g-r) - 0.0038
    ''')
    st.write("[Source](https://www.sdss3.org/dr8/algorithms/sdssUBVRITransform.php)")
    st.markdown("#")

    '''
    ##### 2. Convert B and V values to temperatures in Kelvin.
    '''
    st.latex(r'''
        Temperature = 4600(K)× (\frac{1}{0.92 (B-V) + 0.17} + \frac{1}{0.92 (B-V) + 0.62})
    ''')
    st.write("[Source](https://en.wikipedia.org/wiki/Color_index)")
    st.markdown("#")

    '''
    ##### 3. Convert temperatures in Kelvin to xyY color.
    '''
    st.latex(r'''
        x_c = \left\{
        \begin{array}{cl}
        -0.2661239\frac{10^9}{T^3} - 0.2343580\frac{10^6}{T^2} + 0.8776956\frac{10^3}{T} + 0.179910 & 1667K\le T \le 4000K \\
        -3.0258469\frac{10^9}{T^3} + 2.1070379\frac{10^6}{T^2} + 0.2226347\frac{10^3}{T} + 0.240390 & 4000K\le T \le 25000K
        \end{array}
        \right. \\
        \ \\
        y_c = \left\{
        \begin{array}{cl}
        -1.1063814x_c^3 - 1.34811020x_c^2 + 2.18555832x_c -0.20219683 & 1667K\le T \le 2222K\\
        -0.9549476x_c^3 - 1.37418593x_c^2 + 2.09137015x_c - 0.16748867 & 2222K\le T \le 4000K\\
        +3.0817580x_c^3 - 5.87338670x_c^2 + 3.75112997x_c - 0.37001483 & 4000K\le T \le 25000K\\
        \end{array}
        \right.
    ''')
    st.write("[Source](https://en.wikipedia.org/wiki/Planckian_locus#Approximation)")
    st.markdown("#")

    '''
    ##### 4. Convert xyY color to XYZ color.
    '''
    st.latex(r'''
        Y = 1 \\
        X = \frac{Y}{y}x \\
        Z = \frac{Y}{y}(1-x-y)
    ''')
    st.write("[Source](https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xy_chromaticity_diagram_and_the_CIE_xyY_color_space)")
    st.markdown("#")

    '''
    ##### 5. Convert XYZ color to RGB color.
    '''
    st.latex(r'''
        \begin{bmatrix}
        R \\
        G \\
        B
        \end{bmatrix}
        =
        \begin{bmatrix}
        3.240479 & -1.537150 & -0.498535 \\
        -0.969256 & 1.875992 & 0.041556 \\
        0.055648 & -0.204043 & 1.057311
        \end{bmatrix}
        .
        \begin{bmatrix}
        X \\
        Y \\
        Z
        \end{bmatrix}
    ''')
    st.write("[Source](https://www.cs.rit.edu/~ncs/color/t_convert.html#RGB%20to%20XYZ%20&%20XYZ%20to%20RGB)")

    st.divider()

    st.subheader("Create Scatter Plots")
    '''
    ##### Star Cluster Structure
    '''
    st.write("- X-Coordinate: Right ascension")
    st.write("- Y-Coordinate: Declination")

    '''
    ##### Hertzsprung-Russell Diagram
    '''
    st.write("- X-Coordinate: g-r")
    st.write("- Y-Coordinate: r")