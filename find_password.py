with open('Mgw7gQgWLIHhiEVkzCYySQ.6zu', 'rb+') as a:
    with open('20210302_232648.jpg', 'rb+') as b:
        with open('.ini.keyfile.ctr', 'rb+') as c:
            enc_img_byte = a.read(1)
            dec_img_byte = b.read(1)
            enc_pw_byte = c.read(1)

            password = ''
            while enc_pw_byte:
                decode = ord(enc_img_byte) ^ ord(dec_img_byte) ^ ord(enc_pw_byte)
                password += chr(decode)
                
                enc_img_byte = a.read(1)
                dec_img_byte = b.read(1)
                enc_pw_byte = c.read(1)

            print(password)
