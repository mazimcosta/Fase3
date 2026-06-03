
from models.quarto import Quarto
from models.cliente import Cliente
from models.reserva import Reserva

from repositories.cliente_repository import ClienteRepository
from repositories.quarto_repository import QuartoRepository
from repositories.reserva_repository import ReservaRepository
from services.reserva_service import ReservaService
from services.cliente_service import ClienteService
from services.quarto_service import QuartoService


def fluxo_normal():
    cliente_repositorio=ClienteRepository()
    quarto_repositorio=QuartoRepository()
    reserva_repositorio=ReservaRepository()
    cliente_service=ClienteService(cliente_repositorio)
    quarto_service=QuartoService(quarto_repositorio)

    

    reserva_service=ReservaService(reserva_repositorio,cliente_repositorio,quarto_repositorio)
    cliente1=Cliente('Maria',45789451224)
    cliente2=Cliente('Joao',4567894512)
    cliente3=Cliente('Marcos',124578954)

    quarto1=Quarto(125,'luxo',150.0)
    quarto2=Quarto(254,'padrao',160.50)
    quarto3=Quarto(321,'luxo',250.50)

    # cliente_service.cadastrar_cliente(cliente1)
    # cliente_service.cadastrar_cliente(cliente2)
    # cliente_service.cadastrar_cliente(cliente3)

    # quarto_service.cadastrar_quarto(quarto1)
    # quarto_service.cadastrar_quarto(quarto2)
    # quarto_service.cadastrar_quarto(quarto3)

    reserva1=Reserva(1,1,20)
    reserva2=Reserva(2,2,25)
    reserva3=Reserva(3,3,45)

    # reserva_service.criar_reserva(reserva1)
    # reserva_service.criar_reserva(reserva2)
    # reserva_service.criar_reserva(reserva3)

    # try:
    #     reserva_service.criar_reserva(reserva1)
    # except ValueError as error:
    #     print(error)
    
    # try:
    #     reserva_erro_cliente=Reserva(999,1,3)
    #     reserva_service.criar_reserva(reserva_erro_cliente)
    # except ValueError as error:
    #     print(error)

    # try:
    #     reserva_erro_quarto=Reserva(1,999,3)
    #     reserva_service.criar_reserva(reserva_erro_quarto)
    # except ValueError as error:
    #     print(error)

    # try:
    #     reserva_quarto_ocupado=Reserva(1,1,3)
    #     reserva_service.criar_reserva(reserva_quarto_ocupado)
    # except ValueError as error:
    #     print(error)
    reserva_service.cancelar_reserva(1)
    return 


fluxo_normal()    

    