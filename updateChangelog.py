import distro
import fileinput
import sys

if len(sys.argv) > 1:
    codename = sys.argv[1]
else:
    codename = distro.codename()

for line in fileinput.input("debian/changelog", inplace=True):
    print(line.replace(") replaceme", "~" + codename + ") " + codename), end="")
