=====================
Refresh Stored Values
=====================

Provides a simple button at the bottom of the form view of model objects which
refresh all stored values for this model.

This module is really small and can be used as a good way to learn OpenERP
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


Installation
------------

Please make sure to launch:

  ./autogen.sh

prior to installing this module to generate the version and the changelog.

Then you can install it as any other OpenERP module.


Usage
-----

1. Ensure that you are are an OpenERP administrator with Extended Interface.
2. Then go to the "Settings" Tab,
3. And in the left menu, follow Technical / Database Structure / Models
4. On any model (previously created or newly created) you'll find a new button
   on the top called "Refresh Stored Values".  Upon click, all stored function
   will get recomputed.
