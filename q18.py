physics=int(input('enter  physics no:'))
chemistry=int(input('enter chemistry no:'))
biology=int(input('enter biology no:'))
mathematics=int(input('enter mathematics no:'))
computer=int(input('enter computer no:'))
if physics>=90:
	print('gradeA')
elif chemistry>=80 and chemistry<=90:
	print('gradeB')
elif biology>=70 and biology<=80:
	print('gradeC')
elif mathematics>=60 and mathematics<=70:
	print('gradeD')
elif computer>=40 and computer<=60:
	print('gradeE')
else:
	print('gradeF')