# -*- coding: utf-8 -*-
"""OpenERP Model adding a 'Refresh Stored values' button to all model.

"""


from osv import osv, fields


class AddModelRefreshButton(osv.osv):
    """Adds a button in report view to create a print action

    The print action is created in the report target's model view.

    """

    _name = 'ir.model'
    _inherit = 'ir.model'

    def refresh_stored(self, cr, uid, ids, context):
        """Adds the print action in the report's model view"""
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


