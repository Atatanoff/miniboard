import os


dir_file = 'data/'
name_file = 'reed.txt'
reed = []

def main():
    if not os.path.isdir(dir_file):
        os.mkdir(dir_file)
        with open(dir_file+name_file, 'w') as file:
            print("один", "два", "три", "четыре", sep='\n', file=file)

    #with open('')

if __name__=="__main__":
    main()