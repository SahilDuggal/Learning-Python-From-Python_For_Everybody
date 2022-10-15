text = "X-DSPAM-Confidence:    0.8475"

get_no_pos = text.find('0')
get_no = text[get_no_pos:]
print_no = float(get_no)

print(print_no)
print(type(print_no))
