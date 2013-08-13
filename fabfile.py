from fabric.api import local


def backup():
	local('git pull heroku master')
	local('git add .')

	print("enter your commit comment: ")
	comment = raw_input()
	local("git commit -m '%s'" % comment)
	
	local('git push')

# trick s3 in order to deploy
def switch_debug(what_to_change, change_to):
    local('cp django_test/local_settings.py django_test/local_settings.bak')
    
    sed = "sed 's/^DEBUG = %s$/DEBUG = %s/' django_test/local_settings.bak > django_test/local_settings.py"
    local(sed % (what_to_change, change_to))
    
    local('rm django_test/local_settings.bak')

def deploy():
	#local('pip freeze > requirements.txt')
    local('git pull')
    local('git add .')
    
    print("enter your commit comment: ")
    comment = raw_input()
    local("git commit -m '%s'" % comment)
    
    local('git push') 
    
    
    switch_debug('True', 'False')
    
    local('python manage.py collectstatic')
    
    switch_debug('False', 'True')
    
    # brings down server for a few seconds
    local('heroku maintenance:on')
    
    local('git push heroku')
    local('heroku run python manage.py migrate')
    
    local('heroku maintenance:off')