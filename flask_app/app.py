
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import networkx as nx

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_network.db'
db = SQLAlchemy(app)

# Initialize an empty graph
G = nx.Graph()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    connections = db.relationship('Connection', backref='user', lazy=True)

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    connected_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Initialize database
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    G.add_node(username)  # Add the user to the graph
    return jsonify({"message": f"User {username} added successfully"}), 201

@app.route('/add_connection', methods=['POST'])
def add_connection():
    data = request.json
    user1 = data.get('user1')
    user2 = data.get('user2')

    if not (User.query.filter_by(username=user1).first() and User.query.filter_by(username=user2).first()):
        return jsonify({"message": "One or both users not found"}), 404
    
    # Add to database
    user1_obj = User.query.filter_by(username=user1).first()
    user2_obj = User.query.filter_by(username=user2).first()

    connection1 = Connection(user_id=user1_obj.id, connected_user_id=user2_obj.id)
    connection2 = Connection(user_id=user2_obj.id, connected_user_id=user1_obj.id)
    
    db.session.add(connection1)
    db.session.add(connection2)
    db.session.commit()
    
    # Add the connection to the graph
    G.add_edge(user1, user2)
    return jsonify({"message": f"Connection between {user1} and {user2} added"}), 201

@app.route('/get_connections/<username>', methods=['GET'])
def get_connections(username):
    if not User.query.filter_by(username=username).first():
        return jsonify({"message": "User not found"}), 404

    connections = list(G.neighbors(username))
    return jsonify({"user": username, "connections": connections})

@app.route('/friend_recommendation/<username>', methods=['GET'])
def friend_recommendation(username):
    if not User.query.filter_by(username=username).first():
        return jsonify({"message": "User not found"}), 404

    # Recommend friends based on mutual connections
    recommendations = []
    for neighbor in G.neighbors(username):
        for mutual in G.neighbors(neighbor):
            if mutual != username and mutual not in G.neighbors(username):
                recommendations.append(mutual)
    return jsonify({"user": username, "recommendations": recommendations})

@app.route('/shortest_path/<user1>/<user2>', methods=['GET'])
def shortest_path(user1, user2):
    if not (User.query.filter_by(username=user1).first() and User.query.filter_by(username=user2).first()):
        return jsonify({"message": "One or both users not found"}), 404

    # Find the shortest path
    try:
        path = nx.shortest_path(G, source=user1, target=user2)
        return jsonify({"path": path})
    except nx.NetworkXNoPath:
        return jsonify({"message": "No path found between the users"}), 404

if __name__ == '__main__':
    app.run(debug=True)
