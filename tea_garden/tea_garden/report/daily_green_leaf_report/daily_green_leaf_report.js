// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Daily Green Leaf Report"] = {
	"filters": [
	 {
            "fieldname":"Date",
            "label": __("DATE"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.defaults.get_user_default("date"),
            "reqd":1
        },


        {
            "fieldname":"estate_name",
            "label": __("ESTATE NAME"),
            "fieldtype": "Link",
            "options": "Estate",
            "default": frappe.defaults.get_user_default("estate"),
            "reqd":1
         }

	]


	
}

