import csv

# 使用 regular reader 读取 csv 文件，并将数据写入新文件
def test_01():
    # 打开 csv 文件
    with open('test_file/cities.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # 跳过第一行
        next(csv_reader)
        # 打开新文件
        with open('test_file/new_cities.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter='\t')

            for line in csv_reader:
                csv_writer.writerow(line)

        new_file.close()

        # for line in csv_reader:
        #     print(line[8])

    # 关闭 csv 文件
    csv_file.close()

# 使用 regular reader 读取 csv 文件
def test_02():
    with open('test_file/new_cities.csv', 'r') as csv_file:
        # 错误示范：如果在读取时不加 delimiter='\t'，则会将整行数据作为一个元素
        # csv_reader = csv.reader(csv_file)
        # 正确示范：加上 delimiter='\t'，则会将每个元素分开
        csv_reader = csv.reader(csv_file, delimiter='\t')

        for line in csv_reader:
            print(line)
    csv_file.close()

# 使用 DictReader 读取 csv 文件
def test_03():
    with open('test_file/cities.csv', 'r') as csv_file:
        # 使用 DictReader 读取 csv 文件可以直接使用列名来读取数据，使其称为字典
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            print(line['City'])
    csv_file.close()

# 使用 DictWriter 写入 csv 文件
def test_04():
    with open('test_file/cities.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # 打开新文件
        with open('test_file/new_cities.csv', 'w') as new_file:
            # 定义列名, 顺序不需要和原文件相同
            fieldnames = ['State', 'EW', 'City']
            # 定义写入文件的格式
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=' ')
            # 将列名写入新文件的开头
            csv_writer.writeheader()
            # 将原文件中的数据写入新文件
            for line in csv_reader:
                # 删除不需要的列，顺序不需要和原文件相同
                del line['LatD']
                del line['LatM']
                del line['LatS']
                del line['NS']
                del line['LonD']
                del line['LonM']
                del line['LonS']
                csv_writer.writerow(line)
        new_file.close()
    csv_file.close()

'''
    csv 模块的常用方法：

        # 常规方法读取 csv 文件
        csv.reader(csvfile, dialect='excel', **fmtparams)
        csv.writer(csvfile, dialect='excel', **fmtparams)

        # 读取 csv 文件并将其转换为字典
        csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', *fmtparams)
        csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', *fmtparams)
'''

# test_01()
# test_02()
# test_03()
test_04()