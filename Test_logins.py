from Paginas.logins import Make_Login as lg
from Paginas.logins import Make_Login as lg
from Paginas.me_gusta import Make_Like
from Paginas.search import Make_Search
from Paginas.seguir import Follow_Someone
from Paginas.historia import Watch_History
import time

class Login():
    def __init__(self) -> None:
        pass

    def PruebaSucces():
        login_s = lg()
        inicio = time.time()
        login_s.login_successful()
        login_s.driver.quit()
        final = time.time()
        
        return final - inicio
    
    def PruebaFailure():
        login_f = lg()
        inicio = time.time()
        login_f.login_failure()
        login_f.driver.quit()
        final = time.time()
        
        return final - inicio




