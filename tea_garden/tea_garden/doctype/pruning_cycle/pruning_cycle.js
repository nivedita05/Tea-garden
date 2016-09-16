// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt

//frappe.ui.form.on('Pruning Cycle', {
//	refresh: function(frm) {

//	}
//});

// the naming series fro the pruning cycle
frappe.ui.form.on("Pruning Cycle", "validate", function(frm) {
    frm.pruning_code="";
    name=frm.doc.year+"-"+frm.doc.section_id;
    frm.set_value("pruning_code",name);
});
   
// get the value of each month after calculatin projected yield*percentage/100
frappe.ui.form.on("Pruning Cycle", "validate", function(frm) {
       
       frm.set_value("january",frm.doc.projected_yield*frm.doc.january_1*0.01)
       frm.set_value("february",frm.doc.projected_yield*frm.doc.february_1*0.01)
       frm.set_value("march",frm.doc.projected_yield*frm.doc.march_1*0.01)
       frm.set_value("april",frm.doc.projected_yield*frm.doc.april_1*0.01)
       frm.set_value("may",frm.doc.projected_yield*frm.doc.may_1*0.01)
       frm.set_value("june",frm.doc.projected_yield*frm.doc.june_1*0.01)
       frm.set_value("july",frm.doc.projected_yield*frm.doc.july_1*0.01)
       frm.set_value("august",frm.doc.projected_yield*frm.doc.august_1*0.01)
       frm.set_value("september",frm.doc.projected_yield*frm.doc.september_1*0.01)
       frm.set_value("october",frm.doc.projected_yield*frm.doc.october_1*0.01)
       frm.set_value("november",frm.doc.projected_yield*frm.doc.november_1*0.01)
       frm.set_value("december",frm.doc.projected_yield*frm.doc.december_1*0.01)

      sum=frm.doc.projected_yield*frm.doc.january_1*0.01+frm.doc.projected_yield*frm.doc.february_1*0.01+
frm.doc.projected_yield*frm.doc.march_1*0.01+frm.doc.projected_yield*frm.doc.april_1*0.01+frm.doc.projected_yield*frm.doc.may_1*0.01+frm.doc.projected_yield*frm.doc.june_1*0.01+frm.doc.projected_yield*frm.doc.july_1*0.01+frm.doc.projected_yield*frm.doc.august_1*0.01+frm.doc.projected_yield*frm.doc.september_1*0.01+frm.doc.projected_yield*frm.doc.october_1*0.01+frm.doc.projected_yield*frm.doc.november_1*0.01+frm.doc.projected_yield*frm.doc.december_1*0.01

      frm.set_value("actual_yield",sum)

});