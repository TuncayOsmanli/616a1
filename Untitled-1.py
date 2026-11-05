

parts = input().split()

values = []
missing = 0

for p in parts:
    if p == "NA":
        missing += 1
    else:
        values.append(float(p))

print("Ölcme:", len(values))
print("Boş:", missing)


print("Min:", min(values))
print("Max:", max(values))

average = round(sum(values) / len(values), 1)

print("Orta qiymət:", average)



def level(v):
    if v < -105:
        return "zəif"
    elif v < -95:
        return "orta"
    else:
        return "yaxşı"


for v in values:
    print(v, "->", level(v))



counts = {
    "zəif": 0,
    "orta": 0,
    "yaxşı": 0
}

for v in values:
    s = level(v)
    counts[s] += 1

print(counts)



share = round(counts["zəif"] / len(values) * 100, 1)

print("Zəif payı:", share, "%")

if share >= 30:
    print("Qerar: briqadanı göndər")
elif share >= 10:
    print("Qerar: müşahidədə saxla")
else:
    print("Qerar: stansiya normaldır")



current = 0
best = 0

for v in values:
    if level(v) == "zəif":
        current += 1

        if current > best:
            best = current
    else:
        current = 0

print("Ən uzun zəif seriya:", best)