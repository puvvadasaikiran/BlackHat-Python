def printlist(inlist,indent=False,level=0):
	for each_item in inlist:
		if isinstance(each_item,list):
			printlist(each_item,indent,level+1)
		else:
			if(indent):
				for tabspace in range(level):
						print("\t",end='')
			print(each_item)


mani=['dd','dd','dd',[11,22,33,[44,11],33,22]]
printlist(mani,True)
