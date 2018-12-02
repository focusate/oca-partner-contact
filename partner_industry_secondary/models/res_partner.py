# Copyright 2015 Antiun Ingenieria S.L. - Javier Iniesta
# Copyright 2016 Tecnativa S.L. - Vicent Cubells
# Copyright 2018 Eficent Business and IT Consulting Services, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, exceptions, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    industry_id = fields.Many2one(string='Main Industry')

    secondary_industry_ids = fields.Many2many(
        comodel_name='res.partner.industry', string="Secondary Industries",
        domain="[('id', '!=', industry_id)]")

    @api.constrains('industry_id', 'secondary_industry_ids')
    def _check_industries(self):
        if self.industry_id in self.secondary_industry_ids:
            raise exceptions.UserError(
                _('The main industry must be different '
                  'from the secondary industries.'))