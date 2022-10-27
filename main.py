import httpx

new_blocklist = []

with open("blocklists.txt", "r") as f:
    blocklists = [blocklist.strip() for blocklist in f.readlines()]

for blocklist in blocklists:
    new_blocklist.extend(
        [
            uri.split("#")[0].strip().split(" ")[-1]
            for uri in httpx.get(blocklist).text.split("\n")
            if not uri.strip().startswith("#") and len(uri.strip())
        ]
    )


print(f"Old combined adlist size: {len(new_blocklist)}")
new_blocklist = sorted(list(set(new_blocklist)))
print(f"New adlist size: {len(new_blocklist)}")

with open("blocklist.txt", "w") as f:
    f.write("# List created with https://github.com/RAV64/hostlist-duplicate-remover\n")
    f.write(f"# Blocklist size: {len(new_blocklist)}\n")
    f.write("# Combined blocklist from:\n")
    for blocklist in sorted(blocklists):
        f.write(f"# {blocklist}\n")
    f.write("\n".join(new_blocklist))
