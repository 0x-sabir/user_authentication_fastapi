from fastapi import FastAPI 
from routers import authentication,checkauthorization,signup
from mydb.database import Base, engine
from mydb import models



app = FastAPI()



models.Base.metadata.create_all(bind=engine)



app.include_router(authentication.router)
app.include_router(signup.router)
app.include_router(checkauthorization.router)