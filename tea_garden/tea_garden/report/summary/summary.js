// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

frappe.query_reports["Summary"] = {
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

       

	]
		
    }