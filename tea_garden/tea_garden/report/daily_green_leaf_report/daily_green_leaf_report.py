# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from tea_garden.tea_garden.doctype import daily_green_leaf_in_details

def execute(self):
	self.get_value()


def get_value(self):
	bush=frappe.db.sql(""" select bush_type from `tabDaily Green Leaf in details` where date=%s and estate_name=%s""",(self.date,self.estate_name))
	return bush