# -*- coding: utf-8 -*-
# This file is part of atm_company Tryton Module.  The 
# COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.

from trytond.pool import Pool
from .company import *


def register():
    Pool.register(
        Company,
        module='atm_company', type_='model')
