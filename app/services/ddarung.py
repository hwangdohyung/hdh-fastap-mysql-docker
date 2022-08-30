from app.models.ddarung import DDarung

class DDarung:
    def __init__(self) -> None:
        pass
    
    def submit(self, path, train, test):
        ddarung = DDarung()
        ddarung.hook(path, train, test)
                
       
        
    
