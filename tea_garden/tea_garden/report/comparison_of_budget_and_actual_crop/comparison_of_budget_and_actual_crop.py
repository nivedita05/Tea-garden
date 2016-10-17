# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import utils
from frappe.utils import flt
from datetime import datetime,timedelta
import calendar



def execute(filters=None):
	columns = get_columns()
	report_entries = get_report_entries(filters)
	data = []

	

	for sle in report_entries:
		month_wise_budget_for_jan=get_monthly_budget(sle.section_name,filters,"01")
		month_wise_budget_for_feb=get_monthly_budget(sle.section_name,filters,"02")
		
		month_wise_budget_for_mar=get_monthly_budget(sle.section_name,filters,"03")
		month_wise_budget_for_apr=get_monthly_budget(sle.section_name,filters,"04")

		month_wise_budget_for_may=get_monthly_budget(sle.section_name,filters,"05")
		month_wise_budget_for_jun=get_monthly_budget(sle.section_name,filters,"06")

		month_wise_budget_for_jul=get_monthly_budget(sle.section_name,filters,"07")
		month_wise_budget_for_aug=get_monthly_budget(sle.section_name,filters,"08")

		month_wise_budget_for_sep=get_monthly_budget(sle.section_name,filters,"09")
		month_wise_budget_for_oct=get_monthly_budget(sle.section_name,filters,"10")

		month_wise_budget_for_nov=get_monthly_budget(sle.section_name,filters,"11")
		month_wise_budget_for_dec=get_monthly_budget(sle.section_name,filters,"12")

		


		total=get_projected_yield(sle.section_name,filters)
		vac=get_vacancy_percentage(sle.section_name,filters)




		month_wise_act_for_jan=get_monthly_act(sle.section_name,filters,"01")
		month_wise_act_for_feb=get_monthly_act(sle.section_name,filters,"02")

		month_wise_act_for_mar=get_monthly_act(sle.section_name,filters,"03")
		month_wise_act_for_apr=get_monthly_act(sle.section_name,filters,"04")


		month_wise_act_for_may=get_monthly_act(sle.section_name,filters,"05")
		month_wise_act_for_jun=get_monthly_act(sle.section_name,filters,"06")

		month_wise_act_for_jul=get_monthly_act(sle.section_name,filters,"07")
		month_wise_act_for_aug=get_monthly_act(sle.section_name,filters,"08")

		month_wise_act_for_sep=get_monthly_act(sle.section_name,filters,"09")
		month_wise_act_for_oct=get_monthly_act(sle.section_name,filters,"10")

		month_wise_act_for_nov=get_monthly_act(sle.section_name,filters,"11")
		month_wise_act_for_dec=get_monthly_act(sle.section_name,filters,"12")


		act_total=get_act_for_year(sle.section_name,filters)
		percent=round((act_total[0][0]*100)/total[0][0],0)


		

		jan_diff=get_diff(sle.section_name,filters,"01")
		feb_diff=get_diff(sle.section_name,filters,"02")

		mar_diff=get_diff(sle.section_name,filters,"03")
		apr_diff=get_diff(sle.section_name,filters,"04")

		may_diff=get_diff(sle.section_name,filters,"05")
		jun_diff=get_diff(sle.section_name,filters,"06")
		
		jul_diff=get_diff(sle.section_name,filters,"07")
		aug_diff=get_diff(sle.section_name,filters,"08")

		sep_diff=get_diff(sle.section_name,filters,"09")
		oct_diff=get_diff(sle.section_name,filters,"10")

		nov_diff=get_diff(sle.section_name,filters,"11")
		dec_diff=get_diff(sle.section_name,filters,"12")
		
		
		tot_diff=act_total[0][0]-total[0][0]
		per_mon_bud=get_budget_for_a_particular_mon(sle.section_name,filters,frappe.utils.get_datetime(filters.date).strftime('%m'))
		per_mon_act=get_act_for_a_particular_mon(sle.section_name,filters,frappe.utils.get_datetime(filters.date).strftime('%m'))
		per_mon_diff=get_diff_per_month(sle.section_name,filters,frappe.utils.get_datetime(filters.date).strftime('%m'))


		mon_todate_act=get_todate_act_for_part_month(sle.section_name,filters)
		mon_todate_bud=get_todate_bud_for_part_month(sle.section_name,filters,frappe.utils.get_datetime(filters.date).strftime('%m'))
		mon_todate_diff=round(mon_todate_act[0][0]-mon_todate_bud,2)


		per_cent=round((mon_todate_bud*100)/mon_todate_act[0][0],2)

		bud_made_tea=round(sle.section_area*mon_todate_bud,0)
		act_made_tea=round(sle.section_area*mon_todate_act[0][0],0)
		diff_made_tea=round(act_made_tea-bud_made_tea,0)


		data.append([sle.division_name,sle.section_name,sle.section_area,'Budget',month_wise_budget_for_jan,month_wise_budget_for_feb,month_wise_budget_for_mar,month_wise_budget_for_apr,month_wise_budget_for_may,month_wise_budget_for_jun,month_wise_budget_for_jul,month_wise_budget_for_aug,month_wise_budget_for_sep,month_wise_budget_for_oct,month_wise_budget_for_nov,month_wise_budget_for_dec,total,percent,vac,per_mon_bud,mon_todate_bud,per_cent,bud_made_tea])
		data.append(['','','','Act',month_wise_act_for_jan,month_wise_act_for_feb,month_wise_act_for_mar,month_wise_act_for_apr,month_wise_act_for_may,month_wise_act_for_jun,month_wise_act_for_jul,month_wise_act_for_aug,month_wise_act_for_sep,month_wise_act_for_oct,month_wise_act_for_nov,month_wise_act_for_dec,act_total,'','',per_mon_act,mon_todate_act,'',act_made_tea])
		data.append(['','','',"<b>"+'(+/-)'+"<b>","<b>"+str(jan_diff)+"</b>","<b>"+str(feb_diff)+"</b>","<b>"+str(mar_diff)+"</b>","<b>"+str(apr_diff)+"</b>","<b>"+str(may_diff)+"</b>","<b>"+str(jun_diff)+"</b>","<b>"+str(jul_diff)+"</b>","<b>"+str(aug_diff)+"</b>","<b>"+str(sep_diff)+"</b>","<b>"+str(oct_diff)+"</b>","<b>"+str(nov_diff)+"</b>","<b>"+str(dec_diff)+"</b>","<b>"+str(tot_diff)+"</b>",'','',"<b>"+str(per_mon_diff)+"</b>","<b>"+str(mon_todate_diff)+"</b>",'',"<b>"+str(diff_made_tea)+"</b>"])
		#data.append([])

	return columns, data


