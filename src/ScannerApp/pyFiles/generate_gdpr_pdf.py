import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
import sys
from datetime import datetime
import argparse

def generate_current_date():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y.%m.%d')

    return current_date

def create_certificate(name, birth_date, current_date, signature_path, output_path):
    signature_path = os.path.abspath(signature_path)
    template_dir = os.path.abspath('.')
    
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('certificate_template.html')
    
    html_content = template.render(name=name, birth_date=birth_date, current_date=current_date, signature_path=signature_path)
    
    options = {
        'enable-local-file-access': True
    }
    pdfkit.from_string(html_content, output_path, options=options)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='GDPR certificate generator script.')
    parser.add_argument('-uc', '--usercode', type=str, default='UC000000', help='USER CODE')
    parser.add_argument('-ln', '--legalname', type=str, default='LEGAL NAME', help='LEGAL NAME OF USER')
    parser.add_argument('-bd', '--birthday', type=str, default='2000.01.01.', help='BIRTH DATE OF USER')
    args = parser.parse_args()
    current_date = generate_current_date()  
    signature_path = "Signatures/" + args.usercode + ".png"
    output_path = "GDPR_certificates/GDPR_certificate_" + args.legalname + "_" + args.usercode + ".pdf"
    
    create_certificate(args.legalname, args.birthday, current_date, signature_path, output_path)


# test with:
# python3 generate_gdpr_pdf.py -uc VA011208 -ln "Vasi Andras" -bd "2001.12.08."

