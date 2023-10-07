import json
from json import JSONDecodeError

class Settings:
    _instance = None

    def __new__(cls, file_path):
        
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls._instance.path = file_path
            cls._instance.load_settings()
        return cls._instance

    def load_settings(self):
        try:
            with open(self.path, 'r') as file:
                self.settings = dict(json.load(file))
        except FileNotFoundError:
            raise FileNotFoundError("arquivo de configuração settings.json não encontrado")
        except JSONDecodeError:
            raise ValueError("erro de decodificação do arquivo JSON")
        
    def get(self, key, default=None):
        self.settings.get()
        return self.settings.get(key, default)

        
config = Settings('settings/settings.json')

app_config = dict(config.get("application"))
db_config = dict(config.get("database"))
jwt_config = dict(config.get("jwt"))
resource_config = dict(config.get("resources"))

