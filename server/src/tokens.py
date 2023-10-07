from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import datetime, timedelta
import uuid
import jwt
from jwt import InvalidSignatureError, ExpiredSignatureError, DecodeError, PyJWTError
import mysql.connector
from mysql.connector import Error
from keys import KeyManager
import json
from json import JSONDecodeError

app_name = 'assistente_viagens'
audience = 'client'

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "Bearer"
    expires_in: int
    scope: str = 'client'

class Token():
    def __init__(self, header: dict[str, str], payload: dict[str, any], signature: str):
        self.header: dict[str, str] = header
        self.payload: dict[str, any] = payload
        self.signature: str = signature

    @classmethod
    def new(cls, subject_id: int, duration: int = 5*(60*60*24*365)):
        header = {'alg': 'RS256', 'typ': 'JWT'}
        payload = {
            'iss': app_name,
            'aud': audience,
            'sub': subject_id,
            'jti': str(uuid.uuid4()),
            'iat': int(datetime.now().timestamp()),
            'nbf': int(datetime.now().timestamp()),
            'exp': int((datetime.now()+timedelta(seconds=duration)).timestamp())
        }
        signature = jwt.encode(payload=payload, key=KeyManager.get_private_key(), algorithm=header['alg'])   
        return cls(header, payload, signature)
    
    @classmethod
    def from_sign(cls, sig: str, alg: str='RS256', typ: str='JWT', aud: str='client'):
        try:
            header = {'alg': alg, 'typ': typ}
            payload = jwt.decode(jwt=sig, key=KeyManager.get_public_key(), algorithms=[alg, ], audience=aud)
            signature = sig
            return cls(header, payload, signature)
        except PyJWTError as e:
            print("erro na decodificação do token!", e)

    @classmethod
    def from_dict(cls, dictionary: dict[str, any]):
        return cls(**dictionary)
    
    @classmethod
    def from_json(cls, json_str: str):
        dictionary = dict[str, any](json.loads(json_str))
        return cls(**dictionary)

    @classmethod
    def from_db(cls, data: dict):
        header = {'alg': data['alg'], 'typ': data['typ']}
        payload = {
            'iss': data['iss'],
            'aud': data['aud'],
            'sub': data['sub'],
            'jti': data['jti'],
            'iat': data['iat'],
            'nbf': data['nbf'],
            'exp': data['exp']
        }
        signature = data['sig'] 
        return cls(header, payload, signature)

    def to_db(self):
        header = tuple(self.header.values())
        payload = tuple(self.payload.values())
        signature = tuple(self.signature)
        return header + payload + signature

    def to_dict(self) -> dict[str, any]:
        return self.__dict__

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def sign(self) -> str:
        self.signature = jwt.encode(payload=self.payload, key=key, algorithm=self.header['alg'])
        return self.signature

    def renew(self, duration: int = 5*(60*60*24*365)) -> None:
        self.payload['nbf'] = int(datetime.now().timestamp())
        self.payload['exp'] = int((datetime.now()+timedelta(seconds=duration)).timestamp())
        self.signature = self.sign()

    def is_expired(self) -> bool:
        now = int(datetime.now().timestamp())
        return (self.payload['exp'] < now)

    def is_valid(self) -> bool:
        pass
'''
tk = Token.new(subject_id=1)
print(tk.to_json())
tk2 = Token.from_sign(tk.signature)
print(tk2.to_json())
'''

class TokenDatabase():

    def __init__(self, host='localhost', user='user', password='12345', database='travel_assistant_db'):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def create_token(self, token: Token) -> None:
        try:
            connection = mysql.connector.connect(**self.config)
            if connection.is_connected():
                print("Conexão bem-sucedida ao MySQL")
            cursor = connection.cursor()
            query = "INSERT INTO token (alg, typ, iss, aud, sub, jti, iat, nbf, exp, sig) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = token.to_db()
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            print("Token salvo na base de dados com sucesso!")
        except Error as e:
            print("Erro ao salvar o token na base de dados!", e)

    def read_token(self, subject_id: int) -> Token:
        try:
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM token WHERE sub = %s"
            cursor.execute(query, (subject_id,))
            token_dict = cursor.fetchone()
            cursor.close()
            connection.close()
            print("Token obtido da base de dados com sucesso!")
            if token_dict:
                return Token.from_db(token_dict)
            else:
                print(f"Nenhum token com id = {subject_id} foi encontrado na base de dados")
        except ValidationError as e:
            print("Token da base de dados é inválido:", e)
        except Error as e:
            print("Erro ao obter o token da base de dados:", e)

    def update_token(self, token: Token) -> None:
        try:
            connection = mysql.connector.connect(**self.config)
            if connection.is_connected():
                print("Conexão bem-sucedida ao MySQL")
            cursor = connection.cursor()
            query = "UPDATE token SET alg=%s, typ=%s, iss=%s, aud=%s, jti=%s, iat=%s, nbf=%s, exp=%s, sig=%s WHERE sub=%s"
            values = (token.header['alg'], token.header['typ'], token.payload['iss'], token.payload['aud'], token.payload['jti'], 
                      token.payload['iat'], token.payload['nbf'], token.payload['exp'], token.signature, token.payload['sub'])
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            print("Token atualizado na base de dados com sucesso!")
        except Error as e:
            print("Erro ao atualizar o token na base de dados!", e)

    def delete_token(self, subject_id: int) -> None:
        try:
            connection = mysql.connector.connect(**self.config)
            if connection.is_connected():
                print("Conexão bem-sucedida ao MySQL")
            cursor = connection.cursor()
            query = "DELETE FROM token WHERE sub = %s"
            cursor.execute(query, (subject_id,))
            connection.commit()
            cursor.close()
            connection.close()
            print(f"Token com id={subject_id} foi excluido da base de dados!")
        except Error as e:
            print("Erro ao deletar o token da base de dados!", e)


tk = Token.new(subject_id=12)
tkdb = TokenDatabase()


tkdb.create_token(tk)
print(tkdb.read_token(tk.payload['sub']).to_json())
tk.renew()
tkdb.update_token(tk)
# tkdb.delete_token(tk.payload['sub'])


class TokenManager():

    token_type = 'JWT'
    token_algorithm = 'RS256'
    token_exp_secs = 5*(60*60*24*365)
        
    def encode_token(token: Token) -> str:
        return jwt.encode(payload=token.payload, key=KeyManager.get_private_key(), algorithm=token.header['alg'])
        
    def decode_token(encoded_token: str) -> Token:
        try:
            header = {'alg': 'RS256', 'typ': 'JWT'}
            payload = jwt.decode(jwt=encoded_token, key=KeyManager.get_public_key(), algorithms=['RS256', ], audience='client')
            signature = encoded_token
            return Token(header, payload, signature)
        except ExpiredSignatureError as e:
            print("o token expirou!", e)
        except InvalidSignatureError as e:
            print("assinatura não é válida!", e)
        except DecodeError as e:
            print("token é inválido!", e)
        except PyJWTError as e:
            print("erro na decodificação do token!", e)