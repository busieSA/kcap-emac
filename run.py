from app import app_starter

app = app_starter()


if __name__ == "__main__":
    app.run(debug=True)