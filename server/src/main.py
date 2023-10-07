from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from resources import ResourceController
from tokens import Token, SignedToken, TokenManager

app = FastAPI()

@app.get("/resources/assets/{folder}/{file}", response_class=FileResponse)
async def get_asset(folder: str, file: str):
    filepath = f'../resources/assets/{folder}/{file}'
        
    if not ResourceController.ext_exists(file):
        raise HTTPException(status_code=400, detail="Extensão não reconhecida!")
    if not ResourceController.file_exists(filepath):
        raise HTTPException(status_code=400, detail="Recurso não encontrado!")
    
    return FileResponse(path=filepath, media_type=ResourceController.get_ct_type(file))

@app.get("/resources/{file}", response_class=FileResponse)
async def get_resource(file: str):
    filepath = f'../resources/{file}'

    if not file.endswith('.html'):
        return {"error": "extensão não reconhecida!"}
    if not ResourceController.file_exists(filepath):
        raise HTTPException(status_code=400, detail="Recurso não encontrado!")
    
    return FileResponse(path=filepath, media_type="text/html")


@app.post("/auth/create-auth", response_class=JSONResponse)
async def create_auth():
    token = Token(sub=1)
    TokenManager.save_token(token)
    encoded_token = TokenManager.encode_token(token)
    enveloped_token = {'token': encoded_token}

    return JSONResponse(content=enveloped_token)


@app.post("/auth/authenticate", response_class=JSONResponse)
async def authenticate(signed_token: SignedToken):

    return JSONResponse(content=signed_token)
