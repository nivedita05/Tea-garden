from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []
	
	

	for sle in report_entries:
		todate_area    = get_todate_area_pluck(sle.section_name,filters)
		section_detail = get_section_details(sle.section_name,filters)
		data.append([sle.section_name,section_detail[0][0],section_detail[0][1],todate_area])
			
	return columns, data


	


# , sle.section_area, sle.area, sle.prune_type, sle.bush_type


def get_report_entries(filters):
	return frappe.db.sql("""select distinct section_name from `tabDaily Green Leaf in details` where estate_name = %s and prune_type=%s and bush_type=%s and division_name=%s and date BETWEEN %s AND %s ORDER BY date DESC""",(filters.estate_name,filters.prune_type,filters.bush_type,filters.division_name,'2016-01-01', filters.date),as_dict=1)

def get_todate_area_pluck(section_name,filters):
	return frappe.db.sql("""select sum(area) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))

def get_section_details(section_name,filters):
	return frappe.db.sql("""select section_area,area from `tabDaily Green Leaf in details` where section_name = %s ORDER BY date DESC LIMIT 1""",(section_name)) 

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
			"label": _("To Date"),
			"fieldtype": "Float",
			"width":135
		})
		
		return columns

	