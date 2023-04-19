# intro_python
* 4 Pages project 
* py -m venv  website
* website\Scripts\activate.bat
* py manage.py runserver
* py manage.py makemigrations members
* py manage.py migrate
* py manage.py shell
# from members.models import Member
* Member.objects.all()

* member = Member(firstname='Emil', lastname='Refsnes')
*  member.save()
# Execute this command to see if the Member table got a member:

* Member.objects.all().values()

# Add Multiple Records
* member1 = Member(firstname='Tobias', lastname='Refsnes')
* member2 = Member(firstname='Linus', lastname='Refsnes')
* member3 = Member(firstname='Lene', lastname='Refsnes')
* member4 = Member(firstname='Stale', lastname='Refsnes')
* member5 = Member(firstname='Jane', lastname='Doe')
* members_list = [member1, member2, member3, member4, member5]
*  for x in members_list:
*    x.save()
# get values 
* Member.objects.all().values()