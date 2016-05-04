# -*- coding: utf-8 -*-
"""
    __init__.py

"""
from trytond.pool import Pool

from party import Party, PartyMergeView, PartyMerge


def register():
    Pool.register(
        Party,
        PartyMergeView,
        module='party_merge', type_='model'
    )
    Pool.register(
        PartyMerge,
        module='party_merge', type_='wizard'
    )
