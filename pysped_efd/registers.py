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

import collections

def register(reg_number, field_names):
    typename = 'r{}'.format(reg_number)
    reg = collections.namedtuple(typename, field_names)

    class register(reg):
        REG = reg_number

    return register


# Block 0
r0000 = register('0000', (
    'COD_VER', 'COD_FIN', 'DT_INI', 'DT_FIN', 'NOME', 'CNPJ', 'CPF', 'UF',
    'IE', 'COD_MUN', 'IM', 'SUFRAMA', 'IND_PERFIL', 'IND_ATIV',
    ))
r0001 = register('0001', ('IND_MOV',))
r0005 = register('0005', (
    'FANTASIA', 'CEP', 'END', 'NUM', 'COMPL', 'BAIRRO', 'FONE', 'FAX',
    'EMAIL',
    ))
r0015 = register('0015', ('UF_ST', 'IE_ST'))
r0100 = register('0100', (
    'NOME', 'CPF', 'CRC', 'CNPJ', 'CEP', 'END', 'NUM', 'COMPL', 'BAIRRO',
    'FONE', 'FAX', 'EMAIL', 'COD_MUN',
    ))
r0150 = register('0150', (
    'COD_PART', 'NOME', 'COD_PAIS', 'CNPJ', 'CPF', 'IE', 'COD_MUN', 'SUFRAMA',
    'END', 'NUM', 'COMPL', 'BAIRRO',
    ))
r0175 = register('0175', ('DT_ALT', 'NR_CAMPO', 'CONT_ANT'))
r0190 = register('0190', ('UNID', 'DESCR'))
r0200 = register('0200', (
    'COD_ITEM', 'DESCR_ITEM', 'COD_BARRA', 'COD_ANT_ITEM', 'UNID_INV',
    'TIPO_ITEM', 'COD_NCM', 'EX_IPI', 'COD_GEN', 'COD_LST', 'ALIQ_ICMS',
    ))
r0205 = register('0205', (
    'DESCR_ANT_ITEM', 'DT_INI', 'DT_FIM', 'COD_ANT_ITEM',
    ))
r0206 = register('0206', ('COD_COMB',))
r0220 = register('0220', ('UNID_CONV', 'FAT_CONV'))
r0300 = register('0300', (
    'COD_IND_BEM', 'IDENT_MERC', 'DESCR_ITEM', 'COD_PRNC', 'COD_CTA',
    'NR_PARC',
    ))
r0305 = register('0305', ('COD_CCUS', 'FUNC', 'VIDA_UTIL'))
r0400 = register('0400', ('COD_NAT', 'DESCR_NAT'))
r0450 = register('0450', ('COD_INF', 'TXT'))
r0460 = register('0460', ('COD_OBS', 'TXT'))
r0500 = register('0500', (
    'DT_ALT', 'COD_NAT_CC', 'IND_CTA', 'NIVEL', 'COD_CTA', 'NOME_CTA',
    ))
r0600 = register('0600', ('DT_ALT', 'COD_CCUS', 'CCUS'))
r0990 = register('0990', ('QTD_LIN_0',))

# Block C
rC001 = register('C001', ('IND_MOV',))
rC100 = register('C100', (
    'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'NUM_DOC',
    'CHV_NFE', 'DT_DOC', 'DT_E_S', 'VL_DOC', 'IND_PGTO', 'VL_DESC',
    'VL_ABAT_NT', 'VL_MERC', 'IND_FRT', 'VL_FRT', 'VL_SEG', 'VL_OUT_DA',
    'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_IPI', 'VL_PIS',
    'VL_COFINS', 'VL_PIS_ST', 'VL_COFINS_ST',
    ))
rC105 = register('C105', ('OPER', 'UF'))
rC110 = register('C110', ('COD_INF', 'TXT_COMPL'))
rC111 = register('C111', ('NUM_PROC', 'IND_PROC'))
rC112 = register('C112', (
    'COD_DA', 'UF', 'NUM_DA', 'COD_AUT', 'VL_DA', 'DT_VCTO', 'DT_PGTO',
    ))
