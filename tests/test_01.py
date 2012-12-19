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
    COD_FIN='0',
    DT_INI='15122012',
    DT_FIN='19122012',
    NOME='Empresa Um Ltda',
    CNPJ='77300486760765',
    CPF='',
    UF='RS',
    IE='2241025806',
    COD_MUN='4300034',
    IM='',
    SUFRAMA='',
    IND_PERFIL='A',
    IND_ATIV='1'
    )

print efd.generate()
