from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
import frappe
from datetime import datetime



class CustomSalesInvoice(SalesInvoice):
    def on_submit(self):
        counter = 0
        if self.pos_profile == 'Casher 4 Armsha':
            # sales_list = frappe.get_list('Sales Invoice',fields=['name'],filters={'posting_date': self.posting_date,'pos_profile':'Casher 4 Armsha'})
            sales_list = frappe.db.count('Sales Invoice',{'pos_profile':'Casher 4 Armsha', 'posting_date': datetime.now().date()})
            counter = sales_list + 1
            self.custom_daily_counter = counter
        else:
            continue

