import threading
import os
from gui import GUI
from app import app  
from werkzeug.serving import make_server

def run_flask_app():
    app.run(debug=False, use_reloader=False) 

def run_gui():
    gui = GUI()
    gui.run()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.daemon = True  
    flask_thread.start()

    run_gui()

    flask_thread.join()
