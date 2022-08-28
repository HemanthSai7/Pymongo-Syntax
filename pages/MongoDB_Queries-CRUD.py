import streamlit as st
from src.datasets import Dataset
from src.BasicSyntax import Queries

st.set_page_config(page_title="Common MongoDB Queries")

st.sidebar.title("Common MongoDB Queries")
option = st.sidebar.selectbox("Select a query", (None,"$and", "$or","$in","$lt","$lte","$gt","$eq","$ne","$nin","$gte","$lte","$nor"))

# collection_name = st.sidebar.text_input("Enter collection name")
# database_name = st.sidebar.text_input("Enter database name")
# if collection name is not entered, default is "collection1" and if database name is not entered, default is "LearnMongoDB"
collection_name = "collection1"
database_name = "LearnMongoDB"

if option==None:
    st.sidebar.write("Please select a query")

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

if option=="$gt":
  st.markdown(f"> ### $gt")
  code="""for doc in mycol.find({
    "$or":[
      {
        population:{
          "gt":328239523
        }
      },
      population:{
        "$in":[125960000,210147125]
      }
    ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).greaterthan_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")

if option=="$eq":
  st.markdown(f"> ### $eq")
  code="""for doc in mycol.find({
    "$or":[
      {
        name:{
          "eq":"Australia"
        }
      },
      population:{
        "$in":[125960000,210147125]
      }
    ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).equal_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")  

if option=="$ne":
  st.markdown(f"> ### $ne")
  code="""for doc in mycol.find({
    "$or":[
      {
        name:{
          "$eq":"Australia"
        }
      },
      name:{
        "$ne":"United States"
      }
    ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).notequal_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")

if option=="$nin":
  st.markdown(f"> ### $nin")
  code="""for doc in mycol.find({
    "$or":[
      {
        name:{
          "$eq":"Australia"
        }
      },
      name:{
        "$nin":[125960000,210147125]
      }
    ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).notin_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")

if option=="$gte":
  st.markdown(f"> ### $gte")
  code="""for doc in mycol.find({
    population:{
      "$gte":125960000
    }
    })"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).greaterthanequal_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")  

if option=="$lte":
  st.markdown(f"> ### $lte")
  code="""for doc in mycol.find({
    population:{
      "$lte":125960000
    }
    })"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).lessthanequal_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")

if option=="$nor":
  st.markdown(f"> ### $nor")
  code="""for doc in mycol.find({
    "$nor":[
        {
          "population":25681300
          
        },
        {
          "population":328239523
        }
    ]})"""
  st.markdown("### Result")
  st.write(Queries(collection_name, database_name).nor_keyword(collection_name))
  st.markdown("### Code snippet")
  st.code(code, language="python")  
