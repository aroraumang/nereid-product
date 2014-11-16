# -*- coding: utf-8 -*-
"""
    product.py

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import PoolMeta
from nereid import render_template, route

__metaclass__ = PoolMeta

__all__ = ['Product']

class Product:
    __name__ = 'product.product'

    @classmethod
    @route('/products', methods=['GET'])
    def render_list(cls):
        products = cls.search([])

        return render_template(
            'product-list.jinja',
            products=products
        )

    @route('/product/<int:active_id>')
    def render(self):
        return render_template(
            'product.jinja',
            product=self
        )
