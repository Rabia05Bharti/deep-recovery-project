def read_blocks(file_path, block_size=4096):
    block_number = 1
    overlap = 512   # increased overlap (important)

    try:
        with open(file_path, "rb") as file:

            print("Starting disk scan...\n")
            found_types = set()

            while True:
                block = file.read(block_size)

                if not block:
                    break

                # ================= FILE TYPE DETECTION =================

                # PDF
                if b"%PDF" in block and "PDF" not in found_types:
                    print(f"PDF found in block {block_number}")
                    found_types.add("PDF")

                # PNG (full signature)
                if b"\x89PNG\r\n\x1a\n" in block and "PNG" not in found_types:
                    print(f"PNG found in block {block_number}")
                    found_types.add("PNG")

                # JPG (stronger detection)
                if (b"\xff\xd8" in block or b"\xff\xd8\xff\xe1" in block) and "JPG" not in found_types:
                    print(f"JPG found in block {block_number}")
                    found_types.add("JPG")

                # MP3
                if (b"ID3" in block or b"\xff\xfb" in block) and "MP3" not in found_types:
                    print(f"MP3 found in block {block_number}")
                    found_types.add("MP3")

                # MP4 (FIXED ❗ removed [:20])
                if b"ftyp" in block and "MP4" not in found_types:
                    print(f"MP4 found in block {block_number}")
                    found_types.add("MP4")

                # ======================================================

                # Debug: print first few blocks
                if block_number <= 5:
                    print(f"Reading block {block_number}, size={len(block)}")

                # ✅ STOP EARLY (important for demo)
                if len(found_types) == 5:
                    print("\nAll file types found!")
                    break

                yield block_number, block

                block_number += 1

                # ✅ Proper overlap (safe)
                if overlap > 0 and file.tell() > overlap:
                    file.seek(-overlap, 1)

        print("\nScan completed.")
        print("Found types:", found_types)

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")


# ================= TEST RUN =================
if __name__ == "__main__":
    file_path = "input/new_disk.img"

    for block_number, block in read_blocks(file_path):
        pass