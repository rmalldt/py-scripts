import os

# ------------------ Bytes


def bytes_info():
    mbytes = bytes([207, 128, 114, 194, 178])
    print(mbytes)
    print(type(mbytes))
    print(len(mbytes))

    for b in mbytes:
        print(b, end=",")
    print()

    print(mbytes.decode("utf-8"))

    # ------------------ Bytes and bitmap


"""
Bitmap file structure:

    - Bitmap file header: 14 bytes
        - Size: 2 bytes: The header filed used to identify the BMP and DIB file is 0x42 0x4D in hex, 
                         same as `BM` in ASCII.

        - Size: 4 bytes: The size of BMP file in bytes.

    - DIB               : Fixed size
"""
# source_file = "../data/texts/bm_test.txt"
source_file = "../data/bitmaps/vintage-halloween-bat.bmp"
inverted_file = "../data/bitmaps/inverted.bmp"


def invert_bitmap():
    with open(source_file, "rb") as bmfile:  # No encoding
        # Read the 14 byte header
        file_header = bmfile.read(14)

        bmp_id = file_header[0:2]  # check first 2 bytes to check valid BM file
        print(bmp_id)
        if bmp_id == b"BM":  # we have a Windows bitmap file
            # bitmap stores value little endian order
            file_size = int.from_bytes(file_header[2:6], "little")
            print(f"File size in header: {file_size}")
            os_size = os.path.getsize(source_file)
            print(f"File size reported by the operating system: {os_size}")

            # Check if file_sizes returned by file_header and os match
            if file_size != os_size:
                print(
                    "File size does not match file header size. "
                    "Are you sure this is a bitmap file?"
                )
            else:
                reserved = file_header[6:10]
                print(f"For information, reserved bytes are: {reserved}")

                offset = int.from_bytes(file_header[-4:], "little")
                print(f"Bitmap data starts at: {offset}")

                # Now read the DIB header and other information.
                # We're not interested in most of these values, but
                # we'll need them when writing the inverted file.
                # We read all bytes from the current position to 'offset'.
                # This gives us the number of bytes from where we are to the pixel data
                dib_header_etc = bmfile.read(offset - bmfile.tell())

                # Check DIB header size
                dib_header_size = int.from_bytes(dib_header_etc[0:4], "little")

                # We're only going to process BITMAPINFOHEADER files
                print(f"Bitmap header is {dib_header_size} bytes")
                if dib_header_size == 40:
                    image_width = int.from_bytes(
                        dib_header_etc[4:8], "little", signed=True
                    )
                    image_height = int.from_bytes(
                        dib_header_etc[8:12], "little", signed=True
                    )
                    print(f"image is {image_width} by {image_height}")

                    # Get the pixel data size (in bytes)
                    pixel_array_size = int.from_bytes(dib_header_etc[20:24], "little")
                    print(f"Size of pixel array (bytes) = {pixel_array_size}")

                    # Check: we should now be at 'offset' in the file.
                    current_position = bmfile.tell()
                    print(f"File pointer is at position {current_position}")
                    if current_position != offset:
                        print(
                            f"Something's gone wrong. We're at {current_position}, should be at {offset}"
                        )

                    bmfile.seek(offset)  # Strictly speaking, this is redundant.

                    # Read `pixel_array_size` bytes to get the image pixel data
                    image = bytearray(bmfile.read(pixel_array_size))

                    for index, byte in enumerate(image):
                        # Reverse the bits in each byte
                        image[index] = byte ^ 255

                    # Now read the remainder of the file (if any)
                    remainder = bmfile.read()

                    with open(inverted_file, "wb") as inverted_bmfile:
                        print(f"\tWriting header")
                        inverted_bmfile.write(file_header)
                        print(f"\tWriting DIB header and other blocks")
                        inverted_bmfile.write(dib_header_etc)
                        print(f"\tWriting image data")
                        inverted_bmfile.write(image)
                        if remainder:
                            print(f"\tWriting remaining bytes")
                            inverted_bmfile.write(remainder)

                    print(f"Image file {inverted_file} created.")
                else:
                    print(f"{source_file} is not a supported bitmap format.")
        else:
            print(f"{source_file} does not appear to be a bitmap (.bmp) file.")


# ------------------ Test

# bytes_info()
invert_bitmap()
