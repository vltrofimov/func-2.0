class Contact():
    def __init__(self,name,surname,phone,best_contact='нет',**kwargs):
        self.name=name
        self.surname=surname
        self.phone=phone
        self.kwargs=kwargs
        self.best_contact=best_contact
    def str (self):
        print('имя: ',self.name)
        print('фамилия: ',self.surname)
        print('телефон: ',self.phone)
        print('в избранных:  ',self.best_contact)
        print('дополнительная информация: ')
        for x in self.kwargs:
                print('           ',x, ':', self.kwargs[x])

class PhoneBook():
    def __init__(self,name,*args):
        self.name=name
        self.args=list(args)

    def contact_add(self,contact):
        self.args.append(contact)

    def contacts_output(self):
    	for contact in self.args:
            contact.str()

    def contacts_dell(self,phone):
        for contact in self.args:
            if phone in contact.phone:
                self.args.remove(contact)

    def best_contacts_search(self):
        for contact in self.args:
            if contact.best_contact != 'нет':
                contact.str()

    def contact_search(self,name,surname):
        for contact in self.args:
            if contact.name == name and contact.surname == surname:
                contact.str()
        print('\n','search complited')

if __name__=="__main__":
    john = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    vlad = Contact('Vlad','Brown','+79134571828',telegram='@vlad',email='vlad@gmail.com')
    mary = Contact('Mary','Bush','+73281654',best_contact='+71234567809',telegram='@mary',email='mary@gmail.com')

    classmates = PhoneBook('classmates',john,vlad)
    classmates.contact_add(mary)
    classmates.contacts_output()
    classmates.contact_search('Mary','Bush')

