import pyads as ads

AMSNETID = '10.0.2.15.1.1'

plc = ads.Connection(AMSNETID, ads.PORT_TC3PLC1)
plc.open()
print(f"Connected ? : {plc.is_open}")
print(f"Local Address ? : {plc.get_local_address()}")

liste = plc.get_all_symbols()

for item in liste:
    print(item.symbol_type)

plc.close()