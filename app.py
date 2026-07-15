from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

daily_content = [
    {
        "word": "Madrugar",
        "meaning": "To wake up early",
        "example_sentence": "Voy a madrugar mañana para hacer ejercicio.",
        "fun_fact": "In Spain, dinner is often eaten as late as 9 or 10 PM.",
        "song_title": "Cuando Tú Vas by Chenoa",
        "song_link": "https://open.spotify.com/intl-tr/track/2bPH3Ph0RHQuugStXcpyRP?si=d9102029f49e42e0",
        "slang_word": "Guay",
        "slang_meaning": "Cool or awesome (used in Spain)"
    },
    {
        "word": "Anteayer",
        "meaning": "The day before yesterday",
        "example_sentence": "Te vi anteayer en el parque.",
        "fun_fact": "Spanish has a single word for 'day before yesterday' — English doesn't!",
        "song_title": "Lamento Boliviano by Los Enanitos Verdes",
        "song_link": "https://open.spotify.com/intl-tr/track/6Pur3hWy6Nzc27ilmsp5HA?si=9d2aedc2b2b44bae",
        "slang_word": "Chido",
        "slang_meaning": "Cool (used in Mexico)"
    },
    {
        "word": "Esperanza",
        "meaning": "Hope",
        "example_sentence": "Todavía tengo la esperanza de aprobar el examen.",
        "fun fact": "In Columbia, they drink hot chocolate with a thick slice of cheese dropped into it. It is called chocolate santafereño",
        "song_title": "Mil Horas by Los Abuelos De La Nada",
        "song_link": "https://open.spotify.com/track/7Mj6R7TjsPxeLYu0Xdvl73?si=bcc2e676f0cf4f6d",
        "slang_word": "No me des el avión.",
        "slang_meaning": "Don't shrug me off (used in Mexico). Also it literally translates to don't give me the airplane."
    }
        

]

@app.route("/")
def home():
    today = date.today()
    index = today.toordinal() % len(daily_content)
    todays_content = daily_content[index]

    return render_template("home.html", content=todays_content)

if __name__ == "__main__":
    app.run(debug=True)