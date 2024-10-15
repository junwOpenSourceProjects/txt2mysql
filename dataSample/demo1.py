import os
import logging
import pymysql
from pymysql.err import OperationalError, IntegrityError, ProgrammingError

# 配置日志
logging.basicConfig(
	filename='university_rankings_import.log',
	level=logging.INFO,
	format='%(asctime)s - %(levelname)s - %(message)s'
)


def connect_to_mysql(host='localhost', user='root', password='junw', database='computer_rank', charset='utf8mb4'):
	try:
		connection = pymysql.connect(
			host=host,
			user=user,
			password=password,
			database=database,
			charset=charset,
			cursorclass=pymysql.cursors.DictCursor
		)
		logging.info("成功连接到MySQL数据库。")
		return connection
	except OperationalError as e:
		logging.error(f"无法连接到MySQL数据库: {e}")
		raise


def process_txt_file(file_path, connection):
	logging.info(f"开始处理文件: {file_path}")
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			lines = file.readlines()
	except FileNotFoundError:
		logging.error(f"文件未找到: {file_path}")
		return
	except Exception as e:
		logging.error(f"读取文件 {file_path} 时出错: {e}")
		return
	
	if not lines:
		logging.warning(f"文件为空: {file_path}")
		return
	
	# 跳过表头
	data_lines = lines[1:]
	if not data_lines:
		logging.warning(f"文件没有数据行: {file_path}")
		return
	
	insert_query = """
        INSERT INTO university_rankings_usnews (
            university_name_chinese,
            university_name_english,
            university_tags,
            university_tags_state,
            ranking_category,
            ranking_year,
            current_rank_integer,
            current_rank_raw,
            rank_variant
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
	
	with connection.cursor() as cursor:
		for line_num, line in enumerate(data_lines, start=2):
			line = line.strip()
			if not line:
				logging.warning(f"文件 {file_path} 第 {line_num} 行为空，跳过。")
				continue
			parts = line.split('\t')
			if len(parts) != 7:
				logging.error(f"文件 {file_path} 第 {line_num} 行数据格式不正确: {line}")
				continue
			
			try:
				university_name_chinese = parts[0].strip()
				university_name_english = parts[1].strip()
				
				# 处理大学标签，假设格式为 "国家, 洲"
				tags = parts[2].split(',')
				if len(tags) == 2:
					university_tags = tags[0].strip()
					university_tags_state = tags[1].strip()
				else:
					university_tags = tags[0].strip()
					university_tags_state = None  # 如果没有州信息
				
				ranking_category = parts[3].strip()
				ranking_year = int(parts[4].strip())
				current_rank_integer = int(parts[5].strip())
				current_rank_raw = parts[6].strip()
				
				# 根据需求，rank_variant 可以设置为 NULL 或其他逻辑
				rank_variant = None
				
				cursor.execute(insert_query, (
					university_name_chinese,
					university_name_english,
					university_tags,
					university_tags_state,
					ranking_category,
					ranking_year,
					current_rank_integer,
					current_rank_raw,
					rank_variant
				))
			except ValueError as ve:
				logging.error(f"文件 {file_path} 第 {line_num} 行数据类型转换错误: {ve} | 数据: {line}")
			except IntegrityError as ie:
				logging.error(
					f"文件 {file_path} 第 {line_num} 行插入数据库时出错 (IntegrityError): {ie} | 数据: {line}")
			except ProgrammingError as pe:
				logging.error(
					f"文件 {file_path} 第 {line_num} 行插入数据库时出错 (ProgrammingError): {pe} | 数据: {line}")
			except Exception as e:
				logging.error(f"文件 {file_path} 第 {line_num} 行插入数据库时出错: {e} | 数据: {line}")
	
	try:
		connection.commit()
		logging.info(f"成功将文件 {file_path} 的数据插入数据库。")
	except Exception as e:
		logging.error(f"提交事务时出错: {e}")


def main():
	logging.info("程序开始运行。")
	# 获取当前目录
	current_dir = os.getcwd()
	# 列出所有txt文件
	txt_files = [file for file in os.listdir(current_dir) if file.lower().endswith('.txt')]
	
	if not txt_files:
		logging.warning("当前目录下没有找到任何txt文件。")
		print("当前目录下没有找到任何txt文件。")
		return
	
	try:
		connection = connect_to_mysql()
	except Exception as e:
		logging.critical("无法继续程序运行，因为无法连接到数据库。")
		print("无法连接到数据库，检查日志以获取更多信息。")
		return
	
	for txt_file in txt_files:
		file_path = os.path.join(current_dir, txt_file)
		process_txt_file(file_path, connection)
	
	connection.close()
	logging.info("数据库连接已关闭。")
	logging.info("程序运行结束。")
	print("数据导入完成。请查看日志文件获取详细信息。")


if __name__ == "__main__":
	main()
