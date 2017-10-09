import os

dir_list = next(os.walk('.'))[1]
print ("# bugbounty-scans\n\naquatone results for sites with bug bountys")
print ("\n\nRaise an issue if you want a fresh scan or a new domain to be checked")
print ("\n\n")
print ("| Domain 	| Link 	|")
print ("|--------	|------	|")
for a in (dir_list):
	URL = "https://random-robbie.github.io/yahoo-bugbountyscans/"+a+"/report/report_page_0.html"
	print ("")
	if a == ".git":
		print ("")
	else:
		print('| '+a+'|<a href="'+URL+'">Link</a> |\n')
