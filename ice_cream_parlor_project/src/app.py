import streamlit as st
from database_setup import setup_database
from crud_operations import *

# Initialize the database
setup_database()

# Title and description
st.title('Ice Cream Parlor Management System')
st.write('Welcome to the Ice Cream Parlor Management System!')

# Add flavor form
st.subheader('Add New Flavor')
name = st.text_input('Flavor Name')
is_seasonal = st.checkbox('Is Seasonal')
if st.button('Add Flavor'):
    add_flavor(name, is_seasonal)
    st.success('Flavor added successfully!')

# List flavors
st.subheader('Flavors')
flavors = get_flavors()
for flavor in flavors:
    st.write(flavor)



