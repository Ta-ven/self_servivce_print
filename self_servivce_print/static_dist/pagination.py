

class Pagination():
    def __init__(self, total_count, current_page, html, per_page_num=10, max_page_num=7):
        self.total_count = total_count  # 数据总数
        try:
            self.current_page = int(current_page)  # 当前页
        except Exception as e:
            self.current_page = 1
        self.HTML = html  # 网址
        self.per_page_num = per_page_num  # 每页显示的行数
        self.max_page_num = max_page_num  # 最多显示页码

    @property
    def total_pages(self):
        a,b = divmod(self.total_count, self.per_page_num)
        if b==0:
            return a  # 总页数
        else:
            return (a+1)

    def start(self):
        if self.current_page>self.total_pages:  # 当页码大于总页数的时候
            self.current_page = self.total_pages
        elif self.current_page < 1:
            self.current_page = 1
        return (self.current_page-1)*self.per_page_num
    def end(self):
        return self.current_page*self.per_page_num

    @property
    def page_num_range(self):
        half_max_page = int(self.max_page_num / 2)
        if self.current_page-half_max_page < 1:
            return range(1, self.max_page_num+1)
        if self.current_page+half_max_page > self.total_pages:
            return range(self.total_pages-self.max_page_num+1, self.total_pages+1)
        return range(self.current_page-half_max_page, self.current_page+half_max_page+1)

    def page_str(self):
        page_list = []
        frist = "<a href='/%s/?Page=%s'>首页</a>"%(self.HTML, 1)
        page_list.append(frist)
        if self.current_page == 1:
            prev_page = "<a >上一页</a>"
        else:
            prev_page = "<a href='/%s/?Page=%s'>上一页</a>"%(self.HTML,self.current_page-1)
        page_list.append(prev_page)
        for i in self.page_num_range:
            temp = "<a href='/%s/?Page=%s'>%s</a>"%(self.HTML,i,i)
            page_list.append(temp)

        if self.current_page == self.total_pages:
            next_page = "<a>下一页</a>"
        else:
            next_page = "<a href='/%s/?Page=%s'>下一页</a>"%(self.HTML,self.current_page+1)
        page_list.append(next_page)
        last = "<a href='/%s/?p=%s'>尾页</a>" % (self.HTML,self.total_pages)
        page_list.append(last)
        return "".join(page_list)