import typer
from app.database import SessionLocal
from app.models.users_model import UsersModel
from app.schemes.user_schemes import UserRole
from app.hashing import getHash

app = typer.Typer()

@app.command()
def createsuperuser(username: str, password: str
):
    db = SessionLocal()
    try: 
        existing_user = db.query(UsersModel).filter(UsersModel.user_name == username).first()
        if existing_user: 
            typer.echo(f"Error: User {username} already exists!")
            return
        
        salt, hash_password = getHash(password)
        
        new_admin = UsersModel(
            user_name = username,
            user_password = hash_password,
            salt = salt,
            role = UserRole.admin,
        )
        
        db.add(new_admin)
        db.commit()
        typer.echo(f" Admin {username} successfully created!")
        
    except Exception as e:
        typer.echo(f"Error when creating: {e}")
    finally:
        db.close()
        
if __name__ == "__main__":
    app()
    