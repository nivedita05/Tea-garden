# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe and Contributors
# See license.txt
from __future__ import unicode_literals


import frappe
import unittest
import frappe.defaults



import json
from frappe.utils import cstr, flt
from frappe import msgprint, _
from frappe.model.mapper import get_mapped_doc


from frappe import _
from frappe.model.naming import make_autoname
from frappe.model.document import Document
from frappe.test_runner import make_test_records
from tea_garden.tea_garden.doctype.daily_green_leaf import daily_green_leaf
from daily_green_leaf import DailyGreenLeaf


test_records = frappe.get_test_records('Daily Green Leaf')

class TestDailyGreenLeaf(unittest.TestCase):

	def test_estate_name_exist(self):
		estate = frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-08')
		self.assertNotEqual('estate_name', 'Ghatia Tea Estate')
		
       
	def test_estate_name(self):
		estate = frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-08')
		self.assertTrue('estate_name' in estate.as_dict())



	def test_bush_name_exist_or_not(self):
		bush = frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-08')
		self.assertFalse('bush_types' in bush.as_dict())

	def test_bush_name(self):
		bush = frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-08')
		self.assertNotEqual('bush_type', 'UP')
	def test_bush(self):
		bush 	  = 	frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-08')
		th = DailyGreenLeaf(Document)
		self.assertRaises(frappe.ValidationError,th.get_bush_name) 
	