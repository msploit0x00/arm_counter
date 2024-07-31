from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
import frappe
from datetime import datetime



class CustomSalesInvoice(SalesInvoice):
    def validate(self):
        frappe.msgprint("HERE")
        # counter = 0
        # if self.pos_profile == 'Casher 4 Armsha':
        counter = 0
            # sales_list = frappe.get_list('Sales Invoice',fields=['name'],filters={'posting_date': self.posting_date,'pos_profile':'Casher 4 Armsha'})
            # sales_list = frappe.db.get_list('Sales Invoice',{'pos_profile':'Casher 4 Armsha', 'posting_date': datetime.now().date()})
                # count = 0
        invoices = frappe.get_list(
                "Sales Invoice",
                filters={"posting_date": self.posting_date,'pos_profile':'Casher 4 Armsha'},
                fields=["name"],
                limit_start=0,
                limit_page_length=5000,
            )

        if invoices:
            counter = len(invoices)
            # counter = sales_list + 1
            self.custom_daily_counter2 = counter + 1
            self.set_missing_values()
            self.flags.ignore_permissions = True
            frappe.flags.ignore_account_permission = True
            frappe.msgprint("Done")
            frappe.db.set_value('Sales Invoice',self.name,self.custom_daily_counter2,counter)

