import streamlit as st
from src.BasicSyntax import Queries
import time

st.set_page_config(page_title="Home")  # multipage app

# title of the page
title = "MongoDB Queries"
st.title(f"{title}")

st.sidebar.info("Navigation and Information",icon="📑")

#Information
st.sidebar.markdown("This is a simple app to demonstrate the basic syntax of MongoDB queries. The app is built using Streamlit and Python.")

#Instructions to use the app
st.markdown("> ### App Overview")
st.markdown("#### Home🏠")
st.markdown("Home is the landing page of the app. It contains the information about the app and the navigation bar on the left side of the screen. The navigation bar contains the links to the different pages of the app. The pages are as follows:")

st.markdown("#### Basic Syntax 📝")
st.markdown("Basic Syntax page contains the basic syntax of MongoDB queries. The queries are divided into 3 categories:")
st.markdown("1. **CRUD**")
st.markdown("2. **Aggregation**")
st.markdown("3. **Array Indexing**")

st.markdown("#### Insert Data 📥")
st.markdown("Insert Data page contains the code to insert data into the MongoDB database. The data is inserted into the database using the `insert_one()` and `insert_many()` methods.")
st.info("Please Note 🖊: Dataset1 named **LearnMongoDB** and a collection named **collection1** is already inserted into the database. Trying to add the same dataset again will result in an error. The check for the same is **currently** not implemented in the app. You can easily change the name of the collection and insert the data into the database to avoid the error. Also the data will be inserted in my Azure Cosmos DB account. I'll the leave the instructions to set your own account soon")

st.markdown("#### View Dataset 📂")
st.markdown("View the datasets which can be inserted into the app. All the queries which would be implemented will be based on the 13 datasets available")