def get_report_entries(filters):
	return frappe.db.sql("""select distinct division_name ,section_name ,section_area from `tabDaily Green Leaf in details` where estate_name = %s and prune_type=%s order by division_name""",(filters.estate_name,filters.prune_type),as_dict=1)

def get_monthly_budget(section_name,filters,month):

	
	#report_entries = get_report_entries(filters)
	budget=0
	#for sle in report_entries:

	if month == "01" :
		budget = get_month_wise_budget_for_jan(section_name,filters)
	elif month == "02":
		budget = get_month_wise_budget_for_feb(section_name,filters)
	elif month == "03":
		budget = get_month_wise_budget_for_mar(section_name,filters)
	elif month == "04":
		budget = get_month_wise_budget_for_apr(section_name,filters)
	elif month == "05":
		budget = get_month_wise_budget_for_may(section_name,filters)
	elif month == "06":
		budget = get_month_wise_budget_for_jun(section_name,filters)
	elif month == "07":
		budget = get_month_wise_budget_for_jul(section_name,filters)
	elif month == "08":
		budget = get_month_wise_budget_for_aug(section_name,filters)
	elif month == "09":
		budget = get_month_wise_budget_for_sep(section_name,filters)
	elif month == "10":
		budget = get_month_wise_budget_for_oct(section_name,filters)
	elif month == "11":
		budget = get_month_wise_budget_for_nov(section_name,filters)
	elif month == "12":
		budget = get_month_wise_budget_for_dec(section_name,filters)
	return budget



def get_monthly_act(section_name,filters,month):
	
	act=0
	

	if month == "01" :
		act = get_act_for_jan(section_name,filters)
	elif month == "02":
		act = get_act_for_feb(section_name,filters)
	elif month == "03":
		act =get_act_for_mar(section_name,filters)
	elif month == "04":
		act = get_act_for_apr(section_name,filters)
	elif month == "05":
		act = get_act_for_may(section_name,filters)
	elif month == "06":
		act =get_act_for_jun(section_name,filters)
	elif month == "07":
		act =get_act_for_jul(section_name,filters)
	elif month == "08":
		act = get_act_for_aug(section_name,filters)
	elif month == "09":
		act =get_act_for_sep(section_name,filters)
	elif month == "10":
		act =get_act_for_oct(section_name,filters)
	elif month == "11":
		act =get_act_for_nov(section_name,filters)
	elif month == "12":
		act =get_act_for_dec(section_name,filters)
	return act



