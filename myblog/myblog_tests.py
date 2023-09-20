import os
import unittest
import tempfile
import myblog


class MyblogTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, myblog.app.config['DATABASE'] = tempfile.mkstemp()
        print(myblog.app.config['DATABASE'])
        myblog.app.config['TESTING'] = True
        self.app = myblog.app.test_client()
        myblog.init_table()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(myblog.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        print(str(rv.data))
        assert 'No entries here so far' not in str(rv.data)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        """test login、logout"""
        rv = self.login('name', 'password')
        assert 'You were logged in' in str(rv.data)

        rv = self.logout()
        assert 'You were logged out' in str(rv.data)


if __name__ == '__main__':
    unittest.main()