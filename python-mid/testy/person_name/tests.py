import unittest
from main import Person as PersonClass


class PersonTestCase(unittest.TestCase):
    def setUp(self):
        self.person = PersonClass()
        self.user_id = []
        self.user_name = []

    def test_0_set_name(self):
        print('Starting set_name test\n')
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.person.set_name(name)
            self.assertIsNotNone(user_id)
            self.user_id.append(user_id)
        print('user_id lenght', len(self.user_id))
        print(self.user_id)
        print('user_name_lenght', len(self.user_name))
        print('Finishing set_name test')

    def test_1_get_name(self):
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.person.set_name(name)
            self.user_id.append(user_id)

        print('Starting get_name test\n')
        lenght = len(self.user_id)
        print('lenght is equal to', lenght)
        print('Username lenght', len(self.user_name))
        for i in range(4):
            if i < lenght:
                print(self.user_id[i])
                print(self.person.get_name(self.user_id[i]))
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                self.assertEqual('There is no such user', self.person.get_name(i))

    def tearDown(self):
        del self.person, self.user_id, self.user_name


if __name__ == '__main__':
    unittest.main()







