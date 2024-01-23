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
4. Create virtual environment and depending on OS, activate it.
```
virtualenv env
env/Scripts/activate
```
or 
```
virtualenv env
source env/Scripts/activate
```
5. Make a .env file and add the PostgreSQL username (DB_USERNAME), password (DB_PASSWORD), host (DB_HOST), Database Name (DB_NAME) in it.
```
DB_USERNAME=
DB_PASSWORD=
DB_HOST=
DB_NAME=
```
6. Run the Flask server.
```
python app.py
```
7. Open another terminal, and move to frontend directory.
```
cd frontend
```
8. Install the packages
```
yarn
```
9. Run the frontend
```
yarn dev
```
### Verify Data in PostgreSQL
1. Open psql Command Shell
2. `\l` for viewing all databases.
3. `\c <db-name>` for switching to the database where data is stored.
4. `select * from "user";` for viewing all the records.
