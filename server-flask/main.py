from website import create_app

app = create_app()

# makes sure that the server is only run when main.py is being run
if __name__ == '__main__':
    app.run(debug=True)