# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
import datetime
from datetime import datetime
import requests
import simplejson

import logging
_logger = logging.getLogger(__name__)

class CoronaVirus(models.Model):
	_name = 'corona.virus'

	name = fields.Char(string='Name', default='New', readonly=True)
	date = fields.Date(string='Date', default=lambda self:time.strftime("%Y-%m-%d"))
	line_ids = fields.One2many('corona.virus.lines', 'corona_virus_id', string='Lines')


	@api.model
	def create(self, vals):
		if not vals.get('name', False) or vals['name'] == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('corona.virus') or 'Error Number!!!'
		return super(CoronaVirus, self).create(vals)

	@api.multi
	def generate_corona_virus(self):
		url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json'
		r = requests.get(f'{url}')
		res = simplejson.loads(r.text)

		cr = self.env.cr
		sql = "delete from corona_virus_lines where corona_virus_id=%s"
		cr.execute(sql, (self.id,))

		_logger.info(f"=============== [ {res} ] ===============")

		for rec in res['features']:
			self.env['corona.virus.lines'].create({
				'object_id'			: rec['attributes']['OBJECTID'],
				'province_state'	: rec['attributes']['Province_State'],
				'country_region'	: rec['attributes']['Country_Region'],
				'confirmed'			: rec['attributes']['Confirmed'],
				'recovered'			: rec['attributes']['Recovered'],
				'deaths'			: rec['attributes']['Deaths'],
				'corona_virus_id'	: self.id,
			})



class CoronaVirusLines(models.Model):
    _name = 'corona.virus.lines'

    object_id = fields.Integer(string='OBJECTID', readonly=True)
    province_state = fields.Char(string='Province State')
    country_region = fields.Char(string='Country Region')
    confirmed = fields.Char(string='Confirmed')
    recovered = fields.Char(string='Recovered')
    deaths = fields.Char(string='Deaths')
    corona_virus_id = fields.Many2one('corona.virus',string='Corona Virus')
