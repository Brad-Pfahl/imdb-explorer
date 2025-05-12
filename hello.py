from preswald import connect, get_df, text

connect() # Initialize connection to preswald.toml data sources
df = get_df("data/imdb.csv")

from preswald import query

sql = "SELECT * FROM 'data/imdb.csv' WHERE averageRating >= '8.5'"
filtered_df= query(sql, "data/imdb.csv")

# Interactive Table- Top IMDb Movie Table with rating >= 8.5
from preswald import table

text("# Top IMDb Movies")
table(filtered_df, title="Highly Rated Films")

# Box graph visualization of distributions of ratings by genre
from preswald import plotly
import plotly.express as px

# Ensure no nulls before plotting
filtered_df = filtered_df[filtered_df["releaseYear"].notnull()]
filtered_df["releaseYear"] = filtered_df["releaseYear"].astype(int)

# Clean and explode multi-genre entries
df_genres = filtered_df.copy()
df_genres = df_genres[df_genres["genres"].notnull()]
df_genres["genres"] = df_genres["genres"].str.split(", ")
df_genres = df_genres.explode("genres")  # One row per genre

fig = px.box(df_genres, x="genres", y="averageRating", title="Distributions of Ratings by Genre")
plotly(fig)