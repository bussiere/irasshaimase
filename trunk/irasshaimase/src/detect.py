import bluetooth
file = open('reportTel.txt','w')
print "performing inquiry..."

nearby_devices = bluetooth.discover_devices(lookup_names = True)

print "found %d devices" % len(nearby_devices)
file.write("found %d devices \n" % len(nearby_devices))
for name, addr in nearby_devices:
    print "  %s - %s" % (addr, name)
    file.write("  %s - %s \n" % (addr, name))

file.close()