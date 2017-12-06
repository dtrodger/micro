# import os
# import sys
# import unittest
#
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../..')))
#
# from project.extensions import sqldb, bcrypt
# from project.dbmodels.sqldb import User
# from project.utils.base_test import BaseTestCase
#
# from flask_security import current_user
#
# class UserTest(BaseTestCase):
#
#     def test_user_create(self):
#
#         self.testuser1 = self.user_api.create(email='test1@user.com', password='password1', confirmed=False, admin=False)
#         assert self.testuser1.email == User.query.filter_by(
#         email='test1@user.com').first().email
#         self.assertFalse(False)
#
#     def test_send_token_email(self):
#
#         self.user_api.send_token_email(self.testuser.email)
#         self.assertFalse(False)
#         self.assertTemplateUsed('emails/activate.html')
#
#     def test_request_password_reset(self):
#
#         self.user_api.request_password_reset(self.testuser.email)
#         self.assertFalse(False)
#         self.assertTemplateUsed('emails/reset.html')
#
#     def test_reset_password(self):
#
#         self.user_api.reset_password(self.testuser, password='test2')
#         testpassword = bcrypt.check_password_hash(self.testuser.password, 'test2')
#         self.assertFalse(False)
#         assert testpassword == True
#
#     def test_confirm(self):
#
#         self.user_api.confirm(self.testuser)
#         self.assertTrue(self.testuser.confirmed)
#         self.assertFalse(False)
#
#     def test_save_password_hash(self):
#
#         self.user_api.save_password_hash(self.testuser, password='password1')
#         testpassword = bcrypt.check_password_hash(self.testuser.password, 'password1')
#         self.assertFalse(False)
#         assert testpassword == True
#
#     def test_login(self):
#
#         user = self.user_api.login(self.user)
#         self.assertTrue(current_user.is_active())
#         self.assertTrue(current_user.is_authenticated)
#         self.assertFalse(False)
#
#     def test_logout(self):
#
#         self.user_api.login(self.user)
#         user = self.user_api.logout()
#         self.assertFalse(current_user.is_active)
#         self.assertFalse(current_user.is_authenticated)
#         self.assertFalse(False)
#
#     def test_generate_confirmation_token_and_confirm_token(self):
#
#         token = self.user_api.generate_confirmation_token('test@test1.com')
#         self.assertTrue(self.user_api.confirm_token(token, 1))
#         self.assertFalse(False)
#
#
# if __name__ == '__main__':
#     unittest.main()