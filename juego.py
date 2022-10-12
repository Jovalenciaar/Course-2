

def read():
    general =[]
    with open('./archivos/data.txt', 'W', encoding='utf-8') as d:
          for line in d:
            general.append(int(line))
    print(general)

    
  

if __name__ == "__main__":
    read()