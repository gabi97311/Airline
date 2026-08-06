import asyncio

import typer
from app.database import AsyncSessionLocal
from Airline.auth.src.users_model import UsersModel
from Airline.flight_auth.app.users.user_schemes import UserRole
from Airline.auth.src.hashing import getHash
from sqlalchemy import select

app = typer.Typer()

async def create_user_logic(username, password):
    async with AsyncSessionLocal() as db:
        try: 
            stmt = select(UsersModel).where(UsersModel.user_name == username)
            result = await db.execute(stmt)
            existing_user = result.scalar_one_or_none()
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
            await db.commit()
            typer.echo(f" Admin {username} successfully created!")
            
        except Exception as e:
            await db.rollback()
            typer.echo(f"An error occurred: {e}")
        finally:
            await db.close()

@app.command()
def createsuperuser(username: str, password: str):
    asyncio.run(create_user_logic(username, password))
        
if __name__ == "__main__":
    app()
    