// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt


frappe.query_reports["Comparison of Budget and Actual Crop"] = {
	"filters": [
	 {
            "fieldname":"date",
            "label": __("DATE"),
            "fieldtype": "Date",
            "options": "",
            "default": frappe.datetime.get_today(),
            "reqd":1
        },


        {
            "fieldname":"estate_name",
            "label": __("ESTATE NAME"),
            "fieldtype": "Link",
            "options": "Estate",
            "default": frappe.defaults.get_user_default("Estate"),
            "reqd":1
         },

        {
            "fieldname":"prune_type",
            "label": __("PRUNE"),
            "fieldtype": "Link",
            "options": "Prune Type",
            "default": frappe.defaults.get_user_default("Prune"),
            "reqd":1
         },


       

	]
		
    }