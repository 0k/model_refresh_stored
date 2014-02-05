# -*- coding: utf-8 -*-
"""OpenERP Model adding a 'Refresh Stored values' button to all model.

"""


from osv import osv, fields
from openerp import SUPERUSER_ID


class AddModelRefreshButton(osv.osv):
    """Adds a button in model view to refresh stored values of instances

    """

    _name = 'ir.model'
    _inherit = 'ir.model'

    def refresh_stored(self, cr, uid, ids, context):
        todo = []
        for obj_model in self.browse(cr, uid, ids, context=context):
            model = self.pool.get(obj_model.model)
            for k, f in model._columns.iteritems():
                if not isinstance(f, fields.function) or f.store is False:
                    continue
                order = 10
                if f.store is not True: # i.e. if f.store is a dict
                    order = f.store[f.store.keys()[0]][2]
                todo.append((order, model._update_store, (f, k)))
        todo.sort()
        for t in todo:
            t[1](cr, *t[2])
        return True

    _columns = {
    }

    _defaults = {}


def _update_store_by_ids(self, cr, f, k, ids_lst):
    report = ""
    ss = self._columns[k]._symbol_set
    update_query = 'UPDATE "%s" SET "%s"=%s WHERE id=%%s' % (self._table, k, ss[0])
    while ids_lst:
        iids = ids_lst[:40]
        ids_lst = ids_lst[40:]
        res = f.get(cr, self, iids, k, SUPERUSER_ID, {})
        for key, val in res.items():
            if f._multi:
                val = val[k]
            # if val is a many2one, just write the ID
            if type(val) == tuple:
                val = val[0]
            if val is not False:
                report += "%s:%s forced refresh of stored value for function '%s'\n" % (self._name, key, k)
                cr.execute(update_query, (ss[1](val), key))
    return report


def update_store(self, cr, uid, ids, context=None):
    todo = []
    for k, f in self._columns.iteritems():
        if not isinstance(f, fields.function) or f.store is False:
            continue
        order = 10
        if f.store is not True: # i.e. if f.store is a dict
            order = f.store[f.store.keys()[0]][2]
        todo.append((order, self._update_store_by_ids, (f, k, ids)))
    todo.sort()
    report = ""
    for t in todo:
        report += t[1](cr, *t[2])
    return report


osv.osv._update_store_by_ids = _update_store_by_ids
osv.osv.update_store = update_store
