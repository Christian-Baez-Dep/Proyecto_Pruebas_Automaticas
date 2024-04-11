from Paginas.logins import Make_Login as lg
from Paginas.logins import Make_Login as lg
from Paginas.search import Make_Search
from Paginas.seguir import Follow_Someone
import time

class Follow():
    def __init__(self) -> None:
        pass

    def Prueba():
        login_s = lg()
        inicio = time.time()
        login_s.login_successful()
        Make_Search.Search(login_s.driver)
        Follow_Someone.Follow(login_s.driver)
        login_s.driver.quit()
        final = time.time()
        
        return final - inicio