# 用Python，读取txt数据，然后存入MySQL
# 我需要你完成一个Python程序。这个程序的功能是读取txt文件，然后将其中的数据存入MySQL数据库。
# txt中的文件是数据，格式类似于：
# 大学名称	大学英文名称	大学标签	排名名称	年份	当前排名（取整）	当前排名（原始数据）
# 慕尼黑工业大学	Technical University of Munich	德国, 欧洲	计算机科学	2015	32	=32
# 柏林洪堡大学	Humboldt University of Berlin	德国, 欧洲	计算机科学	2015	51	51-100
# 卡尔斯鲁厄理工学院	Karlsruhe Institute of Technology, Kit	德国, 欧洲	计算机科学	2015	51	51-100
# 慕尼黑大学	University of Munich	德国, 欧洲	计算机科学	2015	51	51-100
# 亚琛工业大学	Rwth Aachen University	德国, 欧洲	计算机科学	2015	51	51-100
# 柏林工业大学	Technical University of Berlin	德国, 欧洲	计算机科学	2015	51	51-100
# 海德堡大学	Heidelberg University	德国, 欧洲	计算机科学	2015	101	101-150
# 达姆施塔特工业大学	Technical University Darmstadt	德国, 欧洲	计算机科学	2015	101	101-150
# 萨尔大学	Saarland University	德国, 欧洲	计算机科学	2015	101	101-150
# 柏林自由大学	Free University of Berlin	德国, 欧洲	计算机科学	2015	151	151-200
# 德累斯顿工业大学	Dresden University of Technology	德国, 欧洲	计算机科学	2015	151	151-200
# 斯图加特大学	University of Stuttgart	德国, 欧洲	计算机科学	2015	151	151-200
# 波恩大学	University of Bonn	德国, 欧洲	计算机科学	2015	201	201-250
# 多特蒙德工业大学	Technical University of Dortmund	德国, 欧洲	计算机科学	2015	201	201-250
# 弗莱堡大学	University of Freiburg	德国, 欧洲	计算机科学	2015	201	201-250
# 图宾根大学	University of Tuebingen	德国, 欧洲	计算机科学	2015	251	251-300
# 埃朗根-纽伦堡大学	University of Erlangen, Nuremberg	德国, 欧洲	计算机科学	2015	251	251-300
# 莱比锡大学	University of Leipzig	德国, 欧洲	计算机科学	2015	251	251-300
# 德国基尔大学	University of Kiel	德国, 欧洲	计算机科学	2015	301	301-400
# 哥廷根大学	University of Goettingen	德国, 欧洲	计算机科学	2015	301	301-400
# 汉诺威大学	University of Hannover	德国, 欧洲	计算机科学	2015	301	301-400
# 波鸿大学	University of Bochum	德国, 欧洲	计算机科学	2015	301	301-400
# 不来梅大学	University of Bremen	德国, 欧洲	计算机科学	2015	301	301-400
# 杜伊斯堡-埃森大学	University of Duisburg, Essen	德国, 欧洲	计算机科学	2015	301	301-400
# 法兰克福大学	University of Frankfurt	德国, 欧洲	计算机科学	2015	301	301-400
# 汉堡大学	University of Hamburg	德国, 欧洲	计算机科学	2015	301	301-400
# 康斯坦茨大学	University of Konstanz	德国, 欧洲	计算机科学	2015	301	301-400
# 明斯特大学	University of Muenster	德国, 欧洲	计算机科学	2015	301	301-400
# 我的MySQL数据表已经设计好，建表语句如下：
# -- auto-generated definition
# create table university_rankings_qs
# (
# 	id                      int auto_increment comment '主键'
# 		primary key,
# 	university_name_chinese varchar(255) not null comment '大学名称（中文）',
# 	university_name_english varchar(255) not null comment '大学名称（英文）',
# 	university_tags         varchar(255) null comment '大学标签（例如：国家）',
# 	university_tags_state   varchar(255) null comment '大学标签（例如：洲）',
# 	ranking_category        varchar(100) not null comment '排名类别（例如：计算机科学）',
# 	ranking_year            year         not null comment '排名年份',
# 	current_rank_integer    int          not null comment '当前排名（整数）',
# 	current_rank_raw        varchar(10)  null comment '当前排名（原始数据，例如“=2”）',
# 	rank_variant            varchar(10)  null comment '排名类别'
# )
# 	comment '大学qs排名数据' charset = utf8mb4;

# 数据库登录账户root，密码：junw。computer_rank数据库中已经有university_rankings_qs表。
# 程序需要依次读取当前文件夹内的所有txt文件，每个文件都有表头，表头不要存入表格。
# 然后，每次读取完txt内的数据以后，将其存入university_rankings_qs表中。
# 程序需要处理异常情况，比如文件不存在、数据格式不正确等。
# 程序需要输出日志，记录程序运行的情况。
# 给我完整的Python代码，要能直接执行。