rC113 = register('C113', (
    'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'SER', 'SUB', 'NUM_DOC',
    'DT_DOC',
    ))
rC115 = register('C115', (
    'IND_CARGA', 'CNPJ_COL', 'IE_COL', 'CPF_COL', 'COD_MUN_COL', 'CNPJ_ENTG',
    'IE_ENTG', 'CPF_ENTG', 'COD_MUN_ENTG',
    ))
rC116 = register('C116', ('COD_MOD', 'NR_SAT', 'CHV_CFE', 'NUM_CFE', 'DT_DOC'))
rC120 = register('C120', (
    'COD_DOC_IMP', 'NUM_DOC_IMP', 'PIS_IMP', 'COFINS_IMP', 'NUM_ACDRAW',
    ))
rC130 = register('C130', (
    'VL_SERV_NT', 'VL_BC_ISSQN', 'VL_ISSQN', 'VL_BC_IRRF', 'VL_IRRF',
    'VL_BC_PREV', 'VL_PREV',
    ))
rC140 = register('C140', (
    'IND_EMIT', 'IND_TIT', 'DESC_TIT', 'NUM_TIT', 'QTD_PARC', 'VL_TIT',
    ))
rC141 = register('C141', ('NUM_PARC', 'DT_VCTO', 'VL_PARC'))
rC160 = register('C160', (
    'COD_PART', 'VEIC_ID', 'QTD_VOL', 'PESO_BRT', 'PESO_LIQ', 'UF_ID',
    ))
rC165 = register('C165', (
    'COD_PART', 'VEIC_ID', 'COD_AUT', 'NR_PASSE', 'HORA', 'TEMPER', 'QTD_VOL',
    'PESO_BRT', 'PESO_LIQ', 'NOM_MOT', 'CPF', 'UF_ID',
    ))
rC170 = register('C170', (
    'NUM_ITEM', 'COD_ITEM', 'DESCR_COMPL', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC',
    'IND_MOV', 'CST_ICMS', 'CFOP', 'COD_NAT', 'VL_BC_ICMS', 'ALIQ_ICMS',
    'VL_ICMS', 'VL_BC_ICMS_ST', 'ALIQ_ST', 'VL_ICMS_ST', 'IND_APUR', 'CST_IPI',
    'COD_ENQ', 'VL_BC_IPI', 'ALIQ_IPI', 'VL_IPI', 'CST_PIS', 'VL_BC_PIS',
    'ALIQ_PIS', 'QUANT_BC_PIS', 'ALIQ_PIS', 'VL_PIS', 'CST_COFINS',
    'VL_BC_COFINS', 'ALIQ_COFINS', 'QUANT_BC_COFINS', 'ALIQ_COFINS',
    'VL_COFINS', 'COD_CTA',
    ))
rC171 = register('C171', ('NUM_TANQUE', 'QTDE'))
rC172 = register('C172', ('VL_BC_ISSQN', 'ALIQ_ISSQN', 'VL_ISSQN'))
rC173 = register('C173', (
    'LOTE_MED', 'QTD_ITEM', 'DT_FAB', 'DT_VAL', 'IND_MED', 'TP_PROD',
    'VL_TAB_MAX',
    ))
rC174 = register('C174', ('IND_ARM', 'NUM_ARM', 'DESCR_COMPL'))
rC175 = register('C175', ('IND_VEIC_OPER', 'CNPJ', 'UF', 'CHASSI_VEIC'))
rC176 = register('C176', (
    'COD_MOD_ULT_E', 'NUM_DOC_ULT_E', 'SER_ULT_E', 'DT_ULT_E',
    'COD_PART_ULT_E', 'QUANT_ULT_E', 'VL_UNIT_ULT_E', 'VL_UNIT_BC_ST',
    ))
