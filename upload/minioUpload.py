from minio import Minio

def minioUpload(upImage, name):
    access_key = "6YeaA8o3cmvCYlLx"
    secret_key = "XFIfhNSTqXjyNpr4IRZTPPdXNnHwoGMf"

    client = Minio("127.0.0.1:9000", access_key, secret_key, secure=False)


    found = client.bucket_exists("images")

    if not found:
        client.make_bucket("images")
    else:
        print("Bucket 'images' already exists")

    client.fput_object("images", name , upImage)
    print("Successfully uploaded")
