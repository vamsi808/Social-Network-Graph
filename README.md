
# Social Network Graph Project

This project is a **Social Network Graph** application that allows users to create profiles, connect with other users, visualize the social network, and perform advanced graph algorithms like shortest path and friend recommendations. It uses Flask for the back-end, NetworkX for graph operations, and Vis.js for front-end visualization.

## Features

- **User Profile**: Create and manage user profiles.
- **Connections**: Add and remove connections (friends) between users.
- **Friend Recommendations**: Get friend recommendations based on mutual connections.
- **Shortest Path**: Find the shortest path between two users in the network.
- **Social Network Visualization**: Visualize the social network graph using an interactive interface.

## Technologies Used

- **Back-End**: Flask (Python), SQLAlchemy, NetworkX
- **Front-End**: HTML, CSS, JavaScript, Vis.js
- **Database**: SQLite

## Setup Instructions

### Prerequisites

Make sure you have **Python 3.x** installed. You will also need `pip` for managing Python packages.

### Installation

1. Clone the repository or download the zip file.
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install Flask Flask-SQLAlchemy NetworkX
    ```

4. Set up the database:
    ```bash
    python
    >>> from app import db
    >>> db.create_all()
    ```

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your browser and navigate to `http://localhost:5000/`.

## Endpoints

- **POST `/add_user`**: Add a new user.
    - Request Body: `{ "username": "user_name" }`
    - Response: `{ "message": "User added successfully" }`

- **POST `/add_connection`**: Add a connection (friendship) between two users.
    - Request Body: `{ "user1": "user_name1", "user2": "user_name2" }`
    - Response: `{ "message": "Connection added successfully" }`

- **GET `/get_connections/<username>`**: Get the list of connections for a user.
    - Response: `{ "user": "user_name", "connections": ["user1", "user2"] }`

- **GET `/friend_recommendation/<username>`**: Get friend recommendations based on mutual connections.
    - Response: `{ "user": "user_name", "recommendations": ["user1", "user2"] }`

- **GET `/shortest_path/<user1>/<user2>`**: Get the shortest path between two users.
    - Response: `{ "path": ["user1", "user2", "user3"] }`

## Contributing

Feel free to fork this project and create pull requests. Contributions are welcome!

## Acknowledgements

- Flask documentation: https://flask.palletsprojects.com/
- NetworkX documentation: https://networkx.github.io/
- Vis.js documentation: https://visjs.org/

### Author

Created by K.Vamsi.
