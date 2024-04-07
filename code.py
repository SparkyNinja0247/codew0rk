import openpyxl


text = "martin.middle.wcpss.com"
parts = text.split(".")

last_two_parts = ".".join(parts[-2:])

for x in range(len(parts)-2):
	print(parts[x])
print(last_two_parts)

