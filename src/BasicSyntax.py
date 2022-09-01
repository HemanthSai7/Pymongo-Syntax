from pathlib import Path
from src.DBConnection import Singleton
from src.datasets import Dataset

# mydb=client["LearnMongoDB"]
# mycol=mydb["collection1"]
class Configuration:
  DIR=Path(__file__).parent
  client=Singleton().get_client()
con=Configuration()

class Queries():
  def __init__(self,collection_name,database_name):

    self.collection_name=collection_name
    self.database_name=database_name

  def insert_dataset(self,dataset):
    """insert records"""
    mydb=con.client[self.database_name]
    mycol=mydb[self.collection_name]
    if type(dataset) is list:
      return mycol.insert_many(dataset)
    else:
      return mycol.insert_one(dataset)
  
  def count_documents(self,collection_name):
    """count dcouments in collection"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    return mycol.count_documents({})
  
  def find_documents(self,collection_name,query):
    """find documents in collection"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    for doc in mycol.find({}):
      print(doc)

  def and_keyword(self,collection_name):
    """$and"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    andlist=[]
    for doc in mycol.find({
      "$and":[{"capital":"Washington, D.C.",},
          {"name":"United States",}]
          }):
          andlist.append(doc)
    return andlist

  def or_keyword(self,collection_name):
    """$or"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    orlist=[]
    for doc in mycol.find({
      "$or":[
        {
          "capital":"Washington, D.C.",
        },
        {
          "capital":"Canberra",
        }
        ]
        }):
        orlist.append(doc)    
    return orlist     

  def in_keyword(self,collection_name):
    """$in"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    inlist=[]
    for doc in mycol.find({
      "$or":[
        {
          "capital":"Washington, D.C.",
        },
        {
          "population":{
            "$in":[125960000,210147125]
          }
        }
      ]}):
      inlist.append(doc)
    return inlist

  def lessthan_keyword(self,collection_name):
    """$lt"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    ltlist=[]
    for doc in mycol.find({
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
      ]}):
      ltlist.append(doc)
    return ltlist

  def greaterthan_keyword(self,collection_name):
    """$gt"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    gtlist=[]
    for doc in mycol.find({
      "$or":[
        {
          "population":{
            "$gt":328239523
          }
        },
        {
          "population":{
            "$in":[125960000,210147125]
        }
        }
      ]}):
      gtlist.append(doc)
    return gtlist

  def equal_keyword(self,collection_name):
    """$eq"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    eqlist=[]
    for doc in mycol.find({
      "$or":[
        {
          "name":{
            "$eq":"Australia"
          }
        },
        {
          "population":{
            "$in":[125960000,210147125]
        }
        }
      ]}):
      eqlist.append(doc)
    return eqlist

  def notequal_keyword(self,collection_name):
    """$ne"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    nelist=[]
    for doc in mycol.find({
      "$or":[
        {
          "name":{
            "$eq":"Australia"
          }
        },
        {
          "name":{
            "$ne":"United States"
        }
        }
      ]}):
      nelist.append(doc)
    return nelist

  def notin_keyword(self,collection_name):
    """$nin"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    ninlist=[]
    for doc in mycol.find({
      "$or":[
        {
          "capital":{
            "$eq":"Washington, D.C."
          }
        },
        {
          "population":{
            "$nin":[125960000,210147125]
        }
        }
      ]}):
      ninlist.append(doc)
    return ninlist    


  def greaterthanequal_keyword(self,collection_name):
    """$gte"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    gtelist=[]
    for doc in mycol.find({
      "population":{
        "$gte":125960000
        }
        }):
      gtelist.append(doc)
    return gtelist

  def lessthanequal_keyword(self,collection_name):
    """$lte"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    ltelist=[]
    for doc in mycol.find({
      "population":{
        "$lte":125960000
        }
        }):
        ltelist.append(doc)
    return ltelist  

  def nor_keyword(self,collection_name):
    """$nor"""
    mydb=con.client[self.database_name]
    mycol=mydb[collection_name]
    norlist=[]
    for doc in mycol.find({
      "$nor":[
        {
          "population":25681300
          
        },
        {
          "population":328239523
        }
      ]}):
      norlist.append(doc)
    return norlist  

# test=Queries("collection1","LearnMongoDB")
# test.insert_documents(Dataset.dataset1)
# print(test.lessthan_keyword("collection1"))