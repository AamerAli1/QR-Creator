import tools
import QRCreator
import file_manipulation
import time as t

while True:
    t.sleep(5)
    if file_manipulation.check_if_to_print():

        current_file = str(file_manipulation.get_new_file())
        print(current_file)

        # current_file = "to_print\\hello.TXT"

        file = open(current_file, encoding='utf-8')
        content = file.readlines()
        number_of_lines = (len(content))

        # Extracting property details
        property_line = content[0].split(",")

        printer_name = property_line[0]
        copies = property_line[1]

        # Extracting company details
        company_line = content[1].split(",")

        company_vat_no = company_line[0]
        company_name = company_line[1]
        company_address = company_line[2]
        company_email = company_line[3]
        company_telephone = company_line[4]

        # Extracting header details
        header_line = content[2].split(",")

        date = header_line[0]
        time = header_line[1]
        ref_no_1 = header_line[2]
        ref_no_2 = header_line[3]
        inv_number = header_line[4]
        inv_description = header_line[5]
        cust_name = header_line[6]
        cust_vat_no = header_line[7]
        cust_address = header_line[8]
        cust_no = header_line[9]
        warehouse_no = header_line[10]
        warehouse_name = header_line[11]
        total_weight = header_line[12]
        inv_type = header_line[13]
        cust_other_info = header_line[14]
        salesman_no = header_line[15]
        salesman_name = header_line[16]
        extra_field_cap_1 = header_line[17]
        extra_field_date_1 = header_line[18]
        extra_field_cap_2 = header_line[19]
        extra_field_date_2 = header_line[20]
        extra_field_cap_3 = header_line[21]
        extra_field_date_3 = header_line[22]



        # Extracting footer details
        footer_line = content[3].split(",")

        total_excl_vat = footer_line[0]
        discount = footer_line[1]
        vat_amount = footer_line[2]
        total_amount = footer_line[3]
        amount_in_words = footer_line[4]
        user_id = footer_line[5]
        user_name = footer_line[6]
        additional_charges_amt = footer_line[7]
        additional_charges_disc = footer_line[8]


        file.close()


        # Extracting product details
        a_file = open(current_file , encoding='utf-8')
        lines_to_read = list(range(3,number_of_lines))


        item_no_list = []
        item_arabic_name_list = []
        item_english_name_list = []
        unit_list = []
        expiry_date_list = []
        batch_no_list = []
        quantity_list = []
        unit_price_list = []
        excl_vat_list = []
        vat_list = []
        vat_amt_list = []
        total_amount_list = []

        for position, line in enumerate(a_file):
            if position in lines_to_read:
                to_read = a_file.readlines()
                for i in range(0, number_of_lines - 4):
                    full_product_list = to_read[i].split(",")

                    item_no_list_member = full_product_list[0]
                    item_arabic_name_list_member = full_product_list[1]
                    item_english_name_list_member = full_product_list[2]
                    unit_list_member = full_product_list[3]
                    expiry_date_list_member = full_product_list[4]
                    batch_no_list_member = full_product_list[5]
                    quantity_list_member = full_product_list[6]
                    unit_price_list_member = full_product_list[7]
                    excl_vat_list_member = full_product_list[8]
                    vat_list_member = full_product_list[9]
                    vat_amt_list_member = full_product_list[10]
                    total_list_member = full_product_list[11]

                    item_no_list.append(item_no_list_member)
                    item_arabic_name_list.append(item_arabic_name_list_member)
                    item_english_name_list.append(item_english_name_list_member)
                    unit_list.append(unit_list_member)
                    expiry_date_list.append(expiry_date_list_member)
                    batch_no_list.append(batch_no_list_member)
                    quantity_list.append(quantity_list_member)
                    unit_price_list.append(unit_price_list_member)
                    excl_vat_list.append(excl_vat_list_member)
                    vat_list.append(vat_list_member)
                    vat_amt_list.append(vat_amt_list_member)
                    total_amount_list.append(total_list_member)





        a_file.close()

        company_details_dict = {
            "company_vat_no": company_vat_no,
            "company_name": company_name,
            "company_address": company_address,
            "company_email": company_email,
            "company_telephone": company_telephone
        }

        header_dict = {
        "date" : date,
        "time" : time,
        "ref_no_1" : ref_no_1,
        "ref_no_2" : ref_no_2,
        "inv_number" : inv_number,
        "inv_description" : inv_description,
        "cust_name" : cust_name,
        "cust_vat_no" : cust_vat_no,
        "cust_address" : cust_address,
        "cust_no" : cust_no,
        "warehouse_no" : warehouse_no,
        "warehouse_name" : warehouse_name,
        "total_weight" : total_weight,
        "inv_type" : inv_type,
        "cust_other_info" : cust_other_info,
        "salesman_no" : salesman_no,
        "salesman_name" : salesman_name,
        "extra_field_cap_1" : extra_field_cap_1,
        "extra_field_date_1" : extra_field_date_1,
        "extra_field_cap_2" : extra_field_cap_2,
        "extra_field_date_2" : extra_field_date_2,
        "extra_field_cap_3" : extra_field_cap_3,
        "extra_field_date_3" : extra_field_date_3,
        "QR" : QRCreator.createQR(company_name,company_vat_no,date,vat_amount,total_amount,inv_number)
        }

        footer_dict = {
            "total_excl_vat": total_excl_vat,
            "discount": discount,
            "vat_amount": vat_amount,
            "total_amount": total_amount,
            "amount_in_words": amount_in_words,
            "user_id" : user_id,
            "user_name" : user_name ,
            "additional_charges_amt" : additional_charges_amt ,
            "additional_charges_disc" : additional_charges_disc

        }

        product_dict = {
            "item_no": item_no_list,
            "item_arabic_name": item_arabic_name_list,
            "item_english_name": item_english_name_list,
            "Unit": unit_list,
            "expiry_date" : expiry_date_list,
            "batch_no" : batch_no_list,
            "quantity" : quantity_list,
            "price": unit_price_list,
            "excl_vat": excl_vat_list,
            "vat": vat_amt_list,
            "vat_amt": vat_list,
            "total": total_amount_list
        }
        total_page_required = (45//24)+1
        print(total_page_required)
        mainDict = {
            "company_details_dict" : company_details_dict,
            "header_dict" : header_dict,
            "footer_dict" : footer_dict,
            "product_dict" : product_dict,
            "total_no_of_products":len(product_dict['item_no'])
        }

        break
        # invoice_path = "invoices\\" + inv_number +".pdf"
        # # tools.HTMLToPDF(tools.populate_HTML("HTML_Template/index.html", mainDict), invoice_path)
        # tools.toPrinter(tools.HTMLToPDF(tools.populate_HTML("HTML_Template/index.html",mainDict), invoice_path),printer_name)

        # file is printed by here


        # file_manipulation.move_done_file(current_file)

