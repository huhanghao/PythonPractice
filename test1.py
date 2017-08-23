import xlrd
import MySQLdb as mdb


def open_excel(file='pytest.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception:
        print("异常")


def excel_table_byindex(file='pytest.xls', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(1, nrows):

        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[i] = row[i]
            list.append(app)
    return list


def insertData2Sql():
    # 也可以使用字典进行连接参数的管理
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '137006hhh',
        'db': 'Test1',
        'charset': 'utf8'
    }

    # 设置数据连接
    conn = mdb.connect(**config)
    cursor = conn.cursor()

    try:
        # 插入数据
        value = [2, 1]
        cursor.execute('INSERT INTO Test(f1, f2) values(%s,%s)', value)

        # 查询多条记录
        results = cursor.fetchmany(5)
        for r in results:
            print (r)

        conn.commit()
    except Exception as e:
        # 发生错误时会滚
        conn.rollback()
    finally:

        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        conn.close()


def main():
    tables = excel_table_byindex()
    for row in tables:
        print(row)
    insertData2Sql()


if __name__ == "__main__":
    main()
