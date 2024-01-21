# Flask Web Application with Infinite Scrolling using HTMLX

This repository hosts a Flask-based web application that leverages [HTMLX](https://htmx.org/) to provide an infinite scrolling feature. The application displays a webpage where users can endlessly scroll through a large collection of memes, with new memes being loaded as the user scrolls further down.

## Structure of the Project

- `app.py`: The primary Python script that initiates the Flask application.
- `instance/`: This directory holds SQLite db which already had some data in it.
- `static/`: This directory stores static files such as CSS and JavaScript. Notably, it includes `htmx.min.js`, the HTMLX library that powers the infinite scrolling feature.
- `templates/`: This directory is home to the HTML templates for the webpages. The `index.html` file serves as the main webpage, `render_memes.html` is responsible for rendering the meme templates, and `helpers.html` contains reusable micro-templates.

## How to Run the Application

To launch the application, open your terminal, navigate to the project directory, and execute the following command:

```sh
python app.py