def get_diff(section_name,filters,month):
	pass
	
	diff=0
	

	if month == "01" :
		diff= get_diff_jan(section_name,filters)
	elif month == "02":
		diff = get_diff_feb(section_name,filters)
	elif month == "03":
		diff = get_diff_mar(section_name,filters)
	elif month == "04":
		diff = get_diff_apr(section_name,filters)
	elif month == "05":
		diff = get_diff_may(section_name,filters)
	elif month == "06":
		diff =get_diff_jun(section_name,filters)
	elif month == "07":
		diff = get_diff_jul(section_name,filters)
	elif month == "08":
		diff = get_diff_aug(section_name,filters)
	elif month == "09":
		diff = get_diff_sep(section_name,filters)
	elif month == "10":
		diff = get_diff_oct(section_name,filters)
	elif month == "11":
		diff =get_diff_nov(section_name,filters)
	elif month == "12":
		diff = get_diff_dec(section_name,filters)
	return diff


def get_budget_for_a_particular_mon(section_name,filters,month):
	month=frappe.utils.get_datetime(filters.date).strftime('%m')
	cur_mon_bud=get_monthly_budget(section_name,filters,month)
	return round(float(cur_mon_bud[0][0])*float(frappe.utils.get_datetime(filters.date).strftime('%d'))/calendar.monthrange(int(frappe.utils.get_datetime(filters.date).strftime('%d')),int(month))[1],2)
	#return cur_mon_bud
	
def get_act_for_a_particular_mon(section_name,filters,month):
	month=frappe.utils.get_datetime(filters.date).strftime('%m')
	cur_mon_act=get_monthly_act(section_name,filters,month)
	return round(float(cur_mon_act[0][0])*float(frappe.utils.get_datetime(filters.date).strftime('%d'))/calendar.monthrange(int(frappe.utils.get_datetime(filters.date).strftime('%d')),int(month))[1],2)
	#return cur_mon_act


def get_diff_per_month(section_name,filters,month):
	act=get_act_for_a_particular_mon(section_name,filters,month)
	bud=get_budget_for_a_particular_mon(section_name,filters,month)
	return round(act-bud,2)






