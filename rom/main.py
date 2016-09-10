import os, sys, argparse, binascii

parser = argparse.ArgumentParser()
parser.add_argument("-s", dest = "s", default = "inst_rom.s", type = str)
parser.add_argument("-o", dest = "o", default = "inst_rom.data", type = str)
parser.add_argument("-ld", dest = "ld", default = "ram.ld", type = str)
parser.add_argument("-bin", dest = "bin", default = "mips-gcc-4.8.1/bin", type = str)
args = parser.parse_args()

os.system("%s/mips-elf-as -mips32 %s -o inst_rom.o" % (args.bin, args.s))
os.system("%s/mips-elf-ld -T %s inst_rom.o -o inst_rom.om" % (args.bin, args.ld))
os.system("%s/mips-elf-objcopy -O binary inst_rom.om inst_rom.bin" % args.bin)

with open(args.o, "w") as f:
        s = binascii.b2a_hex(open("inst_rom.bin", "rb").read())
        for i in xrange(len(s) / 8):
                print >> f, s[i * 8 : (i + 1) * 8]

os.system("rm inst_rom.o inst_rom.om inst_rom.bin")