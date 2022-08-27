import streamlit as st
from src.BasicSyntax import Queries
import time
import numpy as np


st.set_page_config(
    page_title="Home",

)
st.title("MongoDB Queries")
st.sidebar.title("Common MongoDB Queries")
option=st.sidebar.selectbox("Select a query",("Insert Documents","Find Documents","$and","$or"))

collection_name=st.sidebar.text_input("Enter collection name")
database_name=st.sidebar.text_input("Enter database name")
#if collection name is not entered, default is "collection1" and if database name is not entered, default is "LearnMongoDB"
if collection_name=="":
  collection_name="collection1"
if database_name=="":
  database_name="LearnMongoDB"
  

if option=="$and":
  code="""mycol.find({
      "$and":[{"capital":"Washington, D.C.",},
          {"name":"United States",}]
          })"""
  st.write(Queries(collection_name,database_name).and_keyword(collection_name))
  st.code(code,language="python")

