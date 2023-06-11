from minio import Minio
from minio.error import S3Error
import json
def get_cred(path):
    file_path = path
    with open(file_path, 'r') as j:
        data = json.load(j)
        #print(data)
    return data
def main():
    bucket_name = "python-test"
    minio_cred = get_cred('./minio_cred/credentials.json')
    # minio config
    clinet = Minio(
        minio_cred['url'].split('//')[1],
        access_key = minio_cred['accessKey'],
        secret_key = minio_cred['secretKey'],
        secure = False
    )
    
    found = clinet.bucket_exists(bucket_name)
    if not found:
        bucket_name = "new-python"
        clinet.make_bucket(bucket_name)
        
    else:
        print(f"Bucket {bucket_name} is existed !")
    
    #create hello.txt
    txt_path = './demo.txt'
    with open(txt_path, 'w') as f:
        f.write('hello minio!')
    
    # put hello.txt
    clinet.fput_object(
        bucket_name, "demo/here_is_test.txt", txt_path
    )

if __name__ == "__main__":
    #my_json = get_cred('./minio_cred/credentials.json')
    #print(my_json['url'])
    #print(my_json['url'].split('//'))
    #print("*"*40)
    #for k, v in my_json.items():
    #    print(f"key:{k}, value:{v}")
    try: 
        main()
    except S3Error as exc:
        print("error occurred.", exc)