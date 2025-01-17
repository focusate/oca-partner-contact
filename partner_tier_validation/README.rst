.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=======================
Partner Tier Validation
=======================

This module extends the functionality of Partner to support a tier
validation process.

Installation
============

This module depends on ``base_tier_validation``. You can find it at
`OCA/server-ux <https://github.com/OCA/server-ux>`_


Configuration
=============

To configure this module, you need to:

#. Go to *Settings > Technical > Tier Validations > Tier Definition*.
#. Create as many tiers as you want for Contact  model.
#. Example:
        Definition	Formula			
        Tier Definition Expression	
        # Available locals:
        #  - rec: current record

        [rec.state == New]

Usage
=====

To use this module, you need to:

#. Create a Contact  triggering at least one "Tier Definition".
#. Click on *Request Validation* button.
#. Under the tab *Reviews* have a look to pending reviews and their statuses.
#. Validator has to update Is Customer or Is Supplier or Both for this Contact to be usable on SO/PO.

Additional features:

* You can filter the Invoices requesting your review through the filter *Needs my
  Review*.
* User with rights to confirm the Vendor Bill (validate all tiers that would
  be generated) can directly do the operation, this is, there is no need for
  her/him to request a validation.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/142/11.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/sale-workflow/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Antonio Yamuta <ayamuta@opensourceintegrators.com>

Do not contact contributors directly about support or help with technical issues.

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
