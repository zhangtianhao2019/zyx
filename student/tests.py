from django.test import TestCase,Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='nobody@the5fire.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )

    def test_creat_and_sex_show(self):
        student =Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        self.assertEqual(student.sex_show,'男','性别字段内容展示不一致！')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        name ='the5fire'
        student = Student.objects.filter(name=name)
        self.assertEqual(students.count(),1,
                         '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):
        client=Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200,'ststus code must be 200!')

    def test_post_student(self):
        client=Client()
        data=dict(
            name='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='程序员',
            qq='3333',
            phone='32222',
        )
        response = client.post('/',data)
        self.assertEqual(response.status_code,302,'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content,
                        'response content must contain 'test_for_post'')


# Create your tests here.
