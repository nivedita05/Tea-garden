// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

//frappe.ui.form.on('Pruning Cycle', {
//	refresh: function(frm) {

//	}
//});

frappe.ui.form.on("Pruning Cycle", "validate", function(frm) {
    frm.pruning_code="";
    name=frm.doc.year+"-"+frm.doc.section_name;
    frm.set_value("pruning_code",name);
});
   

