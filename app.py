import streamlit as st

# Define a function for each page
def home():
    st.title('Home Page')
    st.write('Welcome to the Home Page!')
    st.image('assets/bobtail.jpg', caption='a bobtail squid')

def about():
    st.title('About Page')
    st.write('This is the About Page.')

def contact():
    st.title('Contact Page')
    st.write('This is the Contact Page.')

# Sidebar for navigation
page = st.sidebar.selectbox('Select a page:', ['Home', 'About', 'Contact'])

# Display the selected page
if page == 'Home':
    home()
elif page == 'About':
    about()
elif page == 'Contact':
    contact()

