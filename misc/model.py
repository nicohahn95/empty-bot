import tomllib
import json
from misc import T

class Model:
    def __init__(self, config_path: str, runtime_path: str):
        self._config = self._load_config(config_path)
        self._runtimepath = runtime_path

    async def update_runtime(self):
        with open(self._runtimepath, 'r') as file:
            self._runtime = json.load(file)
            self.LWstate = self._runtime["LWstate"]
            self.KFstate = self._runtime["KFstate"]
    
    def editLWstate(self, state: int):
        self._runtime["LWstate"] = state
        with open (self._runtimepath, "w") as f:
            json.dump(self._runtime, f, indent = 4)

    def editKFstate(self, state: int):
        self._runtime["KFstate"] = state
        with open (self._runtimepath, "w") as f:
            json.dump(self._runtime, f, indent = 4)   

    @staticmethod
    def _load_runtime(path: str) -> T.Config:
        with open(path, "r") as f:
            return json.loads(f.read())


    @staticmethod
    def _load_config(path: str) -> T.Config:
        with open(path, "r") as f:
            return tomllib.loads(f.read())

    @property
    def c(self) -> T.Config:
        return self._config
