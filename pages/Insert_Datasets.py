import streamlit as st
from src.datasets import Dataset
from src.BasicSyntax import Queries

st.set_page_config(page_title="Insert Dataset")

st.markdown("# Insert Dataset")
st.sidebar.title("Datasets")
option=st.selectbox("Select a dataset",["dataset1","dataset2","dataset3","dataset4","dataset5","dataset6","dataset7","dataset8","dataset9","dataset10","dataset11","dataset12","dataset13"])

collection_name=st.sidebar.text_input("Enter collection name")
database_name=st.sidebar.text_input("Enter database name")
#check for the collection name. New data cannot be inserted into an existing collection
if collection_name=="":
  collection_name="collection1"
if database_name=="":
    database_name="LearnMongoDB"
    

#insert dataset
if option=="dataset1":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset1))
  st.write("Dataset inserted")
elif option=="dataset2":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset2))  
  st.write("Dataset inserted")
elif option=="dataset3":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset3))
  st.write("Dataset inserted")
elif option=="dataset4":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset4))
  st.write("Dataset inserted")
elif option=="dataset5":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset5))  
  st.write("Dataset inserted")
elif option=="dataset6":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset6))
  st.write("Dataset inserted")
elif option=="dataset7":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset7))
elif option=="dataset8":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset8))
elif option=="dataset9":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset9))
elif option=="dataset10":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset10))
elif option=="dataset11":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset11))
elif option=="dataset12":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset12))
elif option=="dataset13":
  st.write(Queries(collection_name,database_name).insert_dataset(Dataset.dataset13))    
else:
    st.write("No dataset selected")