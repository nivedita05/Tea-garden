# -*- coding: utf-8 -*-
# Copyright (c) 2015, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime,timedelta
from frappe import _
from frappe import utils





class DailyGreenLeaf(Document):


	def validate(self):
		self.get_bush_name()
		self.get_prune_name()
		self.calculate_today_budget()


		self.validate_section_id()
		self.validtae_area()
		self.validate_uniqueness()

	
		self.calculate_round_number()
		
		

# check the area entered is less than the original area or not , otherwise give  an error message

	def validtae_area(self):
		for i in self.leaf_details:
			if(i.section_area<i.area):
				frappe.throw("the area entered is more than the original area  !!!!!!!")
						
# check the combination of date and garden is unique or not 

	def validate_uniqueness(self):
		name=frappe.db.sql("""select date from `tabDaily Green Leaf` 
				where date=%s and estate_name=%s and docstatus=1""",(self.date,self.estate_name))
		if name:
			frappe.throw("Record already exist for the date!!!!")

# if a record realated to a section for a particula garden on a particular date is already entered or not

	def validate_section_id(self):
		"""Set missing names and warn if duplicate"""
		found = []
		for section in self.leaf_details:

			if section.section_id in found:
				frappe.throw(_("Section {0} entered twice").format(section.section_id))

			found.append(section.section_id)
				
# calculate the budget corresponding to a particular date of a particular month

	def calculate_today_budget(self):
		
		for i in self.leaf_details:
			#if (frappe.utils.get_datetime(self.date).strftime('%Y')=="2016" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2017" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2018" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2019"):
				
			if(frappe.utils.get_datetime(self.date).strftime('%m')=="01"):
				prune_cycle=frappe.db.sql("""select january from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="02"):
				prune_cycle=frappe.db.sql("""select february from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/28),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="03"):
				prune_cycle=frappe.db.sql("""select march from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="04"):
				prune_cycle=frappe.db.sql("""select april from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="05"):
				prune_cycle=frappe.db.sql("""select may from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)


			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="06"):
				prune_cycle=frappe.db.sql("""select june from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)


			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="07"):
				prune_cycle=frappe.db.sql("""select july from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="08"):
				prune_cycle=frappe.db.sql("""select august from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="09"):
				prune_cycle=frappe.db.sql("""select september from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="10"):
				prune_cycle=frappe.db.sql("""select october from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="11"):
				prune_cycle=frappe.db.sql("""select november from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/30),2)

			elif(frappe.utils.get_datetime(self.date).strftime('%m')=="12"):
				prune_cycle=frappe.db.sql("""select december from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
				i.today_budget=round((float(prune_cycle[0][0])/31),2)

			
		

# get the prune name corresponding to the section

	def get_prune_name(self):
		
		for i in self.leaf_details:
			#if (frappe.utils.get_datetime(self.date).strftime('%Y')=="2016" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2017" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2018" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2019"):
			prune_cycle=frappe.db.sql("""select  prune_type from `tabPruning Cycle` where year=%s and section_id=%s limit 1""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
			i.prune_type=prune_cycle[0]
			

# get the bush name corresponding to the section

	def get_bush_name(self):
		
		for i in self.leaf_details:
			#if (frappe.utils.get_datetime(self.date).strftime('%Y')=="2016" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2017" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2018" or frappe.utils.get_datetime(self.date).strftime('%Y')=="2019"):
			prune_bush=frappe.db.sql("""select bush_type from `tabPruning Cycle` where year=%s and section_id=%s""",(frappe.utils.get_datetime(self.date).strftime('%Y'),i.section_id))
			i.bush_type=prune_bush[0]



	def calculate_round_number(self):	
					
		for i in self.leaf_details:
			section_area  =i.section_area
			previous_day  = datetime.strptime(i.date,'%Y-%m-%d')-timedelta(days=1)
			plucked_area  =frappe.db.sql("""select sum(area) from `tabDaily Green Leaf in details` where section_id = %s and date between %s and %s and docstatus=1""",(i.section_id,datetime(datetime.now().year, 1, 1),previous_day.date()))
			if plucked_area[0][0] is None:
				if i.area >= section_area:
					i.round_number =round( i.area/section_area,4)
				else:
					i.round_number = 0	
			else:
				i.round_number = round((plucked_area[0][0]+i.area)/section_area,4) 
				#frappe.throw(last_round_no)	

			if round(float(i.round_number),4).is_integer():
				i.mark="Yes"
			else:
				i.mark="No"


			date1=frappe.db.sql("""select max(date) from `tabDaily Green Leaf in details` where mark='Yes' and docstatus=1 and section_id=%s""",(i.section_id))
			area1=frappe.db.sql("""select sum(area) from `tabDaily Green Leaf in details` where section_id = %s and date>%s and docstatus=1""",(i.section_id,date1))
			if area1[0][0]:
				if round((area1[0][0]+i.area),2)>round(i.section_area,2):
					#frappe.throw("please check whatever area you have entered is not correct")
					frappe.throw(_("Section area entered for {0} is not correct").format(i.section_name))
					#frappe.throw(i.section_id)			#previous_day  = datetime.strptime(i.date,'%Y-%m-%d')-timedelta(days=1)
				elif round((area1[0][0]+i.area),2)==round(i.section_area,2):
					i.mark = "Yes"
				#else:
					#i.mark = "No"
			else:
				mark = 'No'			