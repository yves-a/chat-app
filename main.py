from socket import SocketIO
from application import create_app
import time
from flask_socketio import SocketIO
from application.msg_database import Database

# Create the app
app = create_app()
socketio = SocketIO(app)

@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    '''
    handles the incoming messages from the server and saves them to
    the database
    '''
    
    data = dict(json)
    
    if "name" in data:
        db = Database()
        
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', json)


if __name__ == "__main__":
    socketio.run(app,debug=True, host="0.0.0.0",port=9999)

    