rC177 = register('C177', ('COD_SELO_IPI', 'QT_SELO_IPI'))
rC178 = register('C178', ('CL_ENQ', 'VL_UNID', 'QUANT_PAD'))
rC179 = register('C179', (
    'BC_ST_ORIG_DEST', 'ICMS_ST_REP', 'ICMS_ST_COMPL', 'BC_RET', 'ICMS_RET',
    ))
rC190 = register('C190', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_RED_BC', 'VL_IPI', 'COD_OBS',
    ))
rC195 = register('C195', ('COD_OBS', 'TXT_COMPL'))
rC197 = register('C197', (
    'COD_AJ', 'DESCR_COMPL_AJ', 'COD_ITEM', 'VL_BC_ICMS', 'ALIQ_ICMS',
    'VL_ICMS', 'VL_OUTROS',
    ))
rC300 = register('C300', (
    'COD_MOD', 'SER', 'SUB', 'NUM_DOC_INI', 'NUM_DOC_FIN', 'DT_DOC', 'VL_DOC',
    'VL_PIS', 'VL_COFINS', 'COD_CTA',
    ))
rC310 = register('C310', ('NUM_DOC_CANC',))
rC320 = register('C320', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_RED_BC', 'COD_OBS',
    ))
rC321 = register('C321', (
    'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_PIS', 'VL_COFINS',
    ))
rC350 = register('C350', (
    'SER', 'SUB_SER', 'NUM_DOC', 'DT_DOC', 'CNPJ_CPF', 'VL_MERC', 'VL_DOC',
    'VL_DESC', 'VL_PIS', 'VL_COFINS', 'COD_CTA',
    ))
rC370 = register('C370', (
    'NUM_ITEM', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC',
    ))
rC390 = register('C390', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_RED_BC', 'COD_OBS',
    ))
rC400 = register('C400', ('COD_MOD', 'ECF_MOD', 'ECF_FAB', 'ECF_CX'))
rC405 = register('C405', (
    'DT_DOC', 'CRO', 'CRZ', 'NUM_COO_FIN', 'GT_FIN', 'VL_BRT',
    ))
rC410 = register('C410', ('VL_PIS', 'VL_COFINS'))
rC420 = register('C420', (
    'COD_TOT_PAR', 'VLR_ACUM_TOT', 'NR_TOT', 'DESCR_NR_TOT'
    ))
rC425 = register('C425', (
    'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_PIS', 'VL_COFINS'
    ))
rC460 = register('C460', (
    'COD_MOD', 'COD_SIT', 'NUM_DOC', 'DT_DOC', 'VL_DOC', 'VL_PIS', 'VL_COFINS',
    'CPF_CNPJ', 'NOM_ADQ',
    ))
rC470 = register('C470', (
    'COD_ITEM', 'QTD', 'QTD_CANC', 'UNID', 'VL_ITEM', 'CST_ICMS', 'CFOP',
    'ALIQ_ICMS', 'VL_PIS', 'VL_COFINS',
    ))
rC490 = register('C490', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'COD_OBS',
    ))
rC495 = register('C495', (
    'ALIQ_ICMS', 'COD_ITEM', 'QTD', 'QTD_CANC', 'UNID', 'VL_ITEM', 'VL_DESC',
    'VL_CANC', 'VL_ACMO', 'VL_BC_ICMS', 'VL_ICMS', 'VL_ISEN', 'VL_NT',
    'VL_ICMS_ST',
    ))
rC500 = register('C500', (
    'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'SUB',
    'COD_CONS', 'NUM_DOC', 'DT_DOC', 'DT_E_S', 'VL_DOC', 'VL_DESC', 'VL_FORN',
    'VL_SERV_NT', 'VL_TERC', 'VL_DA', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST',
    'VL_ICMS_ST', 'COD_INF', 'VL_PIS', 'VL_COFINS', 'TP_LIGACAO',
    'COD_GRUPO_TENSAO',
    ))
