import os
from stat import *
from abc import ABC, abstractmethod


class IController(ABC):
    apiPath:str
    
    @property
    @abstractmethod
    def max_brtn(self): ...

    @property
    @abstractmethod
    def cur_brtn(self): ...
    
    @abstractmethod
    def set_brtn(self): ...


class Controller(IController):
    _maxBrtnFile = 'max_brightness'
    _curBrtnFile = 'brightness'

    def __init__(self, apiPath: str, isRec: bool=False):
        self.apiPath: str = apiPath
        self.isRecovered: bool = isRec
        self.curBrtnApi: str = os.path.join(apiPath, self._curBrtnFile)
        self.maxBrtnApi: str = os.path.join(apiPath, self._maxBrtnFile)
        self.recoverValue: int = self.cur_brtn
        
        self.checkAndGivePermissions()

    def __del__(self):
        if self.isRecovered:
            self.set_brtn(self.recoverValue)

    def checkAndGivePermissions(self):
        EXP_MODE = 0o660
        EXP_MODE_S = S_IMODE(EXP_MODE) 
        
        filesToCheck = [
                self.curBrtnApi,
                self.maxBrtnApi
            ]

        for file in filesToCheck:
            cfs = os.stat(file)

            if cfs != EXP_MODE_S:
                os.chmod(file, EXP_MODE)
        


    @property
    def max_brtn(self) -> int:
        try:
            with open(self.maxBrtnApi, 'r') as mApi:
                return int(mApi.read())
        except PermissionError:
            raise PermissionError(f'Cannot get max brightness from file {self.maxBrtnApi}')

    
    @property
    def cur_brtn(self) -> int:
        try:
            with open(self.curBrtnApi, 'r') as cApi:
                return int(cApi.read())
        except PermissionError:
            raise PermissionError(f'Cannot get current brightness from file {self.curBrtnApi}')

    def set_brtn(self, newValue: int) -> bool:
        try:
            if newValue < 0 or newValue > self.max_brtn:
                return False

            with open(self.curBrtnApi, 'w') as cApi:
                cApi.write(str(newValue))
                return True
        except PermissionError:
            raise PermissionError(f'Cannot set new value to file {self.curBrtnApi}')
