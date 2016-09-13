# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest
import frappe.defaults
from frappe.test_runner import make_test_records

test_records = frappe.get_test_records('Daily Green Leaf')

class TestDailyGreenLeaf(unittest.TestCase):
	
	def test_estate_name(self):
		dgl = frappe.get_doc('Daily Green Leaf', '_Test dgl code')
		#dgl = create_daily_green_leaf(do_not_submit=True)
		#dgl.submit()
		self.assertTrue('dgl_code' in dgl.as_dict())
		self.assertEqual(dgl.estate_name, "_Test Estate_1")
		#dgl = create_daily_green_leaf(section_name="_Test Section name", is_subcontracted="Yes")
		#self.assertEquals(len(dgl.get("leaf_details")), 2)
        # Test if test supplier field record is 'Greece'
        #self.assertEqual(supplier.country, "Greece")

        # Test update Supplier instance country value
        #supplier = frappe.get_doc('Supplier', '_Test Supplier')
        #supplier.country = 'Greece'
        #supplier.save()
		#self.assertEqual(supplier.country, "Greece")

def create_daily_green_leaf(**args):
	dgl = frappe.new_doc("Daily Green Leaf")
	args = frappe._dict(args)
	if dgl.date:
		dgl.date = args.date

	dgl.estate_name = args.estate_name or "_Test Estate_1"
	dgl.dgl_code = args.dgl_code or "_Test dgl code"

	dgl.append("leaf_detais", {
		"section_name": args.section or args.section_name or "SG 6/8 A",
		"area": args.area or 7,
		"section_area": args.section_area or 10,
		"leaf_count": args.leaf_count or 15000,
		"pluckers": args.pluckers or 25,
		"estate_name": args.estate_name or "_Test Estate_1",
		"division_name": args.division_name or "Krishna",
		"prune_type": args.prune_type or "LP",
		"bush_type": args.bush_type or "Mature",
		"today_budget": dgl.calculate_today_budget() or 26.67
	})
	if not args.do_not_save:
		dgl.insert()
		if not args.do_not_submit:
			dgl.submit()

	return dgl		