rC510 = register('C510', (
    'NUM_ITEM', 'COD_ITEM', 'COD_CLASS', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC',
    'CST_ICMS', 'CFOP', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST',
    'ALIQ_ST', 'VL_ICMS_ST', 'IND_REC', 'COD_PART', 'VL_PIS', 'VL_COFINS',
    'COD_CTA',
    ))
rC590 = register('C590', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_RED_BC', 'COD_OBS',
    ))
rC600 = register('C600', (
    'COD_MOD', 'COD_MUN', 'SER', 'SUB', 'COD_CONS', 'QTD_CONS', 'QTD_CANC',
    'DT_DOC', 'VL_DOC', 'VL_DESC', 'CONS', 'VL_FORN', 'VL_SERV_NT', 'VL_TERC',
    'VL_DA', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_PIS',
    'VL_COFINS',
    ))
rC601 = register('C601', ('NUM_DOC_CANC',))
rC610 = register('C610', (
    'COD_CLASS', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'CST_ICMS',
    'CFOP', 'ALIQ_ICMS', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST',
    'VL_ICMS_ST', 'VL_PIS', 'VL_COFINS', 'COD_CTA',
    ))
rC690 = register('C690', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_RED_BC', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'COD_OBS',
    ))
rC700 = register('C700', (
    'COD_MOD', 'SER', 'NRO_ORD_INI', 'NRO_ORD_FIN', 'DT_DOC_INI', 'DT_DOC_FIN',
    'NOM_MEST', 'CHV_COD_DIG',
    ))
rC790 = register('C790', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_RED_BC', 'COD_OBS',
    ))
rC791 = register('C791', ('UF', 'VL_BC_ICMS_ST', 'VL_ICMS_ST'))
rC800 = register('C800', (
    'COD_MOD', 'COD_SIT', 'NUM_CFE', 'DT_DOC', 'VL_CFE', 'VL_PIS', 'VL_COFINS',
    'CNPJ_CPF', 'NR_SAT', 'CHV_CFE', 'VL_DESC', 'VL_MERC', 'VL_OUT_DA',
    'VL_ICMS', 'VL_PIS_ST', 'VL_COFINS_ST',
    ))
rC850 = register('C850', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'COD_OBS',
    ))
rC860 = register('C860', ('COD_MOD', 'NR_SAT', 'DT_DOC', 'DOC_INI', 'DOC_FIM'))
rC890 = register('C890', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'COD_OBS',
    ))
rC990 = register('C990', ('QTD_LIN_C',))

# Block D
rD001 = register('D001', ('IND_MOV',))
rD100 = register('D100', (
    'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'SUB',
    'NUM_DOC', 'CHV_CTE', 'DT_DOC', 'DT_A_P', 'TP_CT-e', 'CHV_CTE_REF',
    'VL_DOC', 'VL_DESC', 'IND_FRT', 'VL_SERV', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_NT', 'COD_INF', 'COD_CTA',
    ))
rD110 = register('D110', ('NUM_ITEM', 'COD_ITEM', 'VL_SERV', 'VL_OUT'))
rD120 = register('D120', ('COD_MUN_ORIG', 'COD_MUN_DEST', 'VEIC_ID', 'UF_ID'))
rD130 = register('D130', (
    'COD_PART_CONSG', 'COD_PART_RED', 'IND_FRT_RED', 'COD_MUN_ORIG',
    'COD_MUN_DEST', 'VEIC_ID', 'VL_LIQ_FRT', 'VL_SEC_CAT', 'VL_DESP',
    'VL_PEDG', 'VL_OUT', 'VL_FRT', 'UF_ID',
    ))
