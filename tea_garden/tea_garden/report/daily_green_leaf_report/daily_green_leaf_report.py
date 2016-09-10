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
		data.append([sle.section_name, sle.section_area, sle.area,sle.prune_type,sle.bush_type])
			
	return columns, data


	





def get_report_entries(filters):
	return frappe.db.sql("""select date,section_name, section_area, area, prune_type, bush_type from `tabDaily Green Leaf in details` where estate_name = %s and date= %s""",(filters.estate_name,filters.date),as_dict=1)



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
				"fieldtype": "Float",
				"options": "daily_green_leaf_in_details",
				"width": 70
	    })

		columns.append({
			"fieldname": "area",
			"label": _("Area Plucked"),
			"fieldtype": "Float",
			"options": "daily_green_leaf_in_details",
			"width": 70

			
		})


		columns.append({
			"fieldname": "prune_type",
			"label": _("Prune Type"),
			"fieldtype":"Link",
			"options":"daily_green_leaf_in_details",
			"width":133
		})


		columns.append({
			"fieldname": "bush_type",
			"label": _("Bush Type"),
			"fieldtype": "Link",
			"options":"daily_green_leaf_in_details",
			"width":135
		})


		
		return columns

	
	
   


