with open("day4/input4.txt") as f:
   lines = f.readlines()

messages = []
for line in lines:
    line = line.strip("\n")
    num = str(line)
    header = num[:4]

    if header != "5555":
        continue

    sender_num = num[4:12]
    seq_num = num[12:14]
    checksum = num[14:16]
    payload = num[16:]

    checktotal = 0
    for x in range(0, len(payload), 2):
        checktotal += int(payload[x:x+2],16)

    if checktotal % 256 == int(checksum, 16):
        messages.append([int(seq_num,16), payload])

messages = sorted(messages, key=lambda x: x[0])
messages = "".join([x[1] for x in messages])


print(bytearray.fromhex(messages).decode())