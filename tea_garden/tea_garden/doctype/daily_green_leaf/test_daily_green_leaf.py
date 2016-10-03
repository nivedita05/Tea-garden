# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe and Contributors
# See license.txt
#from __future__ import unicode_literals

import frappe
import unittest
import frappe.defaults
from frappe.test_runner import make_test_records

test_records = frappe.get_test_records('Daily Green Leaf')

class TestDailyGreenLeaf(unittest.TestCase):

	def test_estate_name_exist(self):
		estate = frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-08')
		self.assertNotEqual('estate_name', 'Ghatia Tea Estate')
		
       
	def test_estate_name(self):
		estate = frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-10')
		self.assertTrue('estate_name' in estate.as_dict())


	def test_area(self):
		estate = frappe.get_doc('Daily Green Leaf', 'Ghatia Tea Estate:2016-10-15')
		val_area=self.validtae_area()
		self.assertRaises(ValidationError, val_area)
