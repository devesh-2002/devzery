# Devzery
## Tech Stack
1. Flask
2. PostgreSQL
3. React.js

## Running the Project
1. Fork and Clone the Repository.
2. Move to the backend directory.
```
cd backend
```
3. Install the requirements.txt file
```
pip install -r requirements.txt
```
4. Make a .env file and add the PostgreSQL username (DB_USERNAME), password (DB_PASSWORD), host (DB_HOST), Database Name (DB_NAME) in it.
5. Run the Flask server.
```
python app.py
```
6. Open another terminal, and move to frontend directory.
```
cd frontend
```
7. Install the packages
```
yarn
```
8. Run the frontend
```
yarn dev
```
### Verify Data in PostgreSQL
1. Open psql Command Shell
2. `\l` for viewing all databases.
3. `\c <db-name>` for switching to the database where data is stored.
4. `select * from "user";` for viewing all the records.
