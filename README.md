# Start and run program locally:

## Prerequisites

1. Python 3.10+ and pip
2. Node.js and npm (for Tailwind)
3. MySQL Server & MySQL Workbench
4. A `.env` file in the project root containing:

```
OMDB_API=your_omdb_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_db_password
DB_NAME=movies_db
```

## Project structure

```
project-root/
├── api/
│   ├── __init__.py
│   ├── database.py       # DB connection and helper functions
│   └── omdb.py           # OMDb API client and search_movie()
├── src/
│   └── input.css         # Tailwind source
├── static/
│   └── css/
│       └── output.css    # Compiled Tailwind CSS
├── templates/
│   ├── search.html       # Search page
│   ├── movie_list.html   # Favourite movies list
│   └── stats.html        # Charts and stats page
├── app.py                # Flask application entrypoint
├── .env                  # Environment variables (not committed)
├── pyproject.toml        # Python dependencies
├── package.json          # npm scripts & dependencies
├── tailwind.config.js    # Tailwind config
└── README.md             # This file
```

## Local setup

1. Install Python dependencies:

   ```bash
   pip install -e . --user
   ```
2. Install npm modules:

   ```bash
   npm install
   ```
3. Build Tailwind CSS watch:

   ```bash
   npx tailwindcss -i src/input.css -o static/css/output.css --watch
   ```
4. Ensure MySQL server is running and the schema `movies_db` exists.
5. Run Flask app:

   ```bash
   python app.py
   ```

## Endpoints

* `/`         : Search and save movies
* `/dashboard`: View saved movies and charts
* `/stats`    : Detailed stats (year & genre charts)

Enjoy!