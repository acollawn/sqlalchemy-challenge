# sqlalchemy-challenge

# class notes

1. import engine and database
   
   * from pathlib import Path
   * from sqlalchemy import create_engine, text
   
   -- create reference to the file
    * database_path = Path("../Resources/Census_Data.sqlite")
   
   -- create an enginr that can talk to the database
     * engine = create_engine(f"sqlite:///{database_path")
   
   -- query all records from database
     * query = text("SELECT * FROM Census_Data")
     * data = engine.execute(query)
       * for records in data:
         * print(record)
2. query using Pandas

   -- Import Dependencies
   * from pathlib import Path
   * from sqlalchemy import create_engine, text
   * import pandas as pd
   
   -- create reference file
    * database_path = Path("../Resources/Census_Data.sqlite")

  -- create engine
     * engine = create_engine(f"sqlite:///{database_path")
     * conn = engine_connect()
     
  -- query records in the db
     * data = pd.read_sql("SELECT * FROM Census_Data", conn)

  -- preview data
  * data.head()
    
3. Classes
* #Define the Surfer Class
   class Surfer():

 * #Initialize the Surfer constructor 
     def __init__(self, name, hometown, rank):
         self.name = f"{name} Dude"
         self.hometown = f"{hometown} Waves"
         self.rank = rank