rD140 = register('D140', (
    'COD_PART_CONSG', 'COD_MUN_ORIG', 'COD_MUN_DEST', 'IND_VEIC', 'VEIC_ID',
    'IND_NAV', 'VIAGEM', 'VL_FRT_LIQ', 'VL_DESP_PORT', 'VL_DESP_CAR_DESC',
    'VL_OUT', 'VL_FRT_BRT', 'VL_FRT_MM',
    ))
rD150 = register('D150', (
    'COD_MUN_ORIG', 'COD_MUN_DEST', 'VEIC_ID', 'VIAGEM', 'IND_TFA',
    'VL_PESO_TX', 'VL_TX_TERR', 'VL_TX_RED', 'VL_OUT', 'VL_TX_ADV',
    ))
rD160 = register('D160', (
    'DESPACHO', 'CNPJ_CPF_REM', 'IE_REM', 'COD_MUN_ORI', 'CNPJ_CPF_DEST',
    'IE_DEST', 'COD_MUN_DEST',
    ))
rD161 = register('D161', (
    'IND_CARGA', 'CNPJ_CPF_COL', 'IE_COL', 'COD_MUN_COL', 'CNPJ_CPF_ENTG',
    'IE_ENTG', 'COD_MUN_ENTG',
    ))
rD162 = register('D162', (
    'COD_MOD', 'SER', 'NUM_DOC', 'DT_DOC', 'VL_DOC', 'VL_MERC', 'QTD_VOL',
    'PESO_BRT', 'PESO_LIQ',
    ))
rD170 = register('D170', (
    'COD_PART_CONSG', 'COD_PART_RED', 'COD_MUN_ORIG', 'COD_MUN_DEST', 'OTM',
    'IND_NAT_FRT', 'VL_LIQ_FRT', 'VL_GRIS', 'VL_PDG', 'VL_OUT', 'VL_FRT',
    'VEIC_ID', 'UF_ID',
    ))
rD180 = register('D180', (
    'NUM_SEQ', 'IND_EMIT', 'CNPJ_CPF_EMIT', 'UF_EMIT', 'IE_EMIT',
    'COD_MUN_ORIG', 'CNPJ_CPF_TOM', 'UF_TOM', 'IE_TOM', 'COD_MUN_DEST',
    'COD_MOD', 'SER', 'SUB', 'NUM_DOC', 'DT_DOC', 'VL_DOC',
    ))
rD190 = register('D190', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_RED_BC', 'COD_OBS',
    ))
rD195 = register('D195', ('COD_OBS', 'TXT_COMPL'))
rD197 = register('D197', (
    'COD_AJ', 'DESCR_COMPL_AJ', 'COD_ITEM', 'VL_BC_ICMS', 'ALIQ_ICMS',
    'VL_ICMS', 'VL_OUTROS',
    ))
rD300 = register('D300', (
    'COD_MOD', 'SER', 'SUB', 'NUM_DOC_INI', 'NUM_DOC_FIN', 'CST_ICMS', 'CFOP',
    'ALIQ_ICMS', 'DT_DOC', 'VL_OPR', 'VL_DESC', 'VL_SERV', 'VL_SEG',
    'VL_OUT_DESP', 'VL_BC_ICMS', 'VL_ICMS', 'VL_RED_BC', 'COD_OBS', 'COD_CTA',
    ))
rD301 = register('D301', ('NUM_DOC_CANC',))
rD310 = register('D310', ('COD_MUN_ORIG', 'VL_SERV', 'VL_BC_ICMS', 'VL_ICMS'))
rD350 = register('D350', ('COD_MOD', 'ECF_MOD', 'ECF_FAB', 'ECF_CX'))
rD355 = register('D355', (
    'DT_DOC', 'CRO', 'CRZ', 'NUM_COO_FIN', 'GT_FIN', 'VL_BRT',
    ))
rD360 = register('D360', ('VL_PIS', 'VL_COFINS'))
rD365 = register('D365', (
    'COD_TOT_PAR', 'VLR_ACUM_TOT', 'NR_TOT', 'DESCR_NR_TOT',
    ))
