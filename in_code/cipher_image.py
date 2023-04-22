def cipher_image(path, key):
    """cipher image of a path given using the key

    Args:
        path (string): path where is the image
        key (_type_): key to use to encrypt a image
    """
    # try block to handle exception
    try:

        # print path of image file and encryption key that
        print('The path of file : ', path)
        print('Key for encryption : ', key)

        # open file for reading purpose
        file_image = open(path, 'rb')

        # storing image data in variable "image"
        image = file_image.read()
        file_image.close()

        # converting image into byte array to
        # perform encryption easily on numeric data
        image = bytearray(image)
    
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key
    
        # opening file for writing purpose
        file_image = open(path, 'wb')

        # writing encrypted data in image
        file_image.write(image)
        file_image.close()
        print('Encryption Done...')
     
    except Exception:
        print('Error caught : ', Exception.__name__)

def decrypt_image(filename, key):
    """decrypt a image using the key

    Args:
        path (string): path where the image is    
        key (int): key to decrypt the image
    """
    try:
        print('The path of file : ', filename)

        # if you try with other key different you couldn't open the file
        print('Note : Encryption key and Decryption key must be same.')
        print('Key for Decryption : ', key)

        # open file for reading purpose
        fin = open(filename, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()

        # converting image into byte array to perform decryption easily on numeric data
        image = bytearray(image)
 
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # create a new file and opening file for writing purpose
        image_decrypted = open('decripted-'+filename, 'wb+')

        # writing decryption data in image
        image_decrypted.write(image)
        image_decrypted.close()
        print('Decryption Done...')

    except Exception:
        print('Error caught : ', Exception.__name__)

cipher_image('kitten-02.jpeg', 32)
decrypt_image('kitten-02.jpeg', 32)