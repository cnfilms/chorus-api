import base64


def base_64_encode(data: str):
    return base64.b64encode(data.encode()).decode()


def base_64_encode_file(filepath):
    with open(filepath, 'rb') as file:  # 'rb' = read binary
        return base64.b64encode(file.read()).decode('ascii')


def base_64_decode(data: str):
    return base64.b64decode(data).decode()


def base_64_decode_to_file(base64_string, output_filepath):
    with open(output_filepath, 'wb') as file:
        file.write(base64.b64decode(base64_string))


def write_base_64_to_file(data: str, filepath: str, filename: str):
    destination = f"{filepath}/{filename}"
    with open(destination, "wb+") as f:
        f.write(base64.b64decode(data))
    return destination


def simple_pdf_to_base64(file):
    file_bytes = base64.b64encode(open(file, "rb").read())
    base_64 = file_bytes.decode("ascii")
    return base_64


if __name__ == '__main__':
    # Debug encode / decode files
    # Encoder le PDF
    pdf_path = '/tmp/F_Haut_et_Court_Distri_281125_104419054703.pdf'
    base64_text_path = '/tmp/decoded_facture_base64.txt'
    output_pdf_path = '/tmp/facture_decoded.pdf'

    pdf_base64 = base_64_encode_file(pdf_path)

    # Afficher les premiers caractères pour vérifier
    print("Base64 encodé (premiers 100 caractères):")
    print(pdf_base64[:100])
    print(f"\nLongueur totale : {len(pdf_base64)} caractères")

    # Pour sauvegarder dans un fichier texte
    with open(base64_text_path, 'w') as f:
        f.write(pdf_base64)
    base_64_decode_to_file(pdf_base64, output_pdf_path)

    print(f'''
        Original file : {pdf_path}
        Base64 encode text : {base64_text_path}
        Output pdf decoded file : {output_pdf_path}
    ''')
