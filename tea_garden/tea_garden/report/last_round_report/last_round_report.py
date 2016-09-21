# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime,timedelta
#import timedelta
#import json

def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []
	
	

	for sle in report_entries:

		
		todate_round=get_round(sle.section_id,filters)
		section_detail = get_section_details(sle.section_id,filters)
		
		to_date=get_to_date(sle.section_id,filters)
		from_date=get_from_date(sle.section_id,filters)
		act=get_actual_to_date_green_leaf(sle.section_id,filters)
		bud=get_to_date_budget(sle.section_id,filters)
		perc=get_plus_minus_budget(sle.section_id,filters)
		done_or_not_done=find_round(sle.section_id,filters)
		data.append([sle.division_name,sle.section_id,sle.section_name,section_detail,todate_round,from_date,to_date,act,bud,perc,done_or_not_done])
		
	return columns, data


	


# , sle.section_area, sle.area, sle.prune_type, sle.bush_type


def get_report_entries(filters):
	return frappe.db.sql("""select distinct section_id,section_name,division_name from `tabDaily Green Leaf in details` where estate_name = %s and prune_type=%s and bush_type=%s and date BETWEEN %s AND %s ORDER BY section_id ASC""",(filters.estate_name,filters.prune_type,filters.bush_type,'2016-01-01', filters.date),as_dict=1)

def get_section_details(section_id,filters):
	return frappe.db.sql("""select min(section_area) from `tabDaily Green Leaf in details` where section_id = %s and date BETWEEN %s and %s""",(section_id,'2016-01-01',filters.date)) 


def get_round(section_id,filters):
	return frappe.db.sql("""select sum(area)/section_area from `tabDaily Green Leaf in details` where section_id = %s and date BETWEEN %s AND %s ORDER BY date DESC LIMIT 1 """,(section_id, '2016-01-01',filters.date))

def find_round(section_id,filters):
	todate_round=get_round(section_id,filters)
	if todate_round[0][0].is_integer():
		return "complete"
	else:
		return "incomplete"




def get_to_date(section_id,filters):
	date6=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,'2016-01-01',filters.date))
	single_day=find_round(section_id,filters)
	if single_day=="complete":
		date7=date6
	else:
		date7=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id = %s and date<%s""",(section_id,date6))
	return date7


def get_from_date(section_id,filters):
	date1=get_to_date(section_id,filters) # IT WILL GET ALL THE TO DATE VALUE
	single_day=find_round(section_id,filters) # IT WILL FETCH IF THE ROUND IS ENDED ON THE LAST DAY PLUCKED OR NOT
	plucked_area=frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_id=%s and date=%s """,(section_id,date1)) # IT WILL FETCH THE PLUCKED AREA FOR EACH TO DATE
	original_area=get_section_details(section_id,filters) # IT WILL FETCH THE ORIGINAL AREA
	if single_day=="complete":# IF THE ROUNDS END ON THE LAST DAY OF FETCH 
		# IF IT COMPLETED IN A SINGLE DAY
		if round(float(plucked_area[0][0]),3)==round(float(original_area[0][0]),3):
			date4=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,'2016-01-01',filters.date))
		# IF IT TAK EMORE THAN ONE DAY TO COMPLETE THE ROUND
		elif round(float(plucked_area[0][0]),3)<round(float(original_area[0][0]),3):
			date4=0
			yesterday=datetime.strptime(date1[0][0],'%Y-%m-%d')-timedelta(days=1)
			date3=yesterday.date()
			plucked_area1=frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_id=%s and date=%s """,(section_id,date3))
			total_plucked=plucked_area[0][0]+plucked_area1[0][0]
			if total_plucked==original_area[0][0]:
				date4=date3
	else:
		date1=get_to_date(section_id,filters) # IT WILL GET ALL THE TO DATE VALUE
		plucked_area=frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_id=%s and date=%s """,(section_id,date1))
		todate_round=get_round(section_id,filters)
		date4=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where section_id=%s and date<%s""",(section_id,date1))
		plucked_area1=frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_id=%s and date=%s """,(section_id,date4)) 
		total_plucked=plucked_area[0][0]+plucked_area1[0][0]
		if total_plucked<original_area[0][0]:
			yesterday=datetime.strptime(date4[0][0],'%Y-%m-%d')-timedelta(days=1)
			date3=yesterday.date()
			plucked_area1=frappe.db.sql("""select area from `tabDaily Green Leaf in details` where section_id=%s and date=%s """,(section_id,date3))
			total_plucked+=plucked_area1[0][0]
			#return total_plucked
			if total_plucked==original_area[0][0]:
				date4=date3

	return date4

			
def get_actual_to_date_green_leaf(section_id,filters):
	date1=get_to_date(section_id,filters)
	#date2=get_from_date(section_id,filters)
	return frappe.db.sql("""select round(leaf_count/area,0) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s""",(section_id,date1,filters.date))

def get_to_date_budget(section_id,filters):
	date1=get_to_date(section_id,filters)
	return frappe.db.sql("""select round(((t.round_days*p.august)/(0.225*31)),0) from `tabDaily Green Leaf in details` t INNER JOIN `tabPruning Cycle` p  ON t.section_id=p.section_id where t.section_id = %s and t.date=%s""",(section_id,date1)) 
	
def get_plus_minus_budget(section_id,filters):
	bud=get_to_date_budget(section_id,filters)
	act=get_actual_to_date_green_leaf(section_id,filters)
	percent=round((round(act[0][0],0)-round(bud[0][0],0))*100/round((bud[0][0]),0),2)
	return percent




	
	



def get_sle_conditions(filters):
	conditions = []
	return "and {}".format(" and ".join(conditions)) if conditions else ""



def get_columns():
		
		columns = [{
			"fieldname": "division_name",
				"label": _("Division"),
				"fieldtype": "Link",
				"options": "Division",
				"width": 80

		}]

		columns.append({
				"fieldname": "section_id",
				"label": _("Section Id"),
				"fieldtype": "Link",
				"options": "Section",
				"width": 90
	    })

		columns.append({
				"fieldname": "section_name",
				"label": _("Section Name"),
				"fieldtype": "Link",
				"options": "Section",
				"width": 90
	    })
		
		columns.append({
				"fieldname": "original_area",
				"label": _("Area"),
				"fieldtype": "round(Float,2)",
				"options": "daily_green_leaf_in_details",
				"width": 70
	    })


		
		columns.append({
			"label": _("Round"),
			"fieldtype": "round(Float,5)",
			"width":71
		})

		columns.append({
			"label": _("From"),
			"fieldtype": "Data",
			"width":71
		})

		
		columns.append({
			"label": _("To"),
			"fieldtype": "Data",
			"width":71
		})

		columns.append({
			"label": _("Act"),
			"fieldtype": "round(float,0)",
			"width":71
		})

		columns.append({
			"label": _("Bud"),
			"fieldtype": "round(float,0)",
			"width":71
		})

		columns.append({
			"label": _("+/- %"),
			"fieldtype": "data",
			"width":71
		})

		columns.append({
			"label": _("done or not done"),
			"fieldtype": "data",
			"width":71
		})


		
		return columns

	