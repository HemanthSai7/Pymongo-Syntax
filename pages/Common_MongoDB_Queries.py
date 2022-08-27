import streamlit as st
from src.datasets import Dataset
from src.BasicSyntax import Queries

st.set_page_config(page_title="Common MongoDB Queries")

st.sidebar.title("Common MongoDB Queries")
option = st.sidebar.selectbox("Select a query", ("Find Documents", "$and", "$or","$in","$lt"))

collection_name = st.sidebar.text_input("Enter collection name")
database_name = st.sidebar.text_input("Enter database name")
# if collection name is not entered, default is "collection1" and if database name is not entered, default is "LearnMongoDB"
if collection_name == "":
    collection_name = "collection1"
if database_name == "":
    database_name = "LearnMongoDB"

if option == "$and":

    st.markdown(f"> ### $and")
    code = """for doc in mycol.find({
      "$and":[{"capital":"Washington, D.C.",},
          {"name":"United States",}]
          })"""

    st.markdown("### Result")
    st.write(Queries(collection_name, database_name).and_keyword(collection_name))

    st.markdown("### Code snippet")
    st.code(code, language="python")

if option=="$or":
  st.markdown(f"> ### $or")
  code = """for doc in mycol.find({
    "$or":[{"capital":"Washington, D.C.",},
           {"capital":"Canberra",}
          ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).or_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")

if option=="$in":
  st.markdown(f"> ### $or")
  code="""for doc in mycol.find({
      "$or":[
        {
          "capital":"Washington, D.C.",
        },
        {
          "population":{
            "$in":[125960000,210147125]
          }
        }
      ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).in_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")    
    
if option=="$lt":
  st.markdown(f"> ### $in")
  code="""for doc in mycol.find({
      "$or":[
        {
          "population":{
            "$lt":328239523
          }
        },
        {
          "population":{
            "$in":[125960000,210147125]
        }
        }
      ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).lessthan_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")