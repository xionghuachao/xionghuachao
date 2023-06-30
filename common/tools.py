import datetime
import os
def get_now_time():
    return datetime.datetime.now()
def get_project_path():
    #获取绝对路径
    project_name="web"
    file_path=os.path.dirname(__file__)

    return file_path[:file_path.find(project_name)+len(project_name)]
def sep(path,add_sep_before=False,add_sep_after=False):
    all_path=os.sep.join(path)
    if add_sep_before:
        all_path=os.sep+all_path
    if add_sep_after:
        all_path=all_path+os.sep
    return all_path
def get_img_path(img_name):
    """
    获取商品图片路径
    :param img_name:
    :return:
    """
    img_dir_path=get_project_path()+sep(["img",img_name],add_sep_before=True)
    return img_dir_path


if __name__=='__main__':
    print(get_img_path("2.jpg"))


