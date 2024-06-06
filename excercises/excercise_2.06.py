from sqlalchemy import create_engine
engine = create_engine('sqlite:///sampledb.sqlite')
connection = engine.connect()

# Note the code will return "no such table: Table1" bacause the db is either empty or does not excist
# Proof: https://docs.sqlalchemy.org/en/20/core/connections.html#sqlalchemy.engine.Connection.execute 
# Assertion: https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91 
result = connection.execute("SELECT * FROM Table1")
