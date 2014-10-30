=====================
Refresh Stored Values
=====================

Provides a simple button at the bottom of the form view of model objects which
refresh all stored values for this model.

This module is really small and can be used as a good way to learn OpenERP/Odoo
module creation.

Besides, it could be handy to have this in hand while developping other modules.


Todo
----

- add the button in the one2many view of each fields of a model to
  offer a "per field" refresh.


Requirements
------------

Was tested successfully with:

 - OpenERP 7.0
 - OpenERP/Odoo 8.0


Installation
------------

Please make sure to launch:

  ./autogen.sh

prior to installing this module to generate the version and the changelog.

Then you can install it as any other OpenERP/Odoo module.


Usage
-----

GUI
"""

1. Ensure that you are are an OpenERP administrator with Extended Interface.
2. Then go to the "Settings" Tab,
3. And in the left menu, follow Technical / Database Structure / Models
4. On any model (previously created or newly created) you'll find a new button
   on the top called "Refresh Stored Values".  Upon click, all stored function
   will get recomputed.

Command line
""""""""""""

A command line is provided, but you should be warned that it required
``docopt`` and ``ooop``. You can install them both thanks to:

    pip install docopt ooop

The command line allows you to query a distant openerp server and force
recalculating stored function field on a per record basis. This can provide
usefull if you don't want to recalculate all records.

You can::

    ./restore --help

To get a full help options. Here's an example of usage::

    $ OE_USER=admin OE_PASSWORD=dev OE_DB=test_restore bin/restore project.task --domain "[('name', '=', 't1')]"
    project.task:1 forced refresh of stored value for function 'active'
    project.task:1 forced refresh of stored value for function 'effective_hours'
    project.task:1 forced refresh of stored value for function 'total_hours'
    project.task:1 forced refresh of stored value for function 'delay_hours'
    project.task:1 forced refresh of stored value for function 'progress'
    $

A few handy shortcuts are provided as documented::

    $ bin/restore --help
    Re-calculate stored values for given objects.

    Usage:
        restore (-h | --help)
        restore MODEL [--after DATE | --id IDS] [--limit MAX] [--domain DOMAIN]

    Options:
        -h, --help           Show this screen
        --after DATE         Filters model by created or write date after given DATE
        --id IDS             Filters model to given ids
        --domain DOMAIN      Ignore existing domain and use DOMAIN instead
