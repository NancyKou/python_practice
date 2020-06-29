print('==================')
'''现有一个数据库记录文件（见附件0005_1.txt），保存了学生课程签到的数据库记录。 内容格式如下 ，
('2017-03-13 11:50:09', 271, 131),
('2017-03-14 10:52:19', 273, 131),
('2017-03-13 11:50:19', 271, 126),
每一行记录保存了学生的一次签到信息。
每一次签到信息的记录，分为三个部分， 分别是签到时间、签到课程的id号、签到学生的id号
要求大家实现下面的函数。其中参数fileName为
数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。

def putInfoToDict(fileName):
要求返回的字典对象的格式是这样的：key是各个学生的id号， value是该学生的签到信息
其中value，里面保存着该学生所有签到的信息
其中每个签到的信息是字典对象，有两个元素： key是lessonid的记录课程id，key是checkintime的
记录签到时间，比如，对于上面的示例中的3条记录，相应的返回结果如下：

{
    131: [
        {'lessonid': 271, 'checkintime': '2017-03-13 11:50:09'},
        {'lessonid': 273, 'checkintime': '2017-03-14 10:52:19'},
    ],

    126: [
        {'lessonid': 271, 'checkintime': '2017-03-13 11:50:19'},
    ],
}'''


def putInfoToDict(fileName):
    retDict = {}  #定义一个空字典
    with open('F:/0005_1.txt') as f:
        lines = f.read().splitlines() # 读取文件并按行进行分割
        for line in lines:
            line = line.replace('(', '').replace(')', '').replace(';', '').strip() #将左括号、右括号和空格去掉
            parts = line.split(',') #列表按照逗号进行分割

            ciTime = parts[0].strip().replace("'", '')  #以逗号为分隔符，再次进行切割，并取 索引值为0的值作为签到时间
            lessonid = int(parts[1].strip())  #课程id取索引值为1的值，并转化为int类型
            userid = int(parts[2].strip())  # 用户id取 索引值为2的值 ，并转化为int类型
            toAdd = {'lessonid': lessonid, 'checkintime': ciTime}  #子字典的组成
            # if userid not in retDict:
            #     retDict[userid] = []
            # retDict[userid].append(toAdd)
            retDict.setdefault(userid,[]).append(toAdd)
    return retDict
ret = putInfoToDict('0005_1.txt')
# print(ret)
import pprint
pprint.pprint(ret)