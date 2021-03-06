列表和元组的使用场景那么列表和元组到底用哪一个呢？根据上面所说的特性，我们具体情况具体分析。
1. 如果存储的数据和数量不变，比如你有一个函数，需要返回的是一个地点的经纬度，然后直接传给前端渲染，那么肯定选用元组更合适。
def get_location():
    .....
    return (longitude, latitude)

2. 如果存储的数据或数量是可变的，比如社交平台上的一个日志功能，是统计一个用户在一周之内看了哪些用户的帖子，那么则用列表更合适。
viewer_owner_id_list = [] # 里面的每个元素记录了这个viewer一周内看过的所有owner的id
records = queryDB(viewer_id) # 索引数据库，拿到某个viewer一周内的日志
for record in records:
    viewer_owner_id_list.append(record.id)

总结关于列表和元组，我们今天聊了很多，最后一起总结一下你必须掌握的内容。
总的来说，列表和元组都是有序的，可以存储任意数据类型的集合，区别主要在于下面这两点。

列表是动态的，长度可变，可以随意的增加、删减或改变元素。列表的存储空间略大于元组，性能略逊于元组。
元组是静态的，长度大小固定，不可以对元素进行增加、删减或者改变操作。元组相对于列表更加轻量级，性能稍优。