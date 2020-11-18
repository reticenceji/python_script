#批量修改文件后缀名
import os
import argparse

#批量修改文件名，递归选项设成全局的了。问题不大
def batch_rename(work_dir,old_ext,new_ext):
	#os.scandir,Doc里建议用上下文管理器，但是好像没必要
	global recursive
	for entry in os.scandir(work_dir):
		if entry.is_file():
			#获取文件后缀
			front,ext = os.path.splitext(entry.name)
			if ext==old_ext:
				new_name = front+new_ext
				if os.path.exists(os.path.join(work_dir,new_name)):
					print("'{}' already exists.".format(os.path.join(work_dir,new_name)))
				else:
					print("rename '{}' to '{}'".format(os.path.join(work_dir,entry.name),os.path.join(work_dir,new_name)))
					os.rename(os.path.join(work_dir,entry.name),os.path.join(work_dir,new_name))
		#扫描的结果不包括.和..不用担心死递归吧？
		elif entry.is_dir(follow_symlinks=False) and recursive:
			batch_rename(os.path.join(work_dir,entry.name),old_ext,new_ext)

def main():
	#参数,help会自动生成
	parser = argparse.ArgumentParser(description="批量修改文件后缀名 By Reticenceji")
	parser.add_argument('-d',action='store',dest='dir',help="指定目标目录，默认是当前目录",default='.')
	parser.add_argument('-R',action='store_true',dest='r',help='如果指定了该参数，将递归的修改子目录的文件')
	parser.add_argument('--old',action='store',dest='old',help="旧文件后缀",required=True)
	parser.add_argument('--new',action='store',dest='new',help='新文件后缀',required=True)
	arguments = parser.parse_args()
	
	#处理
	work_dir = arguments.dir
	old_ext = arguments.old if arguments.old[0]=='.' else '.'+arguments.old
	new_ext = arguments.new if arguments.new[0]=='.' else '.'+arguments.new
	global recursive 
	recursive = arguments.r
	#print(work_dir,old_ext,new_ext,recursive)
	try:
		batch_rename(work_dir,old_ext,new_ext)
	except:
		print("Some error happend.Maybe limits of authority")
	print("Done")

if __name__ == "__main__":
	main()