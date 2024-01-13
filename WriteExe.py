end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

with open('image2.png', 'ab') as f, open('process64.exe', 'rb') as e:
    f.write(e.read())