import sys
sys.path.append("C:/Dados/Git/Python/AulasPythonClt2/Aula6/")

from materia.classes.dao.base_dao import BaseDao
from materia.classes.model.animal import Animal


class AnimalDao(BaseDao):
    def inserir(self, animal):
        comando = f"""
                        INSERT INTO ANIMAL
                        (d
                            NOME_CIENTIFICO
                            ,HABITAT
                            ,TIPO_ALIMENTACAO
                        )
                        VALUES
                        (
                            '{animal.get_nome_cientifico()}'
                            ,'{animal.get_habitat()}'
                            ,'{animal.get_tipo()}'
                        )
                    """
        super().inserir(comando)
        pass

animal_dao = AnimalDao()
animal = Animal()
animal_dao.inserir(animal)

