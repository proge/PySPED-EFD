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

from registers import *


class efd:
    registers = {
        '0': [],
        'C': [],
        'D': [],
        'E': [],
        'G': [],
        'H': [],
        '1': [],
        '9': [],
        }

    def add(self, reg):
        self.registers[reg.block].append(reg)

    def _generate_end_blocks(self):
        '''Generate end blocks' data'''

        # Count all registers 
        total_len = 0

        # Count each register type
        reg_len = {}

        for block in self.registers:
            block_len = len(self.registers[block])

            if block_len > 0:
                reg = None

                # Sum the register tha will be added
                block_len += 1

                # Create register for the end of the current block
                if block == '0':
                    reg = r0990(QTD_LIN_0=block_len)
                elif block == 'C':
                    reg = rC990(QTD_LIN_C=block_len)
                elif block == 'D':
                    reg = rD990(QTD_LIN_D=block_len)
                elif block == 'E':
                    reg = rE990(QTD_LIN_E=block_len)
                elif block == 'G':
                    reg = rG990(QTD_LIN_G=block_len)
                elif block == 'H':
                    reg = rH990(QTD_LIN_H=block_len)
                elif block == '1':
                    reg = r1990(QTD_LIN_1=block_len)

                if reg:
                    self.registers[block].append(reg)

                # Sum one for each register type
                for register in self.registers[block]:
                    try:
                        reg_len[register.REG] += 1
                    except:
                        reg_len[register.REG] = 1

        # Sum the count of each block
        for block in self.registers:
            block_len = len(self.registers[block])
            total_len += block_len

        if total_len != 0:
            self.registers['9'].append(r9001(IND_MOV=0))
        else:
            self.registers['9'].append(r9001(IND_MOV=1))
        total_len += 1

        for reg in reg_len:
            self.registers['9'].append(r9900(
                REG_BLC=reg,
                QTD_REG_BLC=reg_len[reg],
                ))
            total_len += 1

        # Sum registers 9990 and 9999
        self.registers['9'].append(r9990(
            QTD_LIN_9=len(self.registers['9']) + 2
            ))

        # Again, sum registers 9990 and 9999
        total_len += 2
        self.registers['9'].append(r9999(QTD_LIN=total_len))

    def generate(self):
        '''Generate EFD file content'''
        self._generate_end_blocks()

        lines = []

        for block in self.registers:
            for reg in self.registers[block]:
                reg_dict = reg.attrs
                line = '|'.join(map(str,
                    [reg.__getattribute__(key) for key in reg_dict]
                    ))
                lines.append('|{}|{}|'.format(reg.REG, line))

        return '\r\n'.join(lines)