rD370 = register('D370', (
    'COD_MUN_ORIG', 'VL_SERV', 'QTD_BILH', 'VL_BC_ICMS', 'VL_ICMS',
    ))
rD390 = register('D390', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ISSQN', 'ALIQ_ISSQN',
    'VL_ISSQN', 'VL_BC_ICMS', 'VL_ICMS', 'COD_OBS',
    ))
rD400 = register('D400', (
    'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'SUB', 'NUM_DOC', 'DT_DOC',
    'VL_DOC', 'VL_DESC', 'VL_SERV', 'VL_BC_ICMS', 'VL_ICMS', 'VL_PIS',
    'VL_COFINS', 'COD_CTA',
    ))
rD410 = register('D410', (
    'COD_MOD', 'SER', 'SUB', 'NUM_DOC_INI', 'NUM_DOC_FIN', 'DT_DOC',
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_DESC', 'VL_SERV',
    'VL_BC_ICMS', 'VL_ICMS',
    ))
rD411 = register('D411', ('NUM_DOC_CANC',))
rD420 = register('D420', ('COD_MUN_ORIG', 'VL_SERV', 'VL_BC_ICMS', 'VL_ICMS'))
rD500 = register('D500', (
    'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'SUB',
    'NUM_DOC', 'DT_DOC', 'DT_A_P', 'VL_DOC', 'VL_DESC', 'VL_SERV',
    'VL_SERV_NT', 'VL_TERC', 'VL_DA', 'VL_BC_ICMS', 'VL_ICMS', 'COD_INF',
    'VL_PIS', 'VL_COFINS', 'COD_CTA', 'TP_ASSINANTE',
    ))
rD510 = register('D510', (
    'NUM_ITEM', 'COD_ITEM', 'COD_CLASS', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC',
    'CST_ICMS', 'CFOP', 'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_BC_ICMS_UF',
    'VL_ICMS_UF', 'IND_REC', 'COD_PART', 'VL_PIS', 'VL_COFINS', 'COD_CTA',
    ))
rD530 = register('D530', (
    'IND_SERV', 'DT_INI_SERV', 'DT_FIN_SERV', 'PER_FISCAL', 'COD_AREA',
    'TERMINAL',
    ))
rD590 = register('D590', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_BC_ICMS_UF', 'VL_ICMS_UF', 'VL_RED_BC', 'COD_OBS',
    ))
rD600 = register('D600', (
    'COD_MOD', 'COD_MUN', 'SER', 'SUB', 'COD_CONS', 'QTD_CONS', 'DT_DOC',
    'VL_DOC', 'VL_DESC', 'VL_SERV', 'VL_SERV_NT', 'VL_TERC', 'VL_DA',
    'VL_BC_ICMS', 'VL_ICMS', 'VL_PIS', 'VL_COFINS',
    ))
rD610 = register('D610', (
    'COD_CLASS', 'COD_ITEM', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'CST_ICMS',
    'CFOP', 'ALIQ_ICMS', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_UF',
    'VL_ICMS_UF', 'VL_RED_BC', 'VL_PIS', 'VL_COFINS', 'COD_CTA',
    ))
rD690 = register('D690', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_BC_ICMS_UF', 'VL_ICMS_UF', 'VL_RED_BC', 'COD_OBS',
    ))
rD695 = register('D695', (
    'COD_MOD', 'SER', 'NRO_ORD_INI', 'NRO_ORD_FIN', 'DT_DOC_INI', 'DT_DOC_FIN',
    'NOM_MEST', 'CHV_COD_DIG',
    ))
rD696 = register('D696', (
    'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS',
    'VL_BC_ICMS_UF', 'VL_ICMS_UF', 'VL_RED_BC', 'COD_OBS',
    ))
rD697 = register('D697', ('UF', 'VL_BC_ICMS', 'VL_ICMS'))
rD990 = register('D990', ('QTD_LIN_D',))













