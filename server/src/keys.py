
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import hmac
import base64

class KeyManager():

    public_key_path: str = "/keys/public_key.pem"
    private_key_path: str = "/keys/private_key.pem"
    private_key_password: str = "92471d06-3ee3-47ba-9d64-d7a4ce29e63d"
    
    def generate_key_pair():
        '''
        gera um par de chaves rsa para autenticação de token dos viajantes
        '''

        public_key_dir, _ = os.path.split(KeyManager.public_key_path)
        private_key_dir, _ = os.path.split(KeyManager.private_key_path)

        if not os.path.exists(public_key_dir):
            os.mkdir(public_key_dir)

        if not os.path.exists(private_key_dir):
            os.mkdir(private_key_dir)

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(KeyManager.private_key_password.encode())
        )

        public_key = private_key.public_key()

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open(KeyManager.private_key_path, "wb") as file:
            file.write(private_pem)

        with open(KeyManager.public_key_path, "wb") as file:
            file.write(public_pem)

    def get_private_key():
        '''
        obtém a chave privada utilizada para criptografar os tokens dos viajantes
        '''

        with open(KeyManager.private_key_path, "rb") as file:
            private_pem = file.read()
            private_key = serialization.load_pem_private_key(
                private_pem, 
                password=KeyManager.private_key_password.encode(), 
                backend=default_backend())

        return private_key

    def get_public_key():
        '''
        obtém a chave pública utilizada para descriptografar os tokens dos viajantes
        '''

        with open(KeyManager.public_key_path, "rb") as file:
            public_pem = file.read()
            public_key = serialization.load_pem_public_key(
                public_pem, 
                backend=default_backend())
            
        return public_key

'''
KeyManager.generate_key_pair()
KeyManager.get_public_key()
KeyManager.get_private_key()
'''