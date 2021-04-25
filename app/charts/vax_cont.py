import pymysql
from database import connectToDatabase

# Import these for method 2
import plotly.graph_objects as go

# Connecting to database
con = connectToDatabase()

# Excecuting query
cur = con.cursor()
cur.execute("SELECT country_name, pop_size FROM country")

# Retrieving results
sql_table = cur.fetchall()

### METHOD 2 ### (Easier to understand my opinion) 

# Isolating x and y tables
x_col = []
y_col = []

for row_number in range(len(sql_table)):
    x_col.append(sql_table[row_number][0])
    y_col.append(sql_table[row_number][1])

# Creating chart
fig_two = go.Figure([go.Bar(x=x_col, y=y_col)])

fig_two.update_layout(
    title = "Population",
    xaxis_title = "country_name",
    yaxis_title = "pop_size",
    dragmode = "pan"
)

fig_two.show()


# # Close database (regardless of method)
con.close()