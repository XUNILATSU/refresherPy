end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

with open('image2.png', 'rb') as f:
    content = f.read()
    offset = content.index(end_hex)
    f.seek(offset + len(end_hex))

    with open('newexe.exe', 'wb') as e:
        e.write(f.read())