// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt
frappe.query_reports["Daily Green Leaf Report"] = {
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
            "fieldname":"bush_type",
            "label": __("Bush"),
            "fieldtype":"Select",
            "options": [
                { "value": "Mature"},
                { "value" : "Young"}],
            "default": "Mature",
            "reqd":1
         },

        {
            "fieldname":"prune_type",
            "label": __("Prune"),
            "fieldtype": "Link",
            "options": "Prune Type",
            "default": "",
            "reqd":1
         },

        

	]


		
    }
    //frappe.query_reports["Daily Green Leaf Report"] = $.extend({},"Ghatia Tea Estate");


