from PIL import Image
import numpy as np
import sys

# Define the signature that marks the end of a PNG file in binary format
PNG_TERMINATOR = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'
EOF_SIGNATURE = ''.join(format(byte, '08b') for byte in PNG_TERMINATOR)

def retrieve_lsb(value, bit_count):
    
    return format(value, '08b')[-bit_count:]

def extract_lsb_for_bits(img_path, lsb_count):
    
    img = Image.open(img_path)
    img_pixels = np.array(img)
    img_height, img_width, _ = img_pixels.shape
    lsb_bits = []

    # Traverse the image diagonally to extract the LSBs
    for diag in range(img_width + img_height - 1):
        for row in range(max(0, diag - img_width + 1), min(diag + 1, img_height)):
            col = diag - row
            red, green, blue = img_pixels[row, col][:3]
            lsb_bits.append(retrieve_lsb(red, lsb_count))
            lsb_bits.append(retrieve_lsb(green, lsb_count))
            lsb_bits.append(retrieve_lsb(blue, lsb_count))

    # Combine all extracted bits into a single binary string
    bit_sequence = ''.join(lsb_bits)

    # Find the EOF signature in the extracted bits and truncate the bit sequence at EOF
    eof_pos = bit_sequence.find(EOF_SIGNATURE)
    if eof_pos != -1:
        bit_sequence = bit_sequence[:eof_pos + len(EOF_SIGNATURE)]

    # Convert the bit sequence to bytes
    extracted_data = int(bit_sequence, 2).to_bytes(len(bit_sequence) // 8, byteorder='big')

    output_filename = f"output-lsb-{lsb_count}-bits"
    with open(output_filename, "wb") as output:
        output.write(extracted_data)

    print(f"Extraction for {lsb_count} LSB(s) completed successfully. Saved to {output_filename}.")

def extract_least_significant_bits_range(img_path):
    # Iterate over bit counts from 8 down to 1
    for bits in range(8, 0, -1):
        print(f"Extracting for {bits} LSB(s)...")
        extract_lsb_for_bits(img_path, bits)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
    else:
        extract_least_significant_bits_range(sys.argv[1])
