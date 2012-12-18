# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2012 Proge Informática Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author Daniel Hartmann <daniel@proge.com.br>                              #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                            #
##############################################################################

import sys
sys.path.append('..')

import pysped_efd

efd = pysped_efd.efd(
    COD_FIN='',
    DT_INI='',
    DT_FIN='',
    NOME='',
    CNPJ='',
    CPF='',
    UF='',
    IE='',
    COD_MUN='',
    IM='',
    SUFRAMA='',
    IND_PERFIL='',
    IND_ATIV=''
    )
reg = pysped_efd.r0005(
    FANTASIA='Empresa Um Ltda',
    CEP='95900-000',
    END='R. Primeira',
    NUM='1',
    COMPL='101',
    BAIRRO='Único',
    FONE='11 3011 1103',
    FAX='',
    EMAIL='responsavel@empresa.com.br',
    )

reg.FAX = '11 3011 1104'

efd.add(reg)

print efd.generate()
