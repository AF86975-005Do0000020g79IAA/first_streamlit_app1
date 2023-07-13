import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣,Omeza3 & oat meal')
streamlit.text('🥗,kult & spinach ,rocket smoothly')
streamlit.text('🐔,Hard-boiled ,free-range egg')
streamlit.text('🥑🍞,Avcado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocada','strawberries']
fruits_to_show =  my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
