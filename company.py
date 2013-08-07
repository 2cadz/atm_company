# -*- coding: utf-8 -*-
# This file is part of atm_company Tryton Module.  The 
# COPYRIGHT file at the top level of this repository contains the
# full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Company']
__metaclass__ = PoolMeta


class Company(ModelSQL, ModelView):
    'Company'
    __name__ = 'company.company'
    
    header = fields.Text('Header', translate=True)
    footer = fields.Text('Footer', translate=True)
