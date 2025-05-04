import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from flask import Flask, render_template
from io import BytesIO
import base64
from flask import Flask, render_template, request
from api import search_movie, fetch_all_movies, post_movie, delete_movie, fetch_movie_genres

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('search.html')


@app.route('/movie_list')
def movie_list():
    movies = fetch_all_movies()
    return render_template('movie_list.html', movies=movies)

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    delete_movie(id)
    status = True
    movies = fetch_all_movies()
    return render_template('movie_list.html', status=status, movies=movies)


@app.route('/search')
def search():
    q = request.args.get('q', '')
    movies = search_movie(q)
    return render_template('search.html', movies=movies)

@app.route('/save', methods=['POST'])
def post():
    imdb_id  = request.form['id']
    title     = request.form['title']
    year      = request.form['year']
    plot      = request.form['plot']
    poster    = request.form['poster']
    director  = request.form['director']
    genre     = request.form['genre']
    awards    = request.form['awards']
    rating    = request.form['rating']

    post_movie(imdb_id, title, year, plot, poster, director, genre, awards, rating)

    status = True
    return render_template('search.html', status=status)

@app.route('/stats')
def stats():
    movies = fetch_all_movies()    

    # Bar chart (movies per year)
    years_raw = [m[2].split('–',1)[0] for m in movies]
    years  = sorted(set(years_raw))
    counts = [years_raw.count(y) for y in years]
    fig1 = plt.figure(figsize=(12,4))
    plt.bar(years, counts)
    buf1 = BytesIO(); fig1.savefig(buf1, format='png')
    bar_img = base64.b64encode(buf1.getvalue()).decode()
    plt.close(fig1)

    # Pie chart (movies per genre)
    genre_data = fetch_movie_genres()
    labels, genre_counts = zip(*genre_data) if genre_data else ([],[])
    fig2 = plt.figure(figsize=(12, 8))
    plt.pie(genre_counts, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    buf2 = BytesIO(); fig2.savefig(buf2, format='png')
    pie_img = base64.b64encode(buf2.getvalue()).decode()
    plt.close(fig2)

    return render_template(
      'stats.html',
      movies=movies,
      bar_img=bar_img,
      pie_img=pie_img
    )



if __name__ == '__main__':

    """ Starter server """
    app.run(debug=True) 