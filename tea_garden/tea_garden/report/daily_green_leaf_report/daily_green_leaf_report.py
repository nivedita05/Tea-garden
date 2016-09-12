from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime
#import timedelta
#import json

def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []
	
	

	for sle in report_entries:
		todate_area    = get_todate_area_pluck(sle.section_name,filters)
		todate_pluckers=get_todate_pluckers(sle.section_name,filters)
		todate_leaf_count=get_todate_green_leaf(sle.section_name,filters)
		todate_pluckers_hector=get_todate_pluckers_per_hector(sle.section_name,filters)
		todate_green_leaf_hector=get_todate_green_leaf_per_hector(sle.section_name,filters)
		todate_plucking_avg=get_plucking_average(sle.section_name,filters)
		todate_round=get_round(sle.section_name,filters)
		todate_yeild_hector=get_todate_yield_per_hector(sle.section_name,filters)
		section_detail = get_section_details(sle.section_name,filters)
		section_detail1=get_section_details1(sle.section_name,filters)
		budget_details=get_budget(sle.section_name,filters)
		pecent_of_crop=get_percent_of_year_croped(sle.section_name,filters)
		date=get_starting_date(sle.section_name,filters)

		data.append([sle.section_name,section_detail,section_detail1,todate_area,todate_pluckers,todate_leaf_count,todate_pluckers_hector,todate_green_leaf_hector,todate_plucking_avg, todate_round,todate_yeild_hector,budget_details,pecent_of_crop,date])
			
	return columns, data


	


# , sle.section_area, sle.area, sle.prune_type, sle.bush_type


def get_report_entries(filters):
	return frappe.db.sql("""select distinct section_name from `tabDaily Green Leaf in details` where estate_name = %s and prune_type=%s and bush_type=%s and division_name=%s and date BETWEEN %s AND %s ORDER BY date DESC""",(filters.estate_name,filters.prune_type,filters.bush_type,filters.division_name,'2016-01-01', filters.date),as_dict=1)

def get_todate_area_pluck(section_name,filters):
	return frappe.db.sql("""select sum(area) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))


def get_todate_pluckers(section_name,filters):
	return frappe.db.sql("""select sum(pluckers) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))


def get_todate_green_leaf(section_name,filters):
	return frappe.db.sql("""select sum(leaf_count) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))


def get_todate_pluckers_per_hector(section_name,filters):
	return frappe.db.sql("""select sum(pluckers)/sum(area) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))

def get_todate_green_leaf_per_hector(section_name,filters):
	return frappe.db.sql("""select sum(leaf_count)/sum(area) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))


def get_plucking_average(section_name,filters):
	return frappe.db.sql("""select round(sum(leaf_count)/sum(pluckers),2) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))

def get_round(section_name,filters):
	return frappe.db.sql("""select sum(area)/section_area from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))



def get_todate_yield_per_hector(section_name,filters):
	return frappe.db.sql("""select round((sum(leaf_count)*0.225)/section_area,2) from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_name, '2016-01-01',filters.date))


def get_section_details(section_name,filters):
	return frappe.db.sql("""select section_area from `tabDaily Green Leaf in details` where section_name = %s and date BETWEEN %s AND %s  ORDER BY Date DESC""",(section_name,'2016-01-01',filters.date)) 


def get_section_details1(section_name,filters):
	return frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_name = %s and date=%s""",(section_name,filters.date)) 



def get_budget(section_name,filters):
	return frappe.db.sql("""select projected_yield*0.225 from `tabPruning Cycle` where section_name = %s """,(section_name)) 


def get_percent_of_year_croped(section_name,filters):
	return frappe.db.sql("""select (sum(t.leaf_count)/sum(t.pluckers))/(p.projected_yield*0.225) from `tabDaily Green Leaf in details` t INNER JOIN `tabPruning Cycle` p  ON t.section_name=p.section_name where t.section_name = %s""",(section_name)) 



def get_starting_date(section_name,filters):
	todays_date=datetime.today().strftime("%Y-%m-%d")
	day1=datetime.strptime(todays_date,'%Y-%m-%d')
	
	starting_date=frappe.db.sql("""select min(date) from `tabDaily Green Leaf in details` where section_name=%s and date BETWEEN %s AND %s""",(section_name,'2016-01-01',filters.date))	
	day2=datetime.strptime(starting_date[0][0],'%Y-%m-%d')

	diff=abs(day1.date()-day2.date()).days
	r=get_round(section_name,filters)
	r_per_days=diff/r[0][0]
	return r_per_days
	#date_diff=todays_date-starting_date
	

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
				"width": 75
	    })

		columns.append({
			"fieldname": "area",
			"label": _("Area Plucked"),
			"fieldtype": "Float",
			"options": "daily_green_leaf_in_details",
			"width": 75

			
		})


		columns.append({
			"label": _("Area Plucked To Date"),
			"fieldtype": "Float",
			"width":75
		})

		columns.append({
			"label": _("Pluckers To Date"),
			"fieldtype": "Int",
			"width":75
		})

		columns.append({
			"label": _("Green leaf To Date"),
			"fieldtype": "Float",
			"width":90
		})

		columns.append({
			"label": _("Pluckers/hector"),
			"fieldtype": "Int",
			"width":72
		})

		columns.append({
			"label": _("Green Leaf/hector"),
			"fieldtype": "Int",
			"width":71
		})

		columns.append({
			"label": _("Plucking Avegare"),
			"fieldtype": "round(Float,2)",
			"width":71
		})

		columns.append({
			"label": _("Round"),
			"fieldtype": "Int",
			"width":71
		})

		columns.append({
			"label": _("Yield/Hector"),
			"fieldtype": "round(Float,2)",
			"width":71
		})

		columns.append({
			"label": _("Budget"),
			"fieldtype": "Int",
			"width":71
		})

		columns.append({
			"label": _("Percent Of Yr Crop"),
			"fieldtype": "Float",
			"width":70
		})

		columns.append({
			"label": _("R/Days"),
			"fieldtype": "Int",
			"width":70
		})

		
		return columns

	