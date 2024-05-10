import streamlit as st

# Define a function for each page
def home():
    st.title('Home Page')
    st.write('Welcome to the Home Page!')

def browse_examples():
    st.title('Browse Examples')
    st.write('This is the Browse Examples Page.')

def ov_and_qk_circuits():
    st.title('OV and QK Circuits')
    st.write('This is the OV and QK Circuits Page.')

def copy_suppression_preserving_ablation():
    st.title('Copy Suppression-Preserving Ablation')
    st.write('This is the Copy Suppression-Preserving Ablation Page.')

def anti_induction_vs_copy_suppression():
    st.title('Anti Induction vs Copy Suppression')
    st.write('This is the Anti Induction vs Copy Suppression Page.')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Tutorial Sections:', ['Home', 'Browse Examples', 'OV and QK circuits', 'Copy Suppression-Preserving Ablation', 'Anti Induction vs Copy Suppression'])

# Display the selected page
if page == 'Home':
    home()
elif page == 'Browse Examples':
    browse_examples()
elif page == 'OV and QK circuits':
    ov_and_qk_circuits()
elif page == 'Copy Suppression-Preserving Ablation':
    copy_suppression_preserving_ablation()
elif page == 'Anti Induction vs Copy Suppression':
    anti_induction_vs_copy_suppression()
