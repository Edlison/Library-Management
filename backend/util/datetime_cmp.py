# @Author  : Edlison
# @Date    : 1/4/21 16:10
import datetime


def is_dt_later(dt1, dt2, fmt='%Y-%m-%d %H:%M:%S'):
    """
    比较日期大小，如果dt1 > dt2, 则返回True

    Args:

    Returns:

    @Author  : Edlison
    @Date    : 1/4/21 16:13
    """
    dt1 = datetime.datetime.strftime(dt1, fmt)
    dt2 = datetime.datetime.strftime(dt2, fmt)
    return dt1 > dt2

