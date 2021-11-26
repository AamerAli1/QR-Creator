import qrcode
import pathlib
from PIL import Image
from QR_Encoder import Fatoora


def createQR(company_name,company_vat,date,time,vat_amt,total_amt,inv_no):


    fatoora_obj = Fatoora(
        seller_name=company_name,
        tax_number=int(company_vat),  # or "1234567891"
        invoice_date= date + "t" + time,  # Timestamp
        total_amount=float(total_amt),  # or 100.0, 100.00, "100.0", "100.00"
        tax_amount=float(vat_amt),  # or 15.0, 15.00, "15.0", "15.00"
    )

    print(fatoora_obj.base64)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(fatoora_obj.base64)
    img = qr.make_image(fill_color="black")

    path = str(pathlib.Path(__file__).parent.resolve()) + "\QRs"
    PNGName = path + "\Invoice-" +  str(inv_no) + ".png"

    img.save(PNGName)
    return PNGName


