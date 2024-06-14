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
flavor_name = st.text_input('Flavor Name')
is_seasonal = st.checkbox('Is Seasonal')
if st.button('Add Flavor'):
    add_flavor(flavor_name, is_seasonal)
    st.success('Flavor added successfully!')

# Add ingredient form
st.subheader('Add New Ingredient')
ingredient_name = st.text_input('Ingredient Name')
quantity = st.number_input('Quantity', min_value=0)
if st.button('Add Ingredient'):
    add_ingredient(ingredient_name, quantity)
    st.success('Ingredient added successfully!')

# Add allergen form
st.subheader('Add New Allergen')
allergen_name = st.text_input('Allergen Name')
if st.button('Add Allergen'):
    add_allergen(allergen_name)
    st.success('Allergen added successfully!')

# Add customer suggestion form
st.subheader('Add Customer Suggestion')
suggestion_flavor_name = st.text_input('Suggested Flavor Name')
customer_name = st.text_input('Customer Name')
allergy_concerns = st.text_area('Allergy Concerns')
if st.button('Add Customer Suggestion'):
    add_customer_suggestion(suggestion_flavor_name, customer_name, allergy_concerns)
    st.success('Customer suggestion added successfully!')

# Add to cart form
st.subheader('Add to Cart')
flavor_id = st.number_input('Flavor ID', min_value=1)
if st.button('Add to Cart'):
    add_to_cart(flavor_id)
    st.success('Flavor added to cart successfully!')

# Search flavors form
st.subheader('Search Flavors')
search_keyword = st.text_input('Search Keyword')
if st.button('Search'):
    search_results = search_flavors(search_keyword)
    if search_results:
        for flavor in search_results:
            st.write(flavor)
    else:
        st.write('No flavors found.')

# List flavors
st.subheader('Flavors')
flavors = get_flavors()
for flavor in flavors:
    st.write(flavor)
