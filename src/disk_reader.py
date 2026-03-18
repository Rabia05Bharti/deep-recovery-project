def read_blocks(file_path, block_size=4096):
    block_number = 1

    try:
        with open(file_path, "rb") as file:

            while True:
                block = file.read(block_size)

                if not block:
                    break

                if block_number<= 5:
                    print(f"Reading block{block_number},size={len(block)}")
                  
                    

               

                yield block_number,block

                block_number += 1

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")


# Test run
if __name__ == "__main__":
    file_path = "input/disk_btrfs.img"

    for block in read_blocks(file_path):
        pass