def get_month_wise_budget_for_jan(section_name,filters):
	return frappe.db.sql("""select january from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_feb(section_name,filters):
	return frappe.db.sql("""select february from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_mar(section_name,filters):
	return frappe.db.sql("""select march from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_apr(section_name,filters):
	return frappe.db.sql("""select april from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_may(section_name,filters):
	return frappe.db.sql("""select may from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_jun(section_name,filters):
	return frappe.db.sql("""select june from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_jul(section_name,filters):
	return frappe.db.sql("""select july from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_aug(section_name,filters):
	return frappe.db.sql("""select august from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_sep(section_name,filters):
	return frappe.db.sql("""select september from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_oct(section_name,filters):
	return frappe.db.sql("""select october from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_nov(section_name,filters):
	return frappe.db.sql("""select november from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_month_wise_budget_for_dec(section_name,filters):
	return frappe.db.sql("""select december from `tabPruning Cycle` where section_name=%s """,(section_name))











def get_projected_yield(section_name,filters):
	return frappe.db.sql("""select projected_yield from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_vacancy_percentage(section_name,filters):
	return frappe.db.sql("""select vacancy_percentage from `tabPruning Cycle` where section_name=%s """,(section_name))

def get_act_for_jan(section_name,filters):
	return frappe.db.sql("""select coalesce(sum(leaf_count)*0.225/section_area,0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 1, 1),datetime(datetime.now().year,1,31)))

def get_act_for_feb(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 2, 1),datetime(datetime.now().year,2,28)))
	

def get_act_for_mar(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 3, 1),datetime(datetime.now().year,3,31)))

def get_act_for_apr(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 4, 1),datetime(datetime.now().year,4,30)))

def get_act_for_may(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 5, 1),datetime(datetime.now().year,5,31)))
	
def get_act_for_jun(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 6, 1),datetime(datetime.now().year,6,30)))


def get_act_for_jul(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 7, 1),datetime(datetime.now().year,7,31)))

def get_act_for_aug(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 8, 1),datetime(datetime.now().year,8,21)))
	

def get_act_for_sep(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 9, 1),datetime(datetime.now().year,9,30)))

def get_act_for_oct(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 10, 1),datetime(datetime.now().year,10,31)))

def get_act_for_nov(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 11, 1),datetime(datetime.now().year,11,30)))
	
def get_act_for_dec(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 12, 1),datetime(datetime.now().year,12,31)))







def get_todate_act_for_part_month(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 1, 1),filters.date))



def get_todate_bud_for_part_month(section_name,filters,month):
	month=frappe.utils.get_datetime(filters.date).strftime('%m')
	bud = 0.0
	for i in range(1,int(month)-1,1):
		bud +=float(get_monthly_budget(section_name,filters,str(i).zfill(2))[0][0])

	bud_mon=float(get_budget_for_a_particular_mon(section_name,filters,month))
	bud=bud+bud_mon
	return round(bud,2)








def get_act_for_year(section_name,filters):
	return frappe.db.sql("""select coalesce(round((sum(leaf_count)*0.225)/section_area,2),0) from `tabDaily Green Leaf in details` where section_name=%s and date between %s and %s """,(section_name,datetime(datetime.now().year, 1, 1),datetime(datetime.now().year,12,31)))




def get_diff_jan(section_name,filters):
	jan_act=get_act_for_jan(section_name,filters)
	jan_bud=get_month_wise_budget_for_jan(section_name,filters)
	return round(jan_act[0][0]-float(jan_bud[0][0]),2)


def get_diff_feb(section_name,filters):
	feb_act=get_act_for_feb(section_name,filters)
	feb_bud=get_month_wise_budget_for_feb(section_name,filters)
	return round(feb_act[0][0]-float(feb_bud[0][0]),2)

def get_diff_mar(section_name,filters):
	mar_act=get_act_for_mar(section_name,filters)
	mar_bud=get_month_wise_budget_for_mar(section_name,filters)
	return round(mar_act[0][0]-float(mar_bud[0][0]),2)

def get_diff_apr(section_name,filters):
	apr_act=get_act_for_apr(section_name,filters)
	apr_bud=get_month_wise_budget_for_apr(section_name,filters)
	return round(apr_act[0][0]-float(apr_bud[0][0]),2)

def get_diff_may(section_name,filters):
	may_act=get_act_for_may(section_name,filters)
	may_bud=get_month_wise_budget_for_may(section_name,filters)
	return round(may_act[0][0]-float(may_bud[0][0]),2)

def get_diff_jun(section_name,filters):
	jun_act=get_act_for_jun(section_name,filters)
	jun_bud=get_month_wise_budget_for_jun(section_name,filters)
	return round(jun_act[0][0]-float(jun_bud[0][0]),2)

def get_diff_jul(section_name,filters):
	jul_act=get_act_for_jul(section_name,filters)
	jul_bud=get_month_wise_budget_for_jul(section_name,filters)
	return round(jul_act[0][0]-float(jul_bud[0][0]),2)


def get_diff_aug(section_name,filters):
	aug_act=get_act_for_aug(section_name,filters)
	aug_bud=get_month_wise_budget_for_aug(section_name,filters)
	return round(aug_act[0][0]-float(aug_bud[0][0]),2)

def get_diff_sep(section_name,filters):
	sep_act=get_act_for_sep(section_name,filters)
	sep_bud=get_month_wise_budget_for_sep(section_name,filters)
	return round(sep_act[0][0]-float(sep_bud[0][0]),2)

def get_diff_oct(section_name,filters):
	oct_act=get_act_for_oct(section_name,filters)
	oct_bud=get_month_wise_budget_for_oct(section_name,filters)
	return round(oct_act[0][0]-float(oct_bud[0][0]),2)

def get_diff_nov(section_name,filters):
	nov_act=get_act_for_nov(section_name,filters)
	nov_bud=get_month_wise_budget_for_nov(section_name,filters)
	return round(nov_act[0][0]-float(nov_bud[0][0]),2)

def get_diff_dec(section_name,filters):
	dec_act=get_act_for_dec(section_name,filters)
	dec_bud=get_month_wise_budget_for_dec(section_name,filters)
	return round(dec_act[0][0]-float(dec_bud[0][0]),2)

def get_columns():
		
	columns = [{
		"fieldname": "division_name",
		"label": _("Division"),
		"fieldtype": "Link",
		"options": "Division",
		"width": 80

	}]

	columns.append({
		"fieldname": "section_name",
		"label": _("Section"),
		"fieldtype": "Link",
		"options": "Section",
		"width": 150
	    })


	columns.append({
		"fieldname": "section_area",
		"label": _("Area"),
		"fieldtype": "Data",
		"width": 50
	    })

	columns.append({
		"fieldname": "blank",
		"label": _(" "),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "january",
		"label": _("JAN"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "february",
		"label": _("FEB"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "march",
		"label": _("MAR"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "april",
		"label": _("APR"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "may",
		"label": _("MAY"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "june",
		"label": _("JUN"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "july",
		"label": _("JUL"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "august",
		"label": _("AUG"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "september",
		"label": _("SEP"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "october",
		"label": _("OCT"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "november",
		"label": _("NOV"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "december",
		"label": _("DEC"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "total",
		"label": _("Total"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "achv",
		"label": _("achv %"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "vac",
		"label": _("VAC %"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "mon",
		"label": _("Mon"),
		"options": "Data",
		"width": 70
	    })

	columns.append({
		"fieldname": "todate",
		"label": _("Todate"),
		"options": "Data",
		"width": 70
	    })
	
	columns.append({
		"fieldname": "todt",
		"label": _("todate %"),
		"options": "Data",
		"width": 70
	    })


	columns.append({
		"fieldname": "made_tea",
		"label": _("Made Tea"),
		"options": "Data",
		"width": 70
	    })

	return columns
