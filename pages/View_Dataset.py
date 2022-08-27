from src.datasets import Dataset
import streamlit as st

st.set_page_config(page_title="View Dataset")

st.markdown("# View Dataset")
st.sidebar.title("Datasets")

#view dataset
dataset=st.selectbox("Select a dataset",("dataset1","dataset2","dataset3","dataset4","dataset5","dataset6","dataset7","dataset8","dataset9","dataset10","dataset11","dataset12","dataset13"))
if dataset=="dataset1":
  st.write(Dataset.dataset1)
elif dataset=="dataset2":
  st.write(Dataset.dataset2)
elif dataset=="dataset3":
  st.write(Dataset.dataset3)
elif dataset=="dataset4":
  st.write(Dataset.dataset4)
elif dataset=="dataset5":
  st.write(Dataset.dataset5)
elif dataset=="dataset6":
  st.write(Dataset.dataset6)
elif dataset=="dataset7":
  st.write(Dataset.dataset7)
elif dataset=="dataset8":
  st.write(Dataset.dataset8)
elif dataset=="dataset9":
  st.write(Dataset.dataset9) 
elif dataset=="dataset10":
  st.write(Dataset.dataset10) 
elif dataset=="dataset11":
  st.write(Dataset.datase11) 
elif dataset=="dataset12":
  st.write(Dataset.dataset12) 
elif dataset=="dataset13":
  st.write(Dataset.dataset13)                         
else:
  st.write("No dataset selected")

 
  
  