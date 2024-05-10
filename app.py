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
st.sidebar.title('Navigation')
if st.sidebar.button('Home'):
    page = 'Home'
elif st.sidebar.button('About'):
    page = 'About'
elif st.sidebar.button('Contact'):
    page = 'Contact'
else:
    page = 'Home'

# Display the selected page
if page == 'Home':
    home()
elif page == 'About':
    about()
elif page == 'Contact':
    contact()

