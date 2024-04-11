from Paginas.logins import Make_Login as lg
from Paginas.logins import Make_Login as lg
from Paginas.me_gusta import Make_Like
from Paginas.search import Make_Search
from Paginas.seguir import Follow_Someone
from Paginas.historia import Watch_History
import time

class Like():
    def __init__(self) -> None:
        pass

    def Prueba():
        login_s = lg()
        inicio = time.time()
        login_s.login_successful()
        Make_Like.Like(login_s.driver)
        login_s.driver.quit()
        final = time.time()
        
        return final - inicio


