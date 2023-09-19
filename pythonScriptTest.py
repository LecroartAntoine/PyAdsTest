import pyads as ads

AMSNETID = '192.168.1.35.1.1'
IPADR = ''

plc = ads.Connection(AMSNETID, ads.PORT_TC3PLC1, IPADR)
plc.open()
print(f"Connected ? : {plc.is_open}")
print(f"Local Address ? : {plc.get_local_address()}")

liste = plc.get_all_symbols()

for item in liste:
    print(item.symbol_type)

plc.close()