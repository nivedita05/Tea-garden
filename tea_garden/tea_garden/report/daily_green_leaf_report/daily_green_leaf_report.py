# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils

def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	#frappe.throw(report_entries)
	data = []
	
	

	for sle in report_entries:
		data.append([sle.section_name, sle.section_area, sle.area, sle.prune_type,sle.bush_type])
			
	return columns, data


	





def get_report_entries(filters):

	[["Section_name"=>"A","section_area"=>10.10,"area"=>12.10,"prune_type"=>"DP","bush_type"=>'M'],["Section_name"=>"A","section_area"=>10.10,"area"=>12.10,"prune_type"=>"DP","bush_type"=>'M']]
	#return frappe.db.sql("""select date,section_name, section_area, area, prune_type, bush_type
	#	from `tabDaily Green Leaf in details` where estate_name = %(estate_name)s and date= %(date)s {sle_conditions}""".format(sle_conditions=get_sle_conditions(filters)), filters, as_dict=1)



def get_sle_conditions(filters):
	conditions = []
	return "and {}".format(" and ".join(conditions)) if conditions else ""



def get_columns():
		
		columns = [{
			"fieldname": "section_name",
			"label": _("Section"),
			"fieldtype": "Link",
			"options": "daily_green_leaf_in_details",
			"width": 120
		}]
		
		columns.append({
				"fieldname": "original_area",
				"label": _("Area"),
				"fieldtype": "Link",
				"options": "daily_green_leaf_in_details",
				"width": 70
	    })

		columns.append({
			"fieldname": "area",
			"label": _("Area Plucked"),
			"fieldtype": "Link",
			"options": "daily_green_leaf_in_details",
			"width":100

			
		})


		columns.append({
			"fieldname": "prune_type",
			"label": _("Prune Type"),
			"fieldtype":"Link",
			"options": "daily_green_leaf_in_details",
			"width":133
		})


		columns.append({
			"fieldname": "bush_type",
			"label": _("Bush Type"),
			"fieldtype": "Link",
			"options": "daily_green_leaf_in_details",
			"width":135
		})


		
		return columns

	
	
   


