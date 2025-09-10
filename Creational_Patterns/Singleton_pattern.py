class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls,*args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self,name):
        if not self._initialized:
            # Initialization 
            self._initialized = True
            
        


