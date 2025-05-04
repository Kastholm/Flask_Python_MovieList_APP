import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("DB_PW")


def conn_to_db():
    try:
        conn = mysql.connector.connect(
            host="Kastholm.mysql.pythonanywhere-services.com",
            user="Kastholm",
            password=password,
            database="movies_db"
        )
        if conn.is_connected():
            print('Connection to DB Established')
            return conn
    except:
        print('Connection to DB Failed')
    
def fetch_all_movies():
    conn = conn_to_db()
    if not conn:
        return []

    dist = conn.cursor()
    dist.execute("SELECT * FROM movie;")
    data = dist.fetchall()
    
    dist.close()
    conn.close()
    return data


def post_movie(id, title, year, plot, poster, director, genre_str, awards, rating):
    conn = conn_to_db()
    if not conn:
        return

    dist = conn.cursor()
    # Add Movie without Genre
    dist.execute(
        """
        INSERT IGNORE INTO Movie
          (imdbID, Title, Year, Plot, Poster, Director, Awards, Rating)
        VALUES
          (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (id, title, year, plot, poster, director, awards, rating)
    )
    # Add and split genres into DB
    genres = [g.strip() for g in genre_str.split(',')]
    for g in genres:
        # opret genre hvis ikke findes
        dist.execute("INSERT IGNORE INTO Genre (name) VALUES (%s)", (g,))
        # hent genre_id
        dist.execute("SELECT id FROM Genre WHERE name=%s", (g,))
        genre_id = dist.fetchone()[0]
        # link film og genre
        dist.execute(
            "INSERT IGNORE INTO MovieGenre (movie_id, genre_id) VALUES (%s, %s)",
            (id, genre_id)
        )

    conn.commit()
    dist.close()
    conn.close()

def delete_movie(id):
    conn = conn_to_db()
    if not conn:
        return
    
    dist = conn.cursor()

    dist.execute(
        "DELETE FROM Movie WHERE imdbID = %s",
        (id,)
    )

    conn.commit()
    dist.close()
    conn.close()

def fetch_movie_genres():
    conn = conn_to_db()
    dist = conn.cursor()
    dist.execute("""
      SELECT g.name, COUNT(*) 
      FROM Genre g
      JOIN MovieGenre mg ON g.id = mg.genre_id
      GROUP BY g.id
    """)
    data = dist.fetchall() 
    dist.close()
    conn.close()
    return data