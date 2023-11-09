import base64


def base_64_encode(data: str):
    return base64.b64encode(data.encode()).decode()


def base_64_encode_file(filepath, encoding="ISO-8859-1"):
    return base_64_encode(open(filepath, encoding=encoding).read())


def base_64_decode(data: str):
    return base64.b64decode(data).decode()


def write_base_64_to_file(data: str, filepath: str, filename: str):
    destination = f"{filepath}/{filename}"
    with open(destination, "wb+") as f:
        f.write(base64.b64decode(data))
    return destination


def simple_pdf_to_base64(file):
    file_bytes = base64.b64encode(open(file, "rb").read())
    base_64 = file_bytes.decode("ascii")
    return